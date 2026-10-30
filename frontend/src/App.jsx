import { useEffect, useState } from "react";
const API_URL =
import.meta.env.VITE_API_URL || "${API_URL}";
import "./App.css";
import {
  Leaf,
  ScanLine,
  Sparkles,
  CircleUserRound,
  SlidersHorizontal,
  Bell,
  ChevronDown,
  ArrowRight,
  Camera,
  Search,
  ShieldCheck,
  History,
  Filter,
  Flame,
  Utensils,
  TrendingUp,
  CalendarDays,
  UserRound,
  Target,
  Ruler,
  Weight,
  Activity,
  Apple,
  Check,
  Pencil,
  CheckCircle2,
} from "lucide-react";

const foodImages = import.meta.glob(
  "./assets/food-images/*.{png,jpg,jpeg,webp}",
  {
    eager: true,
    query: "?url",
    import: "default",
  }
);

const getFoodImage = (foodName) => {
  if (!foodName) return null;

  const fileName = foodName
    .trim()
    .toLowerCase()
    .replace(/[()]/g, "")
    .replace(/\//g, "-")
    .replace(/\s+/g, "-");

  const extensions = ["png", "jpg", "jpeg", "webp"];

  for (const extension of extensions) {
    const imagePath = `./assets/food-images/${fileName}.${extension}`;

    if (foodImages[imagePath]) {
      return foodImages[imagePath];
    }
  }

  return null;
};


function LoginPage({ onLogin, onCreateAccount }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    onLogin({
      username,
      password,
    });
  };

  return (
    <div className="login-page">
      <div className="login-card">

        <div className="login-logo">
          <div className="logo-icon">
            <Leaf size={19} />
          </div>

          <span>NutriWise</span>
        </div>

        <div className="login-heading">
          <p className="eyebrow">WELCOME BACK</p>

          <h2>Your wellness journey continues here.</h2>

          <p>
            Sign in to continue to your personalized nutrition space.
          </p>
        </div>

        <form className="login-form" onSubmit={handleSubmit}>

          <div className="login-field">
            <label htmlFor="username">
              Email
            </label>

            <input
              id="username"
              type="email"
              value={username}
              onChange={(event) => setUsername(event.target.value)}
              placeholder="Enter your email"
              required
            />
          </div>

          <div className="login-field">
            <label htmlFor="password">
              Password
            </label>

            <input
              id="password"
              type="password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              placeholder="Enter your password"
              required
            />
          </div>

          <button
            type="submit"
            className="btn-primary login-button"
          >
            Sign in
            <ArrowRight size={17} />
          </button>

        </form>

                <div className="login-note">
          <ShieldCheck size={16} />

          <span>
            Your account information is securely protected.
          </span>
        </div>

        <div className="auth-switch">
          <span>Don't have an account?</span>

          <button
            type="button"
            onClick={onCreateAccount}
          >
            Create account
          </button>
        </div>

      </div>
    </div>
  );
}

function CreateAccountPage({ onBackToLogin }) {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    age: "",
    gender: "",
    height: "",
    weight: "",
    activity_level: "",
    goal: "",
    food_preference: "",
  });

  const handleChange = (event) => {
    const { name, value } = event.target;

    setFormData((previous) => ({
      ...previous,
      [name]: value,
    }));
  };

  const handleSubmit = async (event) => {
  event.preventDefault();

  try {
    const userResponse = await fetch(
      `${API_URL}/users/`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: formData.name,
          email: formData.email,
          password: formData.password,
        }),
      }
    );

    const userData = await userResponse.json();

    if (!userResponse.ok) {
      alert(userData.detail || "Unable to create account.");
      return;
    }

    const profileResponse = await fetch(
      `${API_URL}/users/${userData.id}/profile`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          age: Number(formData.age),
          height: Number(formData.height),
          weight: Number(formData.weight),
          activity_level: formData.activity_level,
          calorie_target: null,
          goal: formData.goal,
          food_preference: formData.food_preference,
          gender: formData.gender,
        }),
      }
    );

    const profileData = await profileResponse.json();

    if (!profileResponse.ok) {
      alert(
        profileData.detail ||
        "Account was created, but the profile could not be created."
      );
      return;
    }

    console.log("Account created:", userData);
    console.log("Profile created:", profileData);

    alert("Account created successfully! Please sign in.");

    onBackToLogin();

  } catch (error) {
    console.error("Registration request failed:", error);
    alert("Unable to connect to NutriWise server.");
  }
};

  return (
    <div className="login-page">
      <div className="login-card">

        <div className="login-logo">
          <div className="logo-icon">
            <Leaf size={19} />
          </div>

          <span>NutriWise</span>
        </div>

        <div className="login-heading">
          <p className="eyebrow">CREATE YOUR ACCOUNT</p>

          <h2>Start your wellness journey.</h2>

          <p>
            Tell us a little about yourself so NutriWise can personalize
            your nutrition experience.
          </p>
        </div>

        <form className="login-form" onSubmit={handleSubmit}>

          <div className="login-field">
            <label htmlFor="name">Full name</label>

            <input
              id="name"
              name="name"
              type="text"
              value={formData.name}
              onChange={handleChange}
              placeholder="Enter your name"
              required
            />
          </div>

          <div className="login-field">
            <label htmlFor="email">Email</label>

            <input
              id="email"
              name="email"
              type="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="Enter your email"
              required
            />
          </div>

          <div className="login-field">
            <label htmlFor="password">Password</label>

            <input
              id="password"
              name="password"
              type="password"
              value={formData.password}
              onChange={handleChange}
              placeholder="Create a password"
              required
            />
          </div>

          <div className="login-field">
            <label htmlFor="age">Age</label>

            <input
              id="age"
              name="age"
              type="number"
              value={formData.age}
              onChange={handleChange}
              placeholder="Enter your age"
              required
            />
          </div>

          <div className="login-field">
            <label htmlFor="gender">Gender</label>

            <select
              id="gender"
              name="gender"
              value={formData.gender}
              onChange={handleChange}
              required
            >
              <option value="">Select gender</option>
              <option value="Male">Male</option>
              <option value="Female">Female</option>
              <option value="Other">Other</option>
            </select>
          </div>

          <div className="login-field">
            <label htmlFor="height">Height (cm)</label>

            <input
              id="height"
              name="height"
              type="number"
              value={formData.height}
              onChange={handleChange}
              placeholder="e.g. 175"
              required
            />
          </div>

          <div className="login-field">
            <label htmlFor="weight">Weight (kg)</label>

            <input
              id="weight"
              name="weight"
              type="number"
              value={formData.weight}
              onChange={handleChange}
              placeholder="e.g. 70"
              required
            />
          </div>

          <div className="login-field">
            <label htmlFor="activity_level">Activity level</label>

            <select
              id="activity_level"
              name="activity_level"
              value={formData.activity_level}
              onChange={handleChange}
              required
            >
              <option value="">Select activity level</option>
              <option value="sedentary">Sedentary</option>
              <option value="light">Lightly active</option>
              <option value="moderate">Moderately active</option>
              <option value="active">Very active</option>
            </select>
          </div>

          <div className="login-field">
            <label htmlFor="goal">Your goal</label>

            <select
              id="goal"
              name="goal"
              value={formData.goal}
              onChange={handleChange}
              required
            >
              <option value="">Select your goal</option>
              <option value="weight_loss">Weight Loss</option>
              <option value="muscle_gain">Muscle Gain</option>
              <option value="maintain_weight">Maintain Weight</option>
              <option value="general_health">General Health</option>
            </select>
          </div>

          <div className="login-field">
            <label htmlFor="food_preference">Food preference</label>

            <select
              id="food_preference"
              name="food_preference"
              value={formData.food_preference}
              onChange={handleChange}
              required
            >
              <option value="">Select preference</option>
              <option value="vegetarian">Vegetarian</option>
              <option value="non_vegetarian">Non-vegetarian</option>
              <option value="vegan">Vegan</option>
              <option value="eggetarian">Eggetarian</option>
            </select>
          </div>

          <button
            type="submit"
            className="btn-primary login-button"
          >
            Create account
            <ArrowRight size={17} />
          </button>

        </form>

        <div className="auth-switch">
          <span>Already have an account?</span>

          <button
            type="button"
            onClick={onBackToLogin}
          >
            Sign in
          </button>
        </div>

        <div className="login-note">
          <ShieldCheck size={16} />

          <span>
            Your information is securely protected.
          </span>
        </div>

      </div>
    </div>
  );
}


