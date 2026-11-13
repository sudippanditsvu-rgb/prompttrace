import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()


def get_api_key():
    # First, check local environment / .env
    api_key = os.getenv("GEMINI_API_KEY")

    # If not found, check Streamlit Cloud Secrets
    if not api_key:
        try:
            import streamlit as st
            api_key = st.secrets.get("GEMINI_API_KEY")
        except Exception:
            api_key = None

    if not api_key:
        raise ValueError(
            "Gemini API key not found. "
            "Configure GEMINI_API_KEY in your environment or Streamlit Secrets."
        )

    return api_key


client = genai.Client(api_key=get_api_key())


def generate_response(prompt):
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )
            return response.text

        except errors.APIError:
            if attempt == 2:
                raise

            time.sleep(2 * (attempt + 1))