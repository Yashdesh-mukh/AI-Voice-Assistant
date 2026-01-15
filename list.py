import os
import google.generativeai as genai
from google import genai

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key)

models = genai.list_models()
for model in models:
    print(model.name)