function OverviewPage({ onAnalyze, dailySummary, foodHistory, profile, goalData }) {
  const calorieTarget =
    Number(goalData?.calorie_calculation?.recommended_daily_calories) || 2125;

  const proteinTarget =
    Number(goalData?.protein_calculation?.recommended_daily_protein) || 112;

  const carbsTarget = 240;
  const fatTarget = 71;

  const calories = dailySummary?.total_calories || 0;
  const protein = dailySummary?.total_protein || 0;
  const carbs = dailySummary?.total_carbohydrates || 0;
  const fat = dailySummary?.total_fat || 0;

  const caloriePercent = Math.min(
    Math.round((calories / calorieTarget) * 100),
    100
  );

  const proteinPercent = Math.min(
    Math.round((protein / proteinTarget) * 100),
    100
  );

  const carbsPercent = Math.min(
    Math.round((carbs / carbsTarget) * 100),
    100
  );

  const fatPercent = Math.min(
    Math.round((fat / fatTarget) * 100),
    100
  );

  const getMealFoods = (mealType) => {
  const today = new Date().toDateString();

  return (foodHistory || []).filter((item) => {
    if (!item.consumed_at) {
      return false;
    }

    const itemDate = new Date(item.consumed_at).toDateString();

    return (
      itemDate === today &&
      item.meal_type === mealType
    );
  });
};

  const getMealCalories = (mealType) => {
    return getMealFoods(mealType).reduce(
      (total, item) => total + (item.calories || 0),
      0
    );
  };

  const mealDescription = (mealType) => {
    const foods = getMealFoods(mealType);

    if (foods.length === 0) {
      return "Nothing logged yet";
    }

    return foods
      .map((item) => `${item.food_name || "Food"} (${item.quantity}g)`)
      .join(", ");
  };

  const renderMealRow = (mealType, iconClass, label) => {
    const foods = getMealFoods(mealType);
    const mealCalories = getMealCalories(mealType);

    return (
      <div className="meal-row">
        <div className={`meal-icon ${iconClass}`}>
          <Utensils size={18} />
        </div>

        <div className="meal-info">
          <strong>{label}</strong>
          <span>{mealDescription(mealType)}</span>
        </div>

        {foods.length > 0 ? (
          <>
            <span className="meal-calories">
              {Math.round(mealCalories)} kcal
            </span>

           <span className="meal-status complete">
              <CheckCircle2 size={16} />
              Logged
            </span>
          </>
        ) : (
          <button
            className="meal-action"
            onClick={onAnalyze}
          >
            Add <ArrowRight size={15} />
          </button>
        )}
      </div>
    );
  };

  return (
    <main className="page-content overview-page">
      <div className="overview-intro">
        <div>
          <p className="eyebrow">YOUR DAILY OVERVIEW</p>

          <h2>Small choices add up.</h2>

          <p className="intro-text">
            Here's how your nutrition is looking today. No pressure, just
            information to help you feel your best.
          </p>
        </div>

        <button className="btn-primary" onClick={onAnalyze}>
          <ScanLine size={18} />
          Analyze a meal
        </button>
      </div>

      <section className="nutrition-grid">
        <NutritionCard
          title="Calories"
          value={Math.round(calories)}
          target={calorieTarget}
          unit="kcal"
          percent={caloriePercent}
          type="calories"
        />

        <NutritionCard
          title="Protein"
          value={protein.toFixed(1)}
          target={proteinTarget}
          unit="g"
          percent={proteinPercent}
          type="protein"
        />

        <NutritionCard
          title="Carbs"
          value={carbs.toFixed(1)}
          target={carbsTarget}
          unit="g"
          percent={carbsPercent}
          type="carbs"
        />

        <NutritionCard
          title="Fats"
          value={fat.toFixed(1)}
          target={fatTarget}
          unit="g"
          percent={fatPercent}
          type="fats"
        />
      </section>

      <div className="overview-main-grid">
        <section>
          <div className="section-heading">
            <div>
              <p className="eyebrow">TODAY</p>
              <h3>Today's rhythm</h3>
            </div>

            <button className="text-button">View details</button>
          </div>

          <div className="card rhythm-card">
            <div className="meal-list">

              {renderMealRow(
                "Breakfast",
                "breakfast",
                "Breakfast"
              )}

              {renderMealRow(
                "Lunch",
                "lunch",
                "Lunch"
              )}

              {renderMealRow(
                "Dinner",
                "dinner",
                "Dinner"
              )}

              {renderMealRow(
                "Snack",
                "snack",
                "Snack"
              )}

            </div>
          </div>
        </section>

        <section>
          <div className="section-heading">
            <div>
              <p className="eyebrow">A LITTLE GUIDANCE</p>
              <h3>NutriWise Insight</h3>
            </div>
          </div>

          <div className="card insight-card">
            <div className="insight-ring">
              <Sparkles size={24} />
            </div>

            <div className="insight-content">
              <h4>You're building a balanced day</h4>

              <p>
                You've got a good start on protein today. Adding a
                protein-rich dinner could help you comfortably reach your
                target.
              </p>

              <button className="insight-button">
                See protein-rich foods <ArrowRight size={15} />
              </button>
            </div>
          </div>
        </section>
      </div>

      <section className="streak-banner">
        <div className="streak-left">
          <div className="streak-icon">
            <Flame size={20} />
          </div>

          <div>
            <strong>You're on a 7-day rhythm</strong>
            <span>Keep showing up for yourself.</span>
          </div>
        </div>

        <div className="streak-days">
          <span className="streak-day done">M</span>
          <span className="streak-day done">T</span>
          <span className="streak-day done">W</span>
          <span className="streak-day done">T</span>
          <span className="streak-day done">F</span>
          <span className="streak-day done">S</span>
          <span className="streak-day today">S</span>
        </div>
      </section>
    </main>
  );
}



  function NutritionCard({ title, value, target, unit, percent, type }) {
    return (
      <div className={`nutrition-card ${type}`}>
        <div className="nutrition-card-top">
          <div className="nutrition-title">
            <span className={`nutrition-dot ${type}`}></span>
            {title}
          </div>
        </div>

        <div className="nutrition-value">
          {value}
          <span>{unit}</span>
        </div>

        <div className="nutrition-progress">
          <div
            className={`nutrition-progress-bar ${type}`}
            style={{ width: `${percent}%` }}
          ></div>
        </div>

        <div className="nutrition-bottom">
          <span>{percent}% of target</span>
          <span>{target} {unit}</span>
        </div>
      </div>
    );
  }


function AnalyzeFoodPage({ onFoodAdded, profile, setCurrentPage }) {
  const [description, setDescription] = useState("");
  const [foods, setFoods] = useState([]);
  const [searching, setSearching] = useState(false);
  const [showExplorePage, setShowExplorePage] = useState(false);


  const [selectedFood, setSelectedFood] = useState(null);
  const [quantity, setQuantity] = useState(100);
  const [mealType, setMealType] = useState("Breakfast");

  const [aiResult, setAiResult] = useState(null);
  const [aiAnalyzing, setAiAnalyzing] = useState(false);
  const [healthierFood, setHealthierFood] = useState(null);
  const [aiAlternativeSelected, setAiAlternativeSelected] = useState(false);


  console.log("ANALYZE PROFILE:", profile);

const getGoalFit = (nutrition) => {
  if (!nutrition || !profile?.goal) {
    return null;
  }

  const goal = profile.goal.toLowerCase();

  const calories = Number(nutrition.calories || 0);
  const protein = Number(nutrition.protein || 0);
  const fat = Number(nutrition.fat || 0);
  const carbohydrates = Number(nutrition.carbohydrates || 0);
  const fiber = Number(nutrition.fiber || 0);

  if (goal === "weight_loss") {
    if (calories <= 300 && protein >= 5 && fiber >= 2) {
      return {
        status: "Good Fit",
        message:
          "This food can fit well into a weight-loss diet when eaten in a suitable portion."
      };
    }

    if (calories <= 400) {
      return {
        status: "Moderate Fit",
        message:
          "This food can fit your weight-loss goal, but portion size is important."
      };
    }

    return {
      status: "Limit",
      message:
        "This food is relatively calorie-dense, so a smaller portion may be better for your goal."
    };
  }

  if (goal === "muscle_gain") {
    if (protein >= 15) {
      return {
        status: "Good Fit",
        message:
          "This food provides a useful amount of protein for a muscle-gain diet."
      };
    }

    return {
      status: "Moderate Fit",
      message:
        "This food can be included, but consider pairing it with a higher-protein food."
    };
  }

  if (goal === "maintain_weight") {
    if (calories <= 400 && fiber >= 2) {
      return {
        status: "Good Fit",
        message:
          "This food can fit a balanced maintenance diet in a suitable portion."
      };
    }

    return {
      status: "Moderate Fit",
      message:
        "This food can fit your maintenance goal, but keep the portion appropriate."
    };
  }

  if (goal === "general_health") {
    if (fiber >= 2 && calories <= 400) {
      return {
        status: "Good Fit",
        message:
          "This food can fit a balanced diet when included in an appropriate portion."
      };
    }

    return {
      status: "Moderate Fit",
      message:
        "This food can be included as part of a varied and balanced diet."
    };
  }

  return null;
};

    const getHealthierRecommendation = async (food) => {
    if (!food || !profile?.goal) {
      return null;
    }

    try {
      const response = await fetch(
        `${API_URL}/foods/`
      );

      if (!response.ok) {
        return null;
      }

      const foods = await response.json();

      const candidates = foods.filter(
        (item) =>
          Number(item.id) !== Number(food.id) &&
          item.category === food.category
      );
    
      if (candidates.length === 0) {
        return null;
      }

      const goal = profile.goal.toLowerCase();

      let sortedFoods = [...candidates];

      if (goal === "weight_loss") {
        sortedFoods.sort((a, b) => {
          const scoreA =
            Number(a.calories || 0) -
            Number(a.protein || 0) * 5 -
            Number(a.fiber || 0) * 3;

          const scoreB =
            Number(b.calories || 0) -
            Number(b.protein || 0) * 5 -
            Number(b.fiber || 0) * 3;

          return scoreA - scoreB;
        });
      } else if (goal === "muscle_gain") {
        sortedFoods.sort(
          (a, b) =>
            Number(b.protein || 0) -
            Number(a.protein || 0)
        );
      } else {
        sortedFoods.sort(
          (a, b) =>
            Number(a.calories || 0) -
            Number(b.calories || 0)
        );
      }

          return sortedFoods[0];
    } catch (error) {
      console.error("Recommendation error:", error);
      return null;
    }
  };


  useEffect(() => {
    if (!description.trim()) {
      setFoods([]);
      return;
    }

    const timer = setTimeout(() => {
      setSearching(true);

      const token = localStorage.getItem("access_token");

      fetch(
        `${API_URL}/foods/search?name=${encodeURIComponent(
          description
        )}`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      )
        .then((response) => {
          if (!response.ok) {
            throw new Error("Food search failed");
          }

          return response.json();
        })
        .then((data) => {
          console.log("Food search results:", data);
          setFoods(data);
        })
        .catch((error) => {
          console.error("Food search failed:", error);
          setFoods([]);
        })
        .finally(() => {
          setSearching(false);
        });
    }, 400);

    return () => clearTimeout(timer);
  }, [description]);

  return (
    <main className="page-content analyze-page">
      <div className="analyze-intro">
        <p className="eyebrow">FOOD ANALYSIS</p>

        <h2>What are you enjoying?</h2>

        <p className="intro-text">
          Snap a photo or tell us what's on your plate. We'll help you
          understand it without the judgment.
        </p>
      </div>

      <div className="analysis-steps">
  <div className={`analysis-step ${!aiResult ? "active" : "completed"}`}>
    <span className="step-number">1</span>
    <span>AI detection</span>
  </div>

  <span className="step-line"></span>

  <div className={`analysis-step ${selectedFood ? "active" : ""}`}>
    <span className="step-number">2</span>
    <span>Nutrition</span>
  </div>

  <span className="step-line"></span>

  <div className={`analysis-step ${getGoalFit(
    selectedFood
      ? {
          calories: Number(selectedFood.calories || 0),
          protein: Number(selectedFood.protein || 0),
          carbohydrates: Number(selectedFood.carbohydrates || 0),
          fat: Number(selectedFood.fat || 0),
          sugar: Number(selectedFood.sugar || 0),
          fiber: Number(selectedFood.fiber || 0),
        }
      : null
  ) ? "active" : ""}`}>
    <span className="step-number">3</span>
    <span>Goal fit</span>
  </div>

  <span className="step-line"></span>

  <div className={`analysis-step ${healthierFood ? "active" : ""}`}>
    <span className="step-number">4</span>
    <span>Your next step</span>
  </div>
</div>

      <section className="card analyze-card">
        <div className="photo-upload-side">
  <div className="upload-area">
    <div className="upload-icon">
      <Camera size={25} />
    </div>

    <h3>
  {aiAnalyzing
    ? "Analyzing your food..."
    : "Drop a meal photo here"}
</h3>

<p>
  {aiAnalyzing
    ? "AI is identifying your food and nutrition."
    : "JPG or PNG · up to 10MB"}
</p>

    <input
      type="file"
      accept="image/jpeg,image/png"
      id="food-image-upload"
      style={{ display: "none" }}

      onChange={async (event) => {
  const file = event.target.files[0];

  if (!file) {
    return;
  }

  if (file.size > 10 * 1024 * 1024) {
    alert("Please choose an image smaller than 10MB.");
    return;
  }

  console.log("Food image selected:", file);

  const token = localStorage.getItem("access_token");

  const formData = new FormData();
  formData.append("file", file);

  try {
    setAiAnalyzing(true);
    const response = await fetch(
      `${API_URL}/ai/analyze-food`,
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
        },
        body: formData,
      }
    );

    if (!response.ok) {
      throw new Error("Food image upload failed");
    }

    const data = await response.json();

    console.log("AI analysis response:", data);

if (!data.success) {
  throw new Error(data.error || "AI analysis failed");
}

setAiResult(data);

if (data.nutrition) {
  setSelectedFood(data.nutrition);
  setDescription(data.nutrition.name);
  setQuantity(data.nutrition.serving_size || 100);

  const recommendation = await getHealthierRecommendation(
  data.nutrition
);

setHealthierFood(recommendation);
}

    } catch (error) {
    console.error("AI image upload failed:", error);
    alert("Could not analyze the image.");
  } finally {
    setAiAnalyzing(false);
  }
}}
    />

    <label
      htmlFor="food-image-upload"
      className="btn-secondary"
    >
      Choose a photo
    </label>
  </div>
