
import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import errors


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def generate_response(prompt):

    for attempt in range(3):

        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

            return response.text

        except errors.APIError as e:

            print("Gemini API error:", e)

            if attempt < 2:
                wait_time = 2 ** (attempt + 1)

                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)

            else:
                raise
