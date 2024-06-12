import os

import google.generativeai as genai
# pip install -q -U google-generativeai


# https://ai.google.dev/tutorials/python_quickstart

class GeminiAI:
    def __init__(self, model_name):
        self.model_name = model_name
        self.api_key = os.getenv("GOOGLE_API_KEY")

        try:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)
        except Exception as e:
            print(f"Failed to initialize Gemini: {e}")
            raise

    def generate_response(self, input_text):
        """Generates a response using Gemini model"""
        try:
            response = self.model.generate_content(input_text)
            return response
        except Exception as e:
            print(f"Error generating response: {e}")
            return None