</div>

        <div className="description-side">
          <div className="or-divider">
            <span>OR DESCRIBE IT</span>
          </div>

          <label className="label">
            Tell us what's on your plate
          </label>

          <div className="food-search">
            <Search size={18} />

            <input
              type="text"
              value={description}
              onChange={(event) => setDescription(event.target.value)}
              placeholder="e.g. Dal, rice and mixed vegetables"
            />
          </div>

          <button
            type="button"
            className="explore-foods-button"
            onClick={() => setCurrentPage("explore")}
          >
            Explore All Foods
          </button>

          {searching && (
            <p className="suggestion-label">
              SEARCHING FOODS...
            </p>
          )}

          {!searching && foods.length > 0 && (
  <div className={showExplorePage ? "explore-food-grid" : "food-search-results"}>
    {foods.map((food) => (
      <button
        key={food.id}
        type="button"
        className={showExplorePage ? "explore-food-card" : "food-result-item"}
        onClick={() => {
          setDescription(food.name);
          setSelectedFood(food);
          setQuantity(food.serving_size || 100);
          setAiAlternativeSelected(false);
          setFoods([]);
          setShowExplorePage(false);
        }}
      >
        <div>
  <div className="explore-food-image-wrapper">
    {getFoodImage(food.name) ? (
      <img
        src={getFoodImage(food.name)}
        alt={food.name}
        className="explore-food-image"
      />
    ) : (
      <div className="explore-food-image-placeholder">
        🍽️
      </div>
    )}
  </div>

  <strong>{food.name}</strong>

  <span>
    {food.serving_size} {food.serving_unit}
  </span>
</div>

        <div>
          <strong>{food.name}</strong>

          <span>
            {food.serving_size} {food.serving_unit}
          </span>
        </div>

        <span>{food.calories} kcal</span>
      </button>
    ))}
  </div>
)}

          {selectedFood && (() => {
  const quantityMultiplier =
    Number(quantity || 0) /
    Number(selectedFood.serving_size || 100);

  const calculatedNutrition = {
    calories:
      Number(selectedFood.calories || 0) *
      quantityMultiplier,

    protein:
      Number(selectedFood.protein || 0) *
      quantityMultiplier,

    carbohydrates:
      Number(selectedFood.carbohydrates || 0) *
      quantityMultiplier,

    fat:
      Number(selectedFood.fat || 0) *
      quantityMultiplier,

    sugar:
      Number(selectedFood.sugar || 0) *
      quantityMultiplier,

    fiber:
      Number(selectedFood.fiber || 0) *
      quantityMultiplier,
  };

  const goalFit = getGoalFit(calculatedNutrition);

  return (
    <div className="selected-food-box">
      <div className="selected-food-header">

  <div className="selected-food-main">

    <div className="selected-food-image">
      {getFoodImage(selectedFood.name) ? (
        <img
          src={getFoodImage(selectedFood.name)}
          alt={selectedFood.name}
        />
      ) : (
        <div className="selected-food-image-placeholder">
          🍽️
        </div>
      )}
    </div>

    <div className="selected-food-details">
      <p className="suggestion-label">SELECTED FOOD</p>

      <h3>{selectedFood.name}</h3>

      <div className="selected-food-serving">
        {quantity} {selectedFood.serving_unit || "g"}
      </div>

      <div className="selected-food-calories">
        {calculatedNutrition.calories.toFixed(1)} kcal
      </div>
    </div>

  </div>

  <div className="selected-food-ai">

    {aiResult && (
      <div className="ai-confidence-info">

        <small>
          AI confidence: {(aiResult.confidence * 100).toFixed(2)}%
        </small>

        {aiResult.requires_confirmation && (
          <>
            <small className="ai-uncertain-warning">
              ⚠️ AI detected <strong>{selectedFood?.name}</strong>, but confidence is low.
              Please verify the food before adding it.
            </small>

            {aiResult.predictions?.length > 1 && (
              <div className="ai-alternative-predictions">

                <small className="suggestion-label">
                  OTHER AI PREDICTIONS
                </small>

                <div className="ai-prediction-list">
                  {aiResult.predictions.slice(1, 4).map((prediction, index) => (
                    <button
                      type="button"
                      key={index}
                      className="ai-prediction-item"
                      onClick={async () => {
                        try {
                          const token = localStorage.getItem("access_token");

                          const response = await fetch(
                            `${API_URL}/foods/search?name=${encodeURIComponent(
                              prediction.food
                            )}`,
                            {
                              headers: {
                                Authorization: `Bearer ${token}`,
                              },
                            }
                          );

                          if (!response.ok) {
                            throw new Error("Food search failed");
                          }

                          const data = await response.json();

                          if (data.length > 0) {
                            const food = data[0];

                            setSelectedFood(food);
                            setDescription(food.name);
                            setQuantity(food.serving_size || 100);

                            const recommendation =
                              await getHealthierRecommendation(food);

                            setHealthierFood(recommendation);

                            setAiResult({
                              ...aiResult,
                              userSelectedAlternative: true,
                            });
                          }
                        } catch (error) {
                          console.error(
                            "Alternative food selection failed:",
                            error
                          );
                        }
                      }}
                    >
                      {prediction.food} ·{" "}
                      {(prediction.confidence * 100).toFixed(2)}%
                    </button>
                  ))}
                </div>
              </div>
            )}

            {aiAlternativeSelected && (
              <small className="ai-assisted-status">
                AI-assisted selection • Please verify before adding
              </small>
            )}

            <button
              type="button"
              className="ai-change-food-button"
              onClick={() => {
                setSelectedFood(null);
                setAiResult({
                  ...aiResult,
                  userSelectedAlternative: true,
                });
                setHealthierFood(null);
                setAiAlternativeSelected(false);
                setDescription("");
              }}
            >
              Choose another food
            </button>
          </>
        )}

      </div>
    )}

  </div>

</div> 

    <div className="selected-food-nutrition">

      <div>
        <strong>{calculatedNutrition.calories.toFixed(1)}</strong>
        <span>Calories</span>
      </div>

      <div>
        <strong>{calculatedNutrition.protein.toFixed(1)}g</strong>
        <span>Protein</span>
      </div>

      <div>
        <strong>{calculatedNutrition.carbohydrates.toFixed(1)}g</strong>
        <span>Carbs</span>
      </div>

      <div>
        <strong>{calculatedNutrition.fat.toFixed(1)}g</strong>
        <span>Fat</span>
      </div>

      <div>
        <strong>{calculatedNutrition.sugar.toFixed(1)}g</strong>
        <span>Sugar</span>
      </div>

      <div>
        <strong>{calculatedNutrition.fiber.toFixed(1)}g</strong>
        <span>Fiber</span>
      </div>

    </div>
    {goalFit && (
  <div className="goal-fit-box">
    <div>
      <p className="suggestion-label">GOAL FIT</p>
      <h4>{goalFit.status}</h4>
    </div>

    <p>{goalFit.message}</p>
  </div>
)}

  {healthierFood && (
  <div className="goal-fit-box">
    <div>
      <p className="suggestion-label">HEALTHIER ALTERNATIVE</p>
      <h4>{healthierFood.name}</h4>
    </div>

    <p>
      {healthierFood.calories} kcal ·{" "}
      {healthierFood.protein}g protein ·{" "}
      {healthierFood.fiber}g fiber
    </p>
  </div>
)}

  <div className="food-log-options">

  <div className="food-log-field">
    <label className="label">Quantity</label>

    <div className="quantity-input-wrapper">
      <input
        type="number"
        min="1"
        value={quantity}
        onChange={(event) => setQuantity(event.target.value)}
      />

      <span className="quantity-unit">
        {selectedFood.serving_unit || "g"}
      </span>
    </div>
  </div>

  <div className="food-log-field">
    <label className="label">Meal</label>

    <select
      value={mealType}
      onChange={(event) => setMealType(event.target.value)}
    >
      <option value="Breakfast">Breakfast</option>
      <option value="Lunch">Lunch</option>
      <option value="Dinner">Dinner</option>
      <option value="Snack">Snack</option>
    </select>
  </div>

</div>
      </div>
  );
})()}
          <p className="suggestion-label">TRY A SUGGESTION</p>

          <div className="suggestion-chips">
            <button
              className="suggestion-chip"
              onClick={() => setDescription("Avocado toast")}
            >
              Avocado toast
            </button>

            <button
              className="suggestion-chip"
              onClick={() => setDescription("Greek yogurt bowl")}
            >
              Greek yogurt bowl
            </button>
          </div>

          <button
  className="btn-primary continue-button"
  disabled={!selectedFood}
  onClick={async () => {
  if (!selectedFood) {
    return;
    }

    if (aiResult?.requires_confirmation) {
      const confirmed = window.confirm(
        `AI is not fully confident that this is ${selectedFood.name}.\n\nDo you want to add it anyway?`
      );

      if (!confirmed) {
        return;
      }
    }

    const token = localStorage.getItem("access_token");

    try {
      const response = await fetch(
        `${API_URL}/food-history/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify({
            food_id: selectedFood.id,
            quantity: Number(quantity),
            meal_type: mealType,
          }),
        }
      );

      if (!response.ok) {
        throw new Error("Failed to add food");
      }

      const savedFood = await response.json();

      console.log("Food added successfully:", savedFood);

      alert(`${selectedFood.name} added to today's food!`);

      onFoodAdded();

      setSelectedFood(null);
      setDescription("");
      setQuantity(100);
      setMealType("Breakfast");
    } catch (error) {
      console.error("Add food failed:", error);
      alert("Could not add food. Please try again.");
    }
  }}
>
  Add to today's food
  <ArrowRight size={17} />
</button>

          <div className="privacy-note">
            <ShieldCheck size={16} />

            <span>
              Your food photos stay private and are only used to help
              analyze your meal.
            </span>
          </div>
        </div>
      </section>
    </main>
  );
}

