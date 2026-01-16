def budget_breakdown(total_budget, days):
    breakdown = {
        "Transport": int(total_budget * 0.30),
        "Stay": int(total_budget * 0.35),
        "Food": int(total_budget * 0.20),
        "Attractions": int(total_budget * 0.10),
        "Emergency": int(total_budget * 0.05)
    }

    daily_food_budget = breakdown["Food"] // days
    daily_stay_budget = breakdown["Stay"] // days

    return breakdown, daily_food_budget, daily_stay_budget
