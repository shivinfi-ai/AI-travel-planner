import requests
import os

HF_API_KEY = os.getenv("HF_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def health_chat(user_question, city):
    prompt = f"""
    You are a travel health assistant.

    The user is traveling to {city}.
    The user asks: {user_question}

    Give safe, student-friendly medical and food hygiene advice.
    """

    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    try:
        result = response.json()

        # Handle both HuggingFace response formats
        if isinstance(result, list):
            return result[0]["generated_text"]
        else:
            return result["generated_text"]

    except:
        return "⚠️ Health service is temporarily unavailable. Please try again."