function ExploreFoodsPage({ onBack, profile }) {
  const [foods, setFoods] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("All");
  const [selectedFood, setSelectedFood] = useState(null);
  

  useEffect(() => {
    const loadFoods = async () => {
      try {
        const response = await fetch(`${API_URL}/foods/`);

        if (!response.ok) {
          throw new Error("Failed to load foods");
        }

        const data = await response.json();
        setFoods(data);
      } catch (error) {
        console.error("Explore foods failed:", error);
      } finally {
        setLoading(false);
      }
    };

    loadFoods();
  }, []);
  return (
    <main className="page-content explore-page">
      <button
        type="button"
        className="explore-back-button"
        onClick={onBack}
      >
        ← Back to Analyze Food
      </button>

      <div className="explore-page-header">
        <p className="eyebrow">FOOD DISCOVERY</p>

        <h2>Explore Foods</h2>

        <p>
          Discover foods and understand their nutrition.
        </p>
      </div>

      <div className="explore-page-search">
        <Search size={18} />

        <input
          type="text"
          value={searchTerm}
          onChange={(event) => setSearchTerm(event.target.value)}
          placeholder="Search for a food..."
        />
      </div>

      <div className="explore-page-categories">
        {["All", "Indian", "Fruits", "Vegetables", "Snacks", "Meals"].map(
          (category) => (
            <button
              key={category}
              type="button"
              className={selectedCategory === category ? "active" : ""}
              onClick={() => setSelectedCategory(category)}
            >
              {category}
            </button>
          )
        )}
      </div>

      <div className="explore-section-heading">
        <div>
          <p className="suggestion-label">FOOD COLLECTION</p>
          <h3>All Foods</h3>
        </div>
      </div>

      {selectedFood && (
  <div className="explore-food-details">
    <div className="explore-food-details-header">
      <div>
        <p className="suggestion-label">FOOD DETAILS</p>
        <h3>{selectedFood.name}</h3>
        <span>
          {selectedFood.serving_size} {selectedFood.serving_unit}
        </span>
      </div>

      <button
        type="button"
        onClick={() => setSelectedFood(null)}
      >
        Close
      </button>
    </div>

    <div className="explore-nutrition-grid">
      <div>
        <strong>{selectedFood.calories}</strong>
        <span>Calories</span>
      </div>

      <div>
        <strong>{selectedFood.protein}g</strong>
        <span>Protein</span>
      </div>

      <div>
        <strong>{selectedFood.carbohydrates}g</strong>
        <span>Carbs</span>
      </div>

      <div>
        <strong>{selectedFood.fat}g</strong>
        <span>Fat</span>
      </div>

      <div>
        <strong>{selectedFood.sugar}g</strong>
        <span>Sugar</span>
      </div>

      <div>
        <strong>{selectedFood.fiber}g</strong>
        <span>Fiber</span>
      </div>
    </div>
  </div>
)}

      {loading ? (
  <p className="suggestion-label">LOADING FOODS...</p>
) : (

<div className="explore-food-grid">
  {foods
    .filter((food) => {
      const matchesSearch = food.name
        .toLowerCase()
        .includes(searchTerm.toLowerCase());

      const matchesCategory =
        selectedCategory === "All" ||
        food.category?.toLowerCase() === selectedCategory.toLowerCase();

      return matchesSearch && matchesCategory;
    })
    .map((food) => (
      <button
        key={food.id}
        type="button"
        className="explore-food-card"
        onClick={() => setSelectedFood(food)}
      >
        {getFoodImage(food.name) && (
          <img
            src={getFoodImage(food.name)}
            alt={food.name}
            className="explore-food-image"
          />
        )}

        <div>
          <strong>{food.name}</strong>

          <span>
            {food.serving_size} {food.serving_unit}
          </span>
        </div>

                <span>{food.calories} kcal</span>
      </button>
    ))}
  </div>
)}
    </main>
  );
}

