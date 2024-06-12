import os

import google.generativeai as genai
# pip install -q -U google-generativeai

class GeminiChat:
    def __init__(self, model_name):
        self.model_name = model_name
        self.api_key = os.getenv("GOOGLE_API_KEY")

        try:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)
            self.chat = self.model.start_chat(history=[])
        except Exception as e:
            print(f"Failed to initialize Gemini Model: {e}")

    def request(self, user_input):
        """Sends user input to the chat session and returns the response."""
        response = self.chat.send_message(user_input, stream=True)
        response.resolve()
        return response


    def get_last_response(self):
        """Returns the last response from the chat history."""
        if self.chat.history:
            last_message = self.chat.history[-1]
            return f"\n**{last_message.role}**: {last_message.parts[0].text}"
        else:
            return "This is a new chat. How can I help you today?"
