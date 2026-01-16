import pandas as pd

# Load dataset
df_food = pd.read_csv("food_dataset.csv")

def suggest_food(city, daily_budget, food_type="All"):
    """
    Suggest food based on City, Budget and Type (Vegetarian / Non-Vegetarian)
    """

    # Filter by city
    city_food = df_food[df_food['City'].str.lower() == city.lower()]

    if city_food.empty:
        return f"⚠️ No food data found for {city}."

    # Filter by food type
    if food_type.lower() != "all":
        city_food = city_food[city_food['Type'].str.lower() == food_type.lower()]

        if city_food.empty:
            return f"⚠️ No {food_type} food found in {city}."

    # Filter by budget
    city_food_budget = city_food[city_food['Min_Price'] <= daily_budget]

    # If no food fits budget, show cheapest options
    if city_food_budget.empty:
        city_food_budget = city_food.sort_values("Min_Price").head(5)

    # Select top 5
    suggestions = city_food_budget.head(5)

    # Prepare output
    text = f"🍽️ Food suggestions for {city.title()} (Type: {food_type}) within ₹{daily_budget}\n\n"

    for i, row in enumerate(suggestions.itertuples(), 1):
        text += (
            f"{i}. {row.Dish} | {row.Category} | {row.Type} | "
            f"₹{row.Min_Price} – ₹{row.Max_Price}\n"
        )

    return text

