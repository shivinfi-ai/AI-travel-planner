def health_chat(user_question, city):
    """
    Offline health & travel safety assistant
    No API required
    """

    q = user_question.lower()

    # -------- FOOD SAFETY --------
    if "street food" in q or "food" in q:
        return (
            f"🍽 Food Safety Tips in {city}:\n"
            "- Choose busy stalls with high turnover\n"
            "- Eat freshly cooked and hot food\n"
            "- Avoid raw salads and uncovered items\n"
            "- Prefer bottled or filtered water\n"
            "- Wash hands before eating"
        )

    # -------- WATER SAFETY --------
    if "water" in q or "drink" in q:
        return (
            "💧 Water Safety Tips:\n"
            "- Avoid tap water\n"
            "- Use sealed bottled water\n"
            "- Avoid ice cubes in roadside drinks"
        )

    # -------- WEATHER & HEAT --------
    if "heat" in q or "summer" in q or "hot" in q:
        return (
            "☀️ Heat Protection Tips:\n"
            "- Stay hydrated\n"
            "- Wear light cotton clothes\n"
            "- Avoid direct sun between 12–3 PM\n"
            "- Use sunscreen"
        )

    # -------- COLD / RAIN --------
    if "rain" in q or "monsoon" in q or "cold" in q:
        return (
            "🌧 Weather Safety Tips:\n"
            "- Carry umbrella or raincoat\n"
            "- Avoid street food in heavy rain\n"
            "- Wear dry footwear to prevent infections"
        )

    # -------- MEDICAL EMERGENCY --------
    if "emergency" in q or "hospital" in q or "doctor" in q:
        return (
            "🏥 Emergency Tips:\n"
            "- Keep emergency contact numbers saved\n"
            "- Locate nearest hospital via Google Maps\n"
            "- Carry basic medicines"
        )

    # -------- GENERAL TRAVEL HEALTH --------
    return (
        "🩺 General Travel Health Advice:\n"
        "- Carry a basic first-aid kit\n"
        "- Get enough sleep\n"
        "- Avoid over-exertion\n"
        "- Inform someone about your travel plan"
    )
