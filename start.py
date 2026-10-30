import os
import shutil
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

# ============================================================
# NutriWise Development Server Launcher - macOS
# ============================================================

ROOT_DIR = Path(__file__).resolve().parent

BACKEND_DIR = ROOT_DIR / "backend"
FRONTEND_DIR = ROOT_DIR / "frontend"

# Support virtual environments in the project root or backend.
VENV_CANDIDATES = [
    ROOT_DIR / ".venv" / "bin" / "python",
    ROOT_DIR / "venv" / "bin" / "python",
    BACKEND_DIR / ".venv" / "bin" / "python",
    BACKEND_DIR / "venv" / "bin" / "python",
]

VENV_PYTHON = next(
    (path for path in VENV_CANDIDATES if path.is_file()),
    None
)

FRONTEND_URL = "http://localhost:5173/"
BACKEND_URL = "http://127.0.0.1:8000/"
DOCS_URL = "http://127.0.0.1:8000/docs"

processes = []


def print_header():
    print()
    print("=" * 60)
    print("                 NutriWise")
    print("          macOS Development Launcher")
    print("=" * 60)
    print()
    print("Operating System             : macOS")
    print(f"Python                       : {VENV_PYTHON or 'Not found'}")
    print("Backend                      : FastAPI + Uvicorn")
    print("Frontend                     : React + Vite")
    print()
    print(f"Web Application              : {FRONTEND_URL}")
    print(f"Backend                      : {BACKEND_URL}")
    print(f"Backend Documentation        : {DOCS_URL}")
    print()
    print("=" * 60)
    print("Starting NutriWise servers...")
    print("=" * 60)
    print()


def check_paths():
    if not BACKEND_DIR.is_dir():
        sys.exit(f"ERROR: Backend folder not found:\n{BACKEND_DIR}")

    if not FRONTEND_DIR.is_dir():
        sys.exit(f"ERROR: Frontend folder not found:\n{FRONTEND_DIR}")

    if VENV_PYTHON is None:
        print("ERROR: macOS Python virtual environment not found.")
        print()
        print("Create one from the project root with:")
        print("  python3 -m venv .venv")
        print("  source .venv/bin/activate")
        print("  pip install -r backend/requirements.txt")
        sys.exit(1)

    if not (FRONTEND_DIR / "node_modules").is_dir():
        print("ERROR: Frontend dependencies are missing.")
        print("Run these commands:")
        print(f'  cd "{FRONTEND_DIR}"')
        print("  npm install")
        sys.exit(1)

    if shutil.which("npm") is None:
        sys.exit("ERROR: npm not found. Install Node.js and reopen Terminal.")


def start_backend():
    print("[BACKEND] Starting FastAPI...")

    process = subprocess.Popen(
        [
            str(VENV_PYTHON),
            "-m",
            "uvicorn",
            "main:app",
            "--reload",
            "--host",
            "127.0.0.1",
            "--port",
            "8000",
        ],
        cwd=str(BACKEND_DIR),
    )

    processes.append(process)
    return process


def start_frontend():
    print("[FRONTEND] Starting Vite development server...")

    process = subprocess.Popen(
        ["npm", "run", "dev", "--", "--host", "127.0.0.1"],
        cwd=str(FRONTEND_DIR),
    )

    processes.append(process)
    return process


def open_web_application():
    print("[WEB] Waiting for the development servers...")
    time.sleep(4)

    print("[WEB] Opening NutriWise in your default browser...")
    webbrowser.open(FRONTEND_URL)

    print("[WEB] Backend documentation:", DOCS_URL)


def stop_servers():
    print()
    print("Stopping NutriWise servers...")

    for process in reversed(processes):
        if process.poll() is None:
            process.terminate()

    for process in reversed(processes):
        if process.poll() is None:
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()

    print("NutriWise servers stopped.")


def main():
    print_header()
    check_paths()

    try:
        start_backend()
        time.sleep(2)

        if processes[0].poll() is not None:
            raise RuntimeError(
                "Backend stopped during startup. Check the error above."
            )

        start_frontend()
        open_web_application()

        print()
        print("=" * 60)
        print("NutriWise launcher is running!")
        print("=" * 60)
        print()
        print(f"Frontend : {FRONTEND_URL}")
        print(f"Backend  : {BACKEND_URL}")
        print(f"Swagger  : {DOCS_URL}")
        print()
        print("Keep this Terminal open while developing.")
        print("Press CTRL + C to stop both servers.")
        print("=" * 60)
        print()

        while True:
            for process in processes:
                if process.poll() is not None:
                    raise RuntimeError(
                        "A development server stopped. Check its output above."
                    )
            time.sleep(1)

    except KeyboardInterrupt:
        pass
    except RuntimeError as error:
        print(f"\nERROR: {error}")
    finally:
        stop_servers()


if __name__ == "__main__":
    main()