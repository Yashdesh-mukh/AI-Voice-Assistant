import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)

def get_ai_reply(user_text):
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview", 
            contents= f"max 50 words.{user_text}"
        )

        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        return "Sorry, something went wrong with AI."
