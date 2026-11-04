
import os
from dotenv import load_dotenv

from google import genai
from google.genai import errors

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Explain Generative AI in simple words."
    )

    print(response.text)

except errors.APIError as e:
    print("Gemini API error:", e)