function FoodHistoryPage({ foodHistory }) {
  const [historyRange, setHistoryRange] = useState("This week");
  const [mealFilter, setMealFilter] = useState("All meals");
  const getDateLabel = (dateString) => {
    if (!dateString) {
      return {
        main: "",
        sub: "",
      };
    }

    const date = new Date(dateString);
    const today = new Date();

    const todayStart = new Date(
      today.getFullYear(),
      today.getMonth(),
      today.getDate()
    );

    const dateStart = new Date(
      date.getFullYear(),
      date.getMonth(),
      date.getDate()
    );

    const differenceInDays = Math.round(
      (todayStart - dateStart) / (1000 * 60 * 60 * 24)
    );

    if (differenceInDays === 0) {
      return {
        main: "Today",
        sub: date.toLocaleDateString("en-US", {
          weekday: "long",
          month: "short",
          day: "numeric",
        }),
      };
    }

    if (differenceInDays === 1) {
      return {
        main: "Yesterday",
        sub: date.toLocaleDateString("en-US", {
          weekday: "long",
          month: "short",
          day: "numeric",
        }),
      };
    }

    return {
      main: date.toLocaleDateString("en-US", {
        weekday: "long",
      }),
      sub: date.toLocaleDateString("en-US", {
        month: "long",
        day: "numeric",
      }),
    };
  };

  // Dynamic count of all valid food-history records
  const mealsAnalyzed = (foodHistory || []).filter(
    (item) => item.consumed_at
  ).length;

  // Valid food history records
  const validFoodHistory = (foodHistory || []).filter(
  (item) => {
    if (!item.consumed_at) {
      return false;
    }

    if (historyRange === "All time") {
      return true;
    }

    const itemDate = new Date(item.consumed_at);
    const today = new Date();

    const currentDay = today.getDay();

    const mondayOffset =
      currentDay === 0 ? -6 : 1 - currentDay;

    const startOfCurrentWeek = new Date(today);

    startOfCurrentWeek.setDate(
      today.getDate() + mondayOffset
    );

    startOfCurrentWeek.setHours(
      0,
      0,
      0,
      0
    );

    return itemDate >= startOfCurrentWeek;
  }
);

  // Total calories from all historical records
  const totalHistoricalCalories = validFoodHistory.reduce(
    (total, item) => total + (item.calories || 0),
    0
  );

  // Number of unique days with logged food
  const uniqueDays = new Set(
    validFoodHistory.map((item) =>
      new Date(item.consumed_at).toDateString()
    )
  ).size;

  // Average calories per logged day
  const averageDailyCalories =
    uniqueDays > 0
      ? Math.round(totalHistoricalCalories / uniqueDays)
      : 0;

  // Create YYYY-MM-DD date key
  const getDayKey = (date) => {
    const day = new Date(date);

    return `${day.getFullYear()}-${String(
      day.getMonth() + 1
    ).padStart(2, "0")}-${String(day.getDate()).padStart(2, "0")}`;
  };

  // Get Monday of current week
  const today = new Date();

  const startOfWeek = new Date(today);
  const currentDay = startOfWeek.getDay();

  const mondayOffset =
    currentDay === 0 ? -6 : 1 - currentDay;

  startOfWeek.setDate(
    startOfWeek.getDate() + mondayOffset
  );

  startOfWeek.setHours(0, 0, 0, 0);

  // Store calories for each day of current week
  const weeklyCalories = {};

  for (let i = 0; i < 7; i++) {
    const date = new Date(startOfWeek);

    date.setDate(
      startOfWeek.getDate() + i
    );

    weeklyCalories[getDayKey(date)] = 0;
  }

  // Add food calories to the correct day
  validFoodHistory.forEach((item) => {
    const itemDate = new Date(item.consumed_at);

    const dayKey = getDayKey(itemDate);

    if (weeklyCalories[dayKey] !== undefined) {
      weeklyCalories[dayKey] += item.calories || 0;
    }
  });

  // Weekly calorie values
  const weeklyCalorieValues = Object.values(weeklyCalories);

  // Highest calorie value of the current week
  const maxWeeklyCalories = Math.max(
    ...weeklyCalorieValues,
    1
  );

  // Convert each day's calories into a bar height
  const getWeeklyBarHeight = (dayIndex) => {
    const date = new Date(startOfWeek);

    date.setDate(
      startOfWeek.getDate() + dayIndex
    );

    const dayKey = getDayKey(date);
    const calories = weeklyCalories[dayKey] || 0;

    // Show a very small bar when no food was logged
    if (calories === 0) {
      return "4%";
    }

    const percentage =
      (calories / maxWeeklyCalories) * 100;

    return `${Math.max(percentage, 8)}%`;
  };

  // --------------------------------------------------
  // Step 20 - Part 1
  // Calculate weekly consistency
  // --------------------------------------------------

  const loggedWeeklyCalories = Object.values(
    weeklyCalories
  ).filter((calories) => calories > 0);

  let weeklyInsightTitle = "Start logging your meals";
  let weeklyInsightText =
    "Add your meals throughout the week to see your nutrition pattern here.";

  if (loggedWeeklyCalories.length > 0) {
    const weeklyAverage =
      loggedWeeklyCalories.reduce(
        (total, calories) => total + calories,
        0
      ) / loggedWeeklyCalories.length;

    const highestDay = Math.max(
      ...loggedWeeklyCalories
    );

    const lowestDay = Math.min(
      ...loggedWeeklyCalories
    );

    const variation =
      weeklyAverage > 0
        ? (highestDay - lowestDay) / weeklyAverage
        : 0;

    if (loggedWeeklyCalories.length < 3) {
      weeklyInsightTitle = "You're building a rhythm";
      weeklyInsightText =
        "Keep logging your meals to build a clearer picture of your weekly nutrition.";
    } else if (variation <= 0.5) {
      weeklyInsightTitle = "A steady week";
      weeklyInsightText =
        "Your meals have stayed fairly consistent. That's a useful pattern worth keeping.";
    } else {
      weeklyInsightTitle = "A varied week";
      weeklyInsightText =
        "Your daily calories have varied this week. Look for patterns that help you stay on track.";
    }
  }

  // Average calorie target used for history message
  const historyCalorieTarget = 2125;

  const calorieRangeMessage =
    averageDailyCalories === 0
      ? "No calorie data yet"
      : averageDailyCalories < historyCalorieTarget * 0.9
      ? "Below your target"
      : averageDailyCalories > historyCalorieTarget * 1.1
      ? "Above your target"
      : "Within your target range";

  // Dates on which food was logged
  const loggedDates = new Set(
    validFoodHistory.map((item) =>
      new Date(item.consumed_at).toDateString()
    )
  );

  // Calculate current consecutive-day momentum
  let momentumDays = 0;
  const momentumDate = new Date();

  while (true) {
    const dateKey = momentumDate.toDateString();

    if (!loggedDates.has(dateKey)) {
      break;
    }

    momentumDays += 1;

    momentumDate.setDate(
      momentumDate.getDate() - 1
    );
  }

  return (
    <main className="page-content history-page">
      <div className="history-intro">
        <div>
          <p className="eyebrow">
            YOUR PATTERNS, NOT YOUR PERFECTION
          </p>

          <h2>Food history</h2>

          <p className="intro-text">
            Look back at what you've eaten and notice the patterns that
            matter to you.
          </p>
        </div>

        <div className="history-controls">
          <button
  className="history-control"
  onClick={() =>
    setHistoryRange(
      historyRange === "This week"
        ? "All time"
        : "This week"
    )
  }
>
  <CalendarDays size={16} />
  {historyRange}
  <ChevronDown size={15} />
</button>

          <button
  className="history-control"
  onClick={() =>
    setMealFilter(
      mealFilter === "All meals"
        ? "Breakfast"
        : mealFilter === "Breakfast"
        ? "Lunch"
        : mealFilter === "Lunch"
        ? "Dinner"
        : mealFilter === "Dinner"
        ? "Snack"
        : "All meals"
    )
  }
>
  <Filter size={16} />
  {mealFilter}
</button>
        </div>
      </div>

      <section className="history-summary-grid">
        <div className="card history-summary-card">
          <div className="history-summary-icon green">
            <ScanLine size={19} />
          </div>

          <div>
            <span>Meals analyzed</span>
            <strong>{mealsAnalyzed}</strong>
            <small>This week</small>
          </div>
        </div>

        <div className="card history-summary-card">
          <div className="history-summary-icon orange">
            <Utensils size={19} />
          </div>

          <div>
            <span>Average daily calories</span>
            <strong>{averageDailyCalories}</strong>
            <small>{calorieRangeMessage}</small>
          </div>
        </div>

        <div className="card history-summary-card">
          <div className="history-summary-icon purple">
            <TrendingUp size={19} />
          </div>

          <div>
            <span>Your momentum</span>

            <strong>
              {momentumDays}{" "}
              {momentumDays === 1 ? "day" : "days"}
            </strong>

            <small>You've been consistent</small>
          </div>
        </div>
      </section>

      <div className="history-main-grid">
        <section>
          <div className="section-heading">
            <div>
              <p className="eyebrow">RECENT SCANS</p>
              <h3>What you've enjoyed</h3>
            </div>

            <button className="text-button">
              View all
            </button>
          </div>

          <div className="card recent-scans-card">
            {foodHistory && foodHistory.length > 0 ? (
              (() => {
                const validHistory = foodHistory
  .filter((item) => {
    if (!item.consumed_at) {
      return false;
    }

    if (historyRange === "All time") {
      return true;
    }

    const itemDate = new Date(item.consumed_at);
    const today = new Date();

    const currentDay = today.getDay();

    const mondayOffset =
      currentDay === 0 ? -6 : 1 - currentDay;

    const startOfCurrentWeek = new Date(today);

    startOfCurrentWeek.setDate(
      today.getDate() + mondayOffset
    );

    startOfCurrentWeek.setHours(
      0,
      0,
      0,
      0
    );

    return itemDate >= startOfCurrentWeek;
  })
  .sort(
    (a, b) =>
      new Date(b.consumed_at) -
      new Date(a.consumed_at)
  );

                if (validHistory.length === 0) {
                  return (
                    <div className="history-empty-state">
                      <p>No food has been logged yet.</p>

                      <span>
                        Start adding your meals from Analyze Food.
                      </span>
                    </div>
                  );
                }

                const groupedHistory = validHistory.reduce(
                  (groups, item) => {
                    const dateKey = new Date(
                      item.consumed_at
                    ).toDateString();

                    if (!groups[dateKey]) {
                      groups[dateKey] = [];
                    }

                    groups[dateKey].push(item);

                    return groups;
                  },
                  {}
                );

                return Object.entries(groupedHistory).map(
                  ([dateKey, items]) => {
                    const dateLabel = getDateLabel(
                      items[0].consumed_at
                    );

                    return (
                      <div
                        key={dateKey}
                        className="history-date-group"
                      >
                        <div className="history-date-heading">
                          <strong>{dateLabel.main}</strong>

                          <span>{dateLabel.sub}</span>
                        </div>

                        {items.map((item) => (
                          <HistoryMealRow
                            key={item.id}
                            icon={
                              item.meal_type === "Breakfast"
                                ? "breakfast"
                                : item.meal_type === "Lunch"
                                ? "lunch"
                                : item.meal_type === "Dinner"
                                ? "dinner"
                                : "breakfast"
                            }
                            title={item.food_name || "Food"}
                            meal={item.meal_type || "Meal"}
                            calories={`${Math.round(
                              item.calories || 0
                            )} kcal`}
                            time={new Date(
                              item.consumed_at
                            ).toLocaleTimeString([], {
                              hour: "numeric",
                              minute: "2-digit",
                            })}
                            status="Logged"
                          />
                        ))}
                      </div>
                    );
                  }
                );
              })()
            ) : (
              <div className="history-empty-state">
                <p>No food has been logged yet.</p>

                <span>
                  Start adding your meals from Analyze Food.
                </span>
              </div>
            )}
          </div>
        </section>

        <section>
          <div className="section-heading">
            <div>
              <p className="eyebrow">THIS WEEK</p>
              <h3>Week at a glance</h3>
            </div>
          </div>

          <div className="card week-chart-card">
            <div className="week-chart">
              <div className="chart-grid-line line-one"></div>
              <div className="chart-grid-line line-two"></div>
              <div className="chart-grid-line line-three"></div>

              <WeekBar
                day="M"
                height={getWeeklyBarHeight(0)}
              />

              <WeekBar
                day="T"
                height={getWeeklyBarHeight(1)}
              />

              <WeekBar
                day="W"
                height={getWeeklyBarHeight(2)}
              />

              <WeekBar
                day="T"
                height={getWeeklyBarHeight(3)}
              />

              <WeekBar
                day="F"
                height={getWeeklyBarHeight(4)}
              />

              <WeekBar
                day="S"
                height={getWeeklyBarHeight(5)}
              />

              <WeekBar
                day="S"
                height={getWeeklyBarHeight(6)}
                active
              />
            </div>

            <div className="chart-legend">
              <span>
                <i></i>
                Daily calories
              </span>

              <strong>
                {averageDailyCalories > 0
                  ? `${averageDailyCalories.toLocaleString()} avg.`
                  : "No data"}
              </strong>
            </div>

            <div className="history-insight">
              <div className="history-insight-icon">
                <Sparkles size={17} />
              </div>

              <div>
                <strong>{weeklyInsightTitle}</strong>

                <p>{weeklyInsightText}</p>
              </div>
            </div>
          </div>
        </section>
      </div>
    </main>
  );
}

