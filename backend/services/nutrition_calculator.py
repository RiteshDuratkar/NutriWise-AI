def calculate_bmr(
    weight: float,
    height: float,
    age: int,
    gender: str
) -> float:
    """
    Calculate Basal Metabolic Rate (BMR)
    using the Mifflin-St Jeor equation.
    """

    gender = gender.lower()

    if gender == "male":
        return (
            10 * weight
            + 6.25 * height
            - 5 * age
            + 5
        )

    elif gender == "female":
        return (
            10 * weight
            + 6.25 * height
            - 5 * age
            - 161
        )

    else:
        raise ValueError(
            "Gender must be male or female"
        )


def calculate_tdee(
    bmr: float,
    activity_level: str
) -> float:
    """
    Calculate Total Daily Energy Expenditure (TDEE)
    using the user's activity level.
    """

    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "lightly_active": 1.375,
        "moderate": 1.55,
        "moderately_active": 1.55,
        "active": 1.725,
        "very_active": 1.725,
        "extra_active": 1.9
    }

    activity_level = activity_level.lower()

    if activity_level not in activity_multipliers:
        raise ValueError(
            "Invalid activity level"
        )

    return bmr * activity_multipliers[activity_level]


def calculate_calorie_target(
    tdee: float,
    goal: str
) -> float:
    """
    Calculate recommended daily calories
    based on the user's goal.
    """

    goal = goal.lower()

    if goal == "weight_loss":
        return tdee - 500

    elif goal == "weight_gain":
        return tdee + 300

    elif goal == "maintenance":
        return tdee

    else:
        raise ValueError(
            "Invalid goal"
        )


def calculate_protein_target(
    weight: float,
    goal: str
) -> float:
    """
    Calculate recommended daily protein
    based on body weight and goal.
    """

    goal = goal.lower()

    if goal == "weight_loss":
        protein_multiplier = 1.6

    elif goal == "weight_gain":
        protein_multiplier = 1.6

    elif goal == "maintenance":
        protein_multiplier = 1.2

    else:
        raise ValueError(
            "Invalid goal"
        )

    return weight * protein_multiplier