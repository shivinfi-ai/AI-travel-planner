import streamlit as st
from ai_itinerary import generate_itinerary
from budget_optimizer import budget_breakdown
from food_suggester import suggest_food
from health_bot import health_chat

from dotenv import load_dotenv
load_dotenv()

# ---------- LOAD FRONTEND CSS ----------
def load_css():
    try:
        with open("frontend/style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except:
        pass

load_css()

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="🎒 AI Travel Planner for Students", layout="centered")

st.title("🎒 AI Travel Planner for Students")
st.caption("Personalized • Budget-Friendly • AI Powered")

# ---------- USER INPUT FORM ----------
with st.form("travel_form"):
    st.subheader("📌 Enter Trip Details")

    start = st.text_input("Starting City *", placeholder="e.g., Bangalore")
    destination = st.text_input("Destination City *", placeholder="e.g., Hampi")

    col1, col2 = st.columns(2)
    with col1:
        budget = st.number_input("Total Budget (₹) *", min_value=1000, max_value=50000, step=500)
    with col2:
        days = st.number_input("Number of Days *", min_value=1, max_value=10, step=1)

    travel_type = st.selectbox("Travel Type", ["Solo", "Friends", "College Trip", "Backpacking"])

    interests = st.multiselect("Select Interests *", ["Nature", "Beaches", "History", "Food", "Adventure", "Shopping"])

    travel_mode = st.radio("Preferred Transport", ["Bus", "Train", "Bike", "Any"])

    food_type = st.selectbox("Food Preference", ["All", "Vegetarian", "Non-Vegetarian"])

    submit = st.form_submit_button("🚀 Generate Travel Plan")

# ---------- HANDLE SUBMISSION ----------
if submit:

    if not start or not destination or not interests:
        st.error("⚠️ Please fill all required fields marked with *.")
    else:
        # -------- AI ITINERARY --------
        with st.spinner("🤖 AI is planning your trip..."):
            itinerary = generate_itinerary(
                start_city=start,
                dest=destination,
                budget=budget,
                days=days,
                interests=", ".join(interests)   # FIXED for HuggingFace
            )

        st.success("✅ Travel Plan Generated")

        st.markdown("## 🗺️ AI-Generated Itinerary")
        st.write(itinerary)

        # -------- BUDGET BREAKDOWN --------
        breakdown, daily_food_budget, daily_stay_budget = budget_breakdown(budget, days)

        st.markdown("## 💰 Budget Breakdown")
        st.table(breakdown)

        col1, col2 = st.columns(2)
        with col1:
            st.info(f"🍽 Daily Food Budget: ₹{daily_food_budget}")
        with col2:
            st.info(f"🏨 Daily Stay Budget: ₹{daily_stay_budget}")

        # -------- FOOD SUGGESTER --------
        st.markdown("## 🍴 Food Suggestions (Restaurants & Street Food)")
        with st.spinner("Finding safe and affordable food options..."):
            food_plan = suggest_food(destination, daily_food_budget, food_type)
            st.write(food_plan)

        # -------- HEALTH COMPANION CHATBOT --------
        st.markdown("## 🩺 Health Companion Chatbot")
        st.caption("Ask about food safety, health, weather, or travel tips")

        user_health_query = st.text_input("Ask a health-related question")

        if user_health_query:
            with st.spinner("Health Companion is responding..."):
                health_response = health_chat(user_health_query, destination)
                st.write(health_response)

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Built with ❤️ using Hugging Face & Streamlit")

