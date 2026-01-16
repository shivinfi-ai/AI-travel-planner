import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Hugging Face API Key
HF_API_KEY = os.getenv("HF_API_key")

# Hugging Face Inference API (Mistral model)
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct"
HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}


def generate_itinerary(start_city, dest, budget, days, interests):
    """
    Generates a student-friendly, budget travel itinerary
    using Hugging Face Mistral model.
    """

    prompt = f"""
You are an AI travel planner for students in India.

Create a realistic {days}-day travel itinerary.

Trip Details:
- Starting City: {start_city}
- Destination: {dest}
- Total Budget: ₹{budget}
- Interests: {', '.join(interests)}

Guidelines:
- Focus on budget-friendly options
- Use public transport where possible
- Suggest student-friendly hostels or stays
- Include local attractions and free places
- Provide a day-wise breakdown
- Keep suggestions practical and realistic

Output format:
Day 1:
- Activities
- Transport
- Food suggestions
- Approximate cost

Day 2:
...
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 700,
            "temperature": 0.7,
            "top_p": 0.9,
            "do_sample": True
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    try:
        result = response.json()

        # Handle both HF formats
        if isinstance(result, list):
            return result[0]["generated_text"]
        else:
            return result["generated_text"]

    except:
        return "⚠️ Unable to generate itinerary at the moment. Please try again."