function HistoryMealRow({
  icon,
  title,
  meal,
  calories,
  time,
  status,
}) {
  return (
    <div className="history-meal-row">
      <div className={`history-meal-icon ${icon}`}>
        <Utensils size={17} />
      </div>

      <div className="history-meal-info">
        <strong>{title}</strong>

        <span>
          {meal} · {time}
        </span>
      </div>

      <div className="history-meal-right">
        <strong>{calories}</strong>
        <span>{status}</span>
      </div>
    </div>
  );
}


function WeekBar({ day, height, active = false }) {
  return (
    <div className="week-bar-column">
      <div className="week-bar-area">
        <div
          className={`week-bar ${active ? "active" : ""}`}
          style={{ height }}
        ></div>
      </div>

      <span>{day}</span>
    </div>
  );
}


function ProfileGoalsPage({ profile, onProfileUpdated }) {
  const [goal, setGoal] = useState("Weight Loss");
  const [goalData, setGoalData] = useState(null);

  const [isEditingProfile, setIsEditingProfile] = useState(false);

  const [editProfile, setEditProfile] = useState({
    name: "",
    age: "",
    height: "",
    weight: "",
    gender: "",
    activity_level: "",
    food_preference: "",
  });
    const saveProfile = async () => {
    try {
      const token = localStorage.getItem("access_token");

      const userResponse = await fetch(
        `${API_URL}/auth/me`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      if (!userResponse.ok) {
        throw new Error("Failed to get current user");
      }

      const user = await userResponse.json();

      const response = await fetch(
        `${API_URL}/users/${user.id}/profile`,
        {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify({
            age: Number(editProfile.age),
            height: Number(editProfile.height),
            weight: Number(editProfile.weight),
            activity_level: editProfile.activity_level,
            goal: profile?.goal || "weight_loss",
            food_preference: editProfile.food_preference,
            gender: editProfile.gender,
          }),
        }
      );

      if (!response.ok) {
        const errorData = await response.json();

        throw new Error(
          errorData.detail || "Failed to update profile"
        );
      }

      console.log("Profile updated successfully");

await onProfileUpdated();

const goalResponse = await fetch(
  `${API_URL}/goals/`,
  {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  }
);

if (goalResponse.ok) {
  const updatedGoalData = await goalResponse.json();

  const calorieResponse = await fetch(
    `${API_URL}/goals/calorie-calculation`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  const proteinResponse = await fetch(
    `${API_URL}/goals/protein-calculation`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  const calorieData = calorieResponse.ok
    ? await calorieResponse.json()
    : null;

  const proteinData = proteinResponse.ok
    ? await proteinResponse.json()
    : null;

  setGoalData({
    ...updatedGoalData,
    calorie_calculation: calorieData,
    protein_calculation: proteinData,
  });
}

setIsEditingProfile(false);

    } catch (error) {
      console.error("Profile update failed:", error);
    }
  };
  const updateGoal = async (selectedGoal) => {
  try {
    const token = localStorage.getItem("access_token");

    const userResponse = await fetch(
      `${API_URL}/auth/me`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    if (!userResponse.ok) {
      throw new Error("Failed to get current user");
    }

    const user = await userResponse.json();

    const profileResponse = await fetch(
      `${API_URL}/users/${user.id}/profile`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    if (!profileResponse.ok) {
      throw new Error("Failed to fetch profile");
    }

    const profileData = await profileResponse.json();

    let backendGoal = "";

    if (selectedGoal === "Weight Loss") {
      backendGoal = "weight_loss";
    } else if (selectedGoal === "Maintain Weight") {
      backendGoal = "maintenance";
    } else if (selectedGoal === "Build Muscle") {
      backendGoal = "weight_gain";
    }

    const updateResponse = await fetch(
      `${API_URL}/users/${user.id}/profile`,
      {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          age: profileData.age,
          height: profileData.height,
          weight: profileData.weight,
          activity_level: profileData.activity_level,
          calorie_target: profileData.calorie_target,
          goal: backendGoal,
          food_preference: profileData.food_preference,
          gender: profileData.gender,
        }),
      }
    );

    if (!updateResponse.ok) {
      const errorData = await updateResponse.json();
      throw new Error(
        errorData.detail || "Failed to update goal"
      );
    }

    setGoal(selectedGoal);

// Refresh goal data after updating the backend
const goalResponse = await fetch(
  `${API_URL}/goals/`,
  {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  }
);

if (goalResponse.ok) {
  const updatedGoalData = await goalResponse.json();

  const calorieResponse = await fetch(
    `${API_URL}/goals/calorie-calculation`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  let calorieData = null;

  if (calorieResponse.ok) {
    calorieData = await calorieResponse.json();
  }

  const proteinResponse = await fetch(
    `${API_URL}/goals/protein-calculation`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  let proteinData = null;

  if (proteinResponse.ok) {
    proteinData = await proteinResponse.json();
  }

  setGoalData({
    ...updatedGoalData,
    calorie_calculation: calorieData,
    protein_calculation: proteinData,
  });
}

console.log("Goal updated successfully:", backendGoal);


  } catch (error) {
    console.error("Error updating goal:", error);
  }
};


  useEffect(() => {
    const fetchGoal = async () => {
      try {
        const token = localStorage.getItem("access_token");

        const response = await fetch(`${API_URL}/goals/`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (!response.ok) {
          throw new Error("Failed to fetch goal");
        }

        const data = await response.json();

        setGoalData(data);
        const calorieResponse = await fetch(
  `${API_URL}/goals/calorie-calculation`,
  {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  }
);

if (calorieResponse.ok) {
  const calorieData = await calorieResponse.json();

  setGoalData((previous) => ({
    ...previous,
    calorie_calculation: calorieData,
  }));
}

const proteinResponse = await fetch(
  `${API_URL}/goals/protein-calculation`,
  {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  }
);

if (proteinResponse.ok) {
  const proteinData = await proteinResponse.json();

  setGoalData((previous) => ({
    ...previous,
    protein_calculation: proteinData,
  }));
}

        if (data.goal_type === "weight_loss") {
          setGoal("Weight Loss");
        } else if (data.goal_type === "maintenance") {
          setGoal("Maintain Weight");
        } else if (data.goal_type === "weight_gain") {
          setGoal("Build Muscle");
        }

      } catch (error) {
        console.error("Error fetching goal:", error);
      }
    };

    fetchGoal();
  }, []);


  if (isEditingProfile) {
  return (
    <main className="page-content profile-page">

      <div className="profile-intro">
        <div>
          <p className="eyebrow">YOUR PROFILE</p>

          <h2>Edit profile</h2>

          <p className="intro-text">
            Keep your personal details up to date so NutriWise
            can personalize your nutrition plan.
          </p>
        </div>

        <button
          className="btn-secondary"
          onClick={() => setIsEditingProfile(false)}
        >
          Cancel
        </button>
      </div>

      <section className="card profile-edit-card">

        <div className="profile-edit-grid">

          <div className="profile-field">
            <label>Name</label>

            <input
              type="text"
              value={editProfile.name}
              onChange={(e) =>
                setEditProfile({
                  ...editProfile,
                  name: e.target.value,
                })
              }
            />
          </div>

          <div className="profile-field">
            <label>Age</label>

            <input
              type="number"
              value={editProfile.age}
              onChange={(e) =>
                setEditProfile({
                  ...editProfile,
                  age: e.target.value,
                })
              }
            />
          </div>

          <div className="profile-field">
            <label>Height (cm)</label>

            <input
              type="number"
              value={editProfile.height}
              onChange={(e) =>
                setEditProfile({
                  ...editProfile,
                  height: e.target.value,
                })
              }
            />
          </div>

          <div className="profile-field">
            <label>Weight (kg)</label>

            <input
              type="number"
              value={editProfile.weight}
              onChange={(e) =>
                setEditProfile({
                  ...editProfile,
                  weight: e.target.value,
                })
              }
            />
          </div>

          <div className="profile-field">
            <label>Gender</label>

            <select
              value={editProfile.gender}
              onChange={(e) =>
                setEditProfile({
                  ...editProfile,
                  gender: e.target.value,
                })
              }
            >
              <option value="">Select gender</option>
              <option value="male">Male</option>
              <option value="female">Female</option>
              <option value="other">Other</option>
            </select>
          </div>

          <div className="profile-field">
            <label>Activity level</label>

            <select
              value={editProfile.activity_level}
              onChange={(e) =>
                setEditProfile({
                  ...editProfile,
                  activity_level: e.target.value,
                })
              }
            >
              <option value="">Select activity level</option>
              <option value="sedentary">Sedentary</option>
              <option value="light">Light</option>
              <option value="moderate">Moderate</option>
              <option value="active">Active</option>
              <option value="very_active">Very Active</option>
            </select>
          </div>

          <div className="profile-field">
            <label>Food preference</label>

            <select
              value={editProfile.food_preference}
              onChange={(e) =>
                setEditProfile({
                  ...editProfile,
                  food_preference: e.target.value,
                })
              }
            >
              <option value="">Select preference</option>
              <option value="vegetarian">Vegetarian</option>
              <option value="non_vegetarian">Non-Vegetarian</option>
              <option value="vegan">Vegan</option>
              <option value="eggetarian">Eggetarian</option>
            </select>
          </div>

        </div>

        <div className="profile-edit-actions">

          <button
            className="btn-secondary"
            onClick={() => setIsEditingProfile(false)}
          >
            Cancel
          </button>

          <button
            className="btn-primary"
            onClick={saveProfile}
          >
            Save Changes
          </button>

        </div>

      </section>

    </main>
  );
}

  return (
    <main className="page-content profile-page">

      <div className="profile-intro">
        <div>
          <p className="eyebrow">YOUR PERSONAL PLAN</p>

          <h2>Profile & goals</h2>

          <p className="intro-text">
            Your plan is built around you. Update your details anytime
            as your needs change.
          </p>
        </div>

        <button
  className="btn-secondary"
  onClick={() => {
    setEditProfile({
      name: profile?.name || "",
      age: profile?.age || "",
      height: profile?.height || "",
      weight: profile?.weight || "",
      gender: profile?.gender || "",
      activity_level: profile?.activity_level || "",
      food_preference: profile?.food_preference || "",
    });

    setIsEditingProfile(true);
  }}
>
  <Pencil size={16} />
  Edit profile
</button>
      </div>


      <div className="profile-main-grid">

        <section className="card profile-card">

          <div className="profile-card-header">
            <div className="profile-avatar-large">
              M
            </div>

            <div>
              <p className="eyebrow">YOUR PROFILE</p>
              <h3>{profile?.name || "Your profile"}</h3>
              <span>Wellness journey</span>
            </div>
          </div>


          <div className="profile-details">

            <ProfileDetail
              icon={<UserRound size={17} />}
              label="Age"
              value={profile?.age ? `${profile.age} years` : "Not set"}
            />

            <ProfileDetail
              icon={<Ruler size={17} />}
              label="Height"
              value={profile?.height ? `${profile.height} cm` : "Not set"}
            />

            <ProfileDetail
              icon={<Weight size={17} />}
              label="Weight"
              value={profile?.weight ? `${profile.weight} kg` : "Not set"}
            />

            <ProfileDetail
              icon={<Activity size={17} />}
              label="Activity level"
              value={profile?.activity_level || "Not set"}
            />

            <ProfileDetail
              icon={<Apple size={17} />}
              label="Food preference"
              value={profile?.food_preference || "Not set"}
            />

            <ProfileDetail
              icon={<CircleUserRound size={17} />}
              label="Gender"
              value={profile?.gender || "Not set"}
            />

          </div>


          <div className="profile-note">
            <Sparkles size={16} />

            <span>
              Keeping these details up to date helps NutriWise make
              better recommendations for you.
            </span>
          </div>

        </section>


        <section>

          <div className="section-heading">
            <div>
              <p className="eyebrow">YOUR GOALS</p>
              <h3>What are you working toward?</h3>
            </div>
          </div>


          <div className="goal-options">

            <button
              className={`goal-option ${
                goal === "Weight Loss" ? "selected" : ""
              }`}
              onClick={() => updateGoal("Weight Loss")}
            >
              <div className="goal-option-icon">
                <TrendingUp size={19} />
              </div>

              <div>
                <strong>Weight Loss</strong>
                <span>A gentle calorie deficit</span>
              </div>

              {goal === "Weight Loss" && (
                <div className="goal-check">
                  <Check size={14} />
                </div>
              )}
            </button>


            <button
              className={`goal-option ${
                goal === "Maintain Weight" ? "selected" : ""
              }`}
              onClick={() => updateGoal("Maintain Weight")}
            >
              <div className="goal-option-icon">
                <Target size={19} />
              </div>

              <div>
                <strong>Maintain Weight</strong>
                <span>Stay around your current weight</span>
              </div>

              {goal === "Maintain Weight" && (
                <div className="goal-check">
                  <Check size={14} />
                </div>
              )}
            </button>


            <button
              className={`goal-option ${
                goal === "Build Muscle" ? "selected" : ""
              }`}
              onClick={() => updateGoal("Build Muscle")}
            >
              <div className="goal-option-icon">
                <Flame size={19} />
              </div>

              <div>
                <strong>Build Muscle</strong>
                <span>Support strength and muscle growth</span>
              </div>

              {goal === "Build Muscle" && (
                <div className="goal-check">
                  <Check size={14} />
                </div>
              )}
            </button>

          </div>


          <div className="card plan-card">

            <div className="plan-card-header">
              <div>
                <p className="eyebrow">YOUR CURRENT PLAN</p>
                <h3>{goal}</h3>
              </div>

              <div className="plan-badge">
                Personalized
              </div>
            </div>


            <div className="plan-stats">

              <div className="plan-stat">
                <span>Daily calories</span>
                <strong>
  {goalData?.calorie_calculation?.recommended_daily_calories
    ? Math.round(
        goalData.calorie_calculation.recommended_daily_calories
      )
    : "--"}{" "}
  <small>kcal</small>
</strong>
              </div>

              <div className="plan-stat">
                <span>Protein target</span>
                <strong>
                  {goalData?.protein_calculation?.recommended_daily_protein
                    ? Math.round(
                        goalData.protein_calculation.recommended_daily_protein
                      )
                    : "--"}{" "}
                  <small>g</small>
                </strong>
              </div>

              <div className="plan-stat">
              <span>Approach</span>
              <strong>
                {goalData?.approach
                  ? goalData.approach.charAt(0).toUpperCase() +
                    goalData.approach.slice(1)
                  : "--"}
              </strong>
            </div>

            </div>


            <div className="plan-message">
              <div className="plan-message-icon">
                <Sparkles size={17} />
              </div>

              <div>
                <strong>Progress, not perfection.</strong>

                <p>
                  Your targets are designed to give you direction,
                  not create pressure. Small consistent choices matter
                  more than perfect days.
                </p>
              </div>
            </div>


            <button className="plan-adjust-button">
              Adjust your plan
              <ArrowRight size={16} />
            </button>

          </div>

        </section>

      </div>

    </main>
  );
}

function PreferencesPage() {
  const [notifications, setNotifications] = useState(true);
  const [dailyReminders, setDailyReminders] = useState(true);
  const [unit, setUnit] = useState("Metric");
  const [saved, setSaved] = useState(false);
  
    useEffect(() => {
    const savedPreferences = localStorage.getItem(
      "nutriwise_preferences"
    );

    if (savedPreferences) {
      const preferences = JSON.parse(savedPreferences);

      setNotifications(preferences.notifications);
      setDailyReminders(preferences.dailyReminders);
      setUnit(preferences.unit);
    }
  }, []);

  return (
    <main className="page-content">
      <section className="page-intro">
        <p className="eyebrow">YOUR SETTINGS</p>
        <h2>Preferences</h2>
        <p>
          Customize how NutriWise works for you.
        </p>
      </section>

      <section className="card">
        <div className="section-heading">
          <div>
            <p className="eyebrow">NOTIFICATIONS</p>
            <h3>Stay updated</h3>
          </div>
        </div>

        <div className="preference-row">
          <div>
            <strong>Notifications</strong>
            <span>Receive NutriWise updates and alerts</span>
          </div>

          <button
            className={`toggle ${notifications ? "active" : ""}`}
            onClick={() => setNotifications(!notifications)}
          >
            <span></span>
          </button>
        </div>

        <div className="preference-row">
          <div>
            <strong>Daily reminders</strong>
            <span>Get reminders about your nutrition goals</span>
          </div>

          <button
            className={`toggle ${dailyReminders ? "active" : ""}`}
            onClick={() => setDailyReminders(!dailyReminders)}
          >
            <span></span>
          </button>
        </div>
      </section>

      <section className="card">
        <div className="section-heading">
          <div>
            <p className="eyebrow">DISPLAY</p>
            <h3>Units</h3>
          </div>
        </div>

        <div className="preference-row">
          <div>
            <strong>Measurement system</strong>
            <span>Choose how measurements are displayed</span>
          </div>

          <select
            value={unit}
            onChange={(e) => setUnit(e.target.value)}
          >
            <option>Metric</option>
            <option>Imperial</option>
          </select>
        </div>
      </section>

<section className="card preference-save-card">
  <div>
    <strong>Your preferences are saved locally</strong>
    <span>
      Your settings will stay saved even after you leave or refresh NutriWise.
    </span>
  </div>

        <button
  className="primary-button"
  onClick={() => {
  localStorage.setItem(
    "nutriwise_preferences",
    JSON.stringify({
      notifications,
      dailyReminders,
      unit,
    })
  );

  setSaved(true);

  setTimeout(() => {
    setSaved(false);
  }, 2500);
}}
>
  {saved ? "Preferences saved ✓" : "Save preferences"}
</button>
      </section>
    </main>
  );
}

function ProfileDetail({ icon, label, value }) {
  return (
    <div className="profile-detail">

      <div className="profile-detail-icon">
        {icon}
      </div>

      <div>
        <span>{label}</span>
        <strong>{value}</strong>
      </div>

    </div>
  );
}


function App() {
  const [currentPage, setCurrentPage] = useState("overview");
  const [explorePage, setExplorePage] = useState(false);
  const [authPage, setAuthPage] = useState("login");
  const [isLoggedIn, setIsLoggedIn] = useState(
    !!localStorage.getItem("access_token")
);
  const [showUserMenu, setShowUserMenu] = useState(false);
  const [showNotifications, setShowNotifications] = useState(false);
  const [hasUnreadNotifications, setHasUnreadNotifications] = useState(
  localStorage.getItem("nutriwise_notifications_read") !== "true"
);
  const [theme, setTheme] = useState(
  localStorage.getItem("nutriwise_theme") || "light"
);
  useEffect(() => {
  localStorage.setItem("nutriwise_theme", theme);
  document.body.className = theme === "dark" ? "dark-theme" : "";
}, [theme]);

  const [profile, setProfile] = useState(null);
  const [dailySummary, setDailySummary] = useState(null);
  const [foodHistory, setFoodHistory] = useState([]);
  const [goalData, setGoalData] = useState(null);

const fetchProfile = async () => {
  try {
    const token = localStorage.getItem("access_token");

    const userResponse = await fetch(
      `${API_URL}/auth/me`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    if (!userResponse.ok) {
      throw new Error("Failed to fetch current user");
    }

    const userData = await userResponse.json();

    console.log("Current user:", userData);

    const profileResponse = await fetch(
      `${API_URL}/users/${userData.id}/profile`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    if (!profileResponse.ok) {
      throw new Error("Failed to fetch profile");
    }

    const profileData = await profileResponse.json();

    console.log("Profile:", profileData);

    setProfile({
      ...profileData,
      name: userData.name,
      email: userData.email,
    });
  } catch (error) {
    console.error("Profile request failed:", error);
  }
};

useEffect(() => {
  if (!isLoggedIn) {
    return;
  }

  fetchProfile();

    // Fetch goal and nutrition targets
  const fetchGoalData = async () => {
    try {
      const token = localStorage.getItem("access_token");

      const goalResponse = await fetch(
        `${API_URL}/goals/`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      if (!goalResponse.ok) {
        throw new Error("Failed to fetch goal");
      }

      const goal = await goalResponse.json();

      const calorieResponse = await fetch(
        `${API_URL}/goals/calorie-calculation`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      const proteinResponse = await fetch(
        `${API_URL}/goals/protein-calculation`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      const calorieData = calorieResponse.ok
        ? await calorieResponse.json()
        : null;

      const proteinData = proteinResponse.ok
        ? await proteinResponse.json()
        : null;

      const combinedGoalData = {
        ...goal,
        calorie_calculation: calorieData,
        protein_calculation: proteinData,
      };

      console.log("Goal data:", combinedGoalData);

      setGoalData(combinedGoalData);
    } catch (error) {
      console.error("Goal data request failed:", error);
    }
  };

  fetchGoalData();


  // Fetch today's nutrition summary
  const token = localStorage.getItem("access_token");

  fetch(
    `${API_URL}/food-history/daily-summary`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  )
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to fetch daily nutrition");
      }

      return response.json();
    })
    .then((summaryData) => {
      console.log("Daily nutrition:", summaryData);
      setDailySummary(summaryData);
    })
    .catch((error) => {
      console.error(
        "Daily nutrition request failed:",
        error
      );
    });
}, [isLoggedIn]);

const refreshFoodData = async () => {
  const token = localStorage.getItem("access_token");

  try {
    const historyResponse = await fetch(
      `${API_URL}/food-history/`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    const historyData = await historyResponse.json();
    setFoodHistory(historyData);

    const summaryResponse = await fetch(
      `${API_URL}/food-history/daily-summary`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    const summaryData = await summaryResponse.json();
    setDailySummary(summaryData);

    console.log("Food data refreshed");
  } catch (error) {
    console.error("Food data refresh failed:", error);
  }
};
useEffect(() => {
  if (!isLoggedIn) {
    return;
  }

  const token = localStorage.getItem("access_token");

  fetch(
    `${API_URL}/food-history/`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  )
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to fetch food history");
      }

      return response.json();
    })
    .then((historyData) => {
      console.log("Food history:", historyData);
      setFoodHistory(historyData);
    })
    .catch((error) => {
      console.error(
        "Food history request failed:",
        error
      );
    });
}, [isLoggedIn]);

const handleLogin = async (credentials) => {
  try {
    const formData = new URLSearchParams();

    formData.append("username", credentials.username);
    formData.append("password", credentials.password);

    const response = await fetch(`${API_URL}/auth/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: formData,
    });

    const data = await response.json();

    console.log("Login response:", data);

    if (!response.ok) {
      console.error("Login failed:", data);
      return;
    }

    localStorage.setItem("access_token", data.access_token);

    console.log(
      "JWT saved successfully. Token length:",
      data.access_token?.length
    );

    // Get the currently logged-in user
    const userResponse = await fetch(`${API_URL}/auth/me`, {
      headers: {
        Authorization: `Bearer ${data.access_token}`,
      },
    });

    const userData = await userResponse.json();

    console.log("Logged-in user:", userData);

    if (!userResponse.ok) {
      console.error("Failed to get logged-in user:", userData);
      return;
    }

    // Store the logged-in user's ID
    localStorage.setItem("user_id", userData.id);

    setIsLoggedIn(true);
  } catch (error) {
    console.error("Login request failed:", error);
  }
};

  if (!isLoggedIn) {
  if (authPage === "create-account") {
    return (
      <CreateAccountPage
        onBackToLogin={() => setAuthPage("login")}
      />
    );
  }

  return (
    <LoginPage
      onLogin={handleLogin}
      onCreateAccount={() => setAuthPage("create-account")}
    />
  );
}

  return (
    <div className="app-shell">

      <aside className="sidebar">

        <div className="logo">
          <div className="logo-icon">
            <Leaf size={19} />
          </div>

          <span>NutriWise</span>
        </div>


        <div className="sidebar-section">

          <p className="sidebar-label">YOUR SPACE</p>

          <nav className="sidebar-nav">

            <button
              className={`nav-item ${
                currentPage === "overview" ? "active" : ""
              }`}
              onClick={() => setCurrentPage("overview")}
            >
              <Sparkles size={18} />
              <span>Overview</span>
            </button>


            <button
              className={`nav-item ${
                currentPage === "analyze" ? "active" : ""
              }`}
              onClick={() => setCurrentPage("analyze")}
            >
              <ScanLine size={18} />
              <span>Analyze food</span>
            </button>


            <button
              className={`nav-item ${
                currentPage === "history" ? "active" : ""
              }`}
              onClick={() => setCurrentPage("history")}
            >
              <History size={18} />
              <span>Food history</span>
            </button>


            <button
              className={`nav-item ${
                currentPage === "profile" ? "active" : ""
              }`}
              onClick={() => setCurrentPage("profile")}
            >
              <CircleUserRound size={18} />
              <span>Profile & goals</span>
            </button>

          </nav>

        </div>


        <div className="sidebar-bottom">

          <div className="wellness-card">
            <Sparkles size={17} />

            <strong>A gentler way to eat</strong>

            <p>
              One good choice at a time is more than enough.
            </p>
          </div>


          <button
           className="preferences"
           onClick={() => setCurrentPage("preferences")}
          >
           <SlidersHorizontal size={17} />
           <span>Preferences</span>
          </button>

        </div>

      </aside>


      <div className="main-area">

        <header className="top-header">

          <div className="header-left">

            <p className="header-eyebrow">
              {currentPage === "analyze"
                ? "FOOD ANALYSIS"
                : currentPage === "history"
                ? "YOUR PATTERNS, NOT YOUR PERFECTION"
                : currentPage === "profile"
                ? "YOUR PERSONAL PLAN"
                : "YOUR DAILY OVERVIEW"}
            </p>

            <h1>
  {currentPage === "analyze"
    ? "Analyze a food"
    : currentPage === "history"
    ? "Food history"
    : currentPage === "profile"
    ? "Profile & goals"
    : (() => {
        const hour = new Date().getHours();

        let greeting;

        if (hour >= 5 && hour < 12) {
          greeting = "Good morning";
        } else if (hour >= 12 && hour < 17) {
          greeting = "Good afternoon";
        } else if (hour >= 17 && hour < 21) {
          greeting = "Good evening";
        } else {
          greeting = "Good night";
        }

        return `${greeting}, ${profile?.name || "User"}`;
      })()}
</h1>

          </div>


          <div className="header-right">

            <button
              className="theme-button"
              onClick={() => setTheme(theme === "light" ? "dark" : "light")}
              title={theme === "light" ? "Switch to Night Mode" : "Switch to Day Mode"}
            >
              {theme === "light" ? "🌙" : "☀️"}
            </button>

          <div className="notification-wrapper">

  <button
  className="notification-button"
  onClick={() => {
  setShowNotifications(!showNotifications);
}}
>
  <Bell size={19} />

  {hasUnreadNotifications && (
    <span className="notification-dot"></span>
  )}
</button>

  {showNotifications && (
    <div className="notification-panel">

      <div className="notification-panel-header">
  <div>
    <strong>Notifications</strong>
    <span>Stay updated with NutriWise</span>
  </div>

  <div className="notification-panel-actions">
    <button
      className="notification-mark-read"
      onClick={() => {
        setHasUnreadNotifications(false);
        localStorage.setItem(
          "nutriwise_notifications_read",
          "true"
        );
      }}
    >
      Mark all as read
    </button>

    <button
      className="notification-close"
      onClick={() => setShowNotifications(false)}
    >
      ×
    </button>
  </div>
</div>

      <div className="notification-item">
        <div className="notification-icon">
          <Sparkles size={16} />
        </div>

        <div>
          <strong>Welcome to NutriWise</strong>
          <span>Your personalized nutrition journey is ready.</span>
        </div>
      </div>

      <div className="notification-item">
        <div className="notification-icon">
          <Leaf size={16} />
        </div>

        <div>
          <strong>Keep tracking your meals</strong>
          <span>Add your meals regularly to understand your daily nutrition.</span>
        </div>
      </div>

      <div className="notification-empty">
        You're all caught up 🎉
      </div>

    </div>
  )}

</div>


          <div className="user-menu-wrapper">

  <button
    className="user-menu"
    onClick={() => setShowUserMenu(!showUserMenu)}
  >
    <div className="avatar">
      M
    </div>

    <div className="user-info">
      <strong>{profile?.name || "User"}</strong>
      <span>Wellness journey</span>
    </div>

    <ChevronDown size={16} />
  </button>

  {showUserMenu && (
    <div className="user-dropdown">

      <button
        onClick={() => {
          setCurrentPage("profile");
          setShowUserMenu(false);
        }}
      >
        Profile & Goals
      </button>

      <button
        onClick={() => {
          setCurrentPage("preferences");
          setShowUserMenu(false);
        }}
      >
        Preferences
      </button>

      <button
        onClick={() => {
          localStorage.removeItem("access_token");
          setIsLoggedIn(false);
          setShowUserMenu(false);
        }}
      >
        Log out
      </button>

    </div>
  )}

</div>
          </div>

        </header>


        {currentPage === "overview" && (
          <OverviewPage
            onAnalyze={() => setCurrentPage("analyze")}
            dailySummary={dailySummary}
            foodHistory={foodHistory}
            profile={profile}
            goalData={goalData}
          />
        )}

        {explorePage && (
          <ExploreFoodsPage
            onBack={() => setExplorePage(false)}
            profile={profile}
          />
        )}

      {currentPage === "analyze" && (
        <AnalyzeFoodPage
          onFoodAdded={refreshFoodData}
          profile={profile}
          setCurrentPage={setCurrentPage}
        />
      )}

      {currentPage === "explore" && (
        <ExploreFoodsPage
          onBack={() => setCurrentPage("analyze")}
          profile={profile}
        />
      )}


      {explorePage && (
        <ExploreFoodsPage
          onBack={() => setExplorePage(false)}
          profile={profile}
        />
      )}

        {currentPage === "history" && (
          <FoodHistoryPage
            foodHistory={foodHistory}
          />
        )}

        {currentPage === "profile" && (
          <ProfileGoalsPage
            profile={profile}
            onProfileUpdated={fetchProfile}
          />
        )}

        {currentPage === "preferences" && (
          <PreferencesPage />
        )}

      </div>

    </div>
  );
}


export default App;