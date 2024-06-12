from gemini import GeminiAI

from dotenv import load_dotenv

from img_to_text import GeminiImg
from chat import GeminiChat

# https://ai.google.dev/tutorials/python_quickstart

load_dotenv()

# text-to-text
model_name = "gemini-pro"
your_ai = GeminiAI(model_name)

def response(input):
    return your_ai.generate_response(input_text=input)

# img-to-text
model_name_img = "gemini-pro-vision"
your_img_ai = GeminiImg(model_name_img)

def img_response(input, img):
    return your_img_ai.generate_response(input_text=input, input_img=img)


# chat
model_name_chat = "gemini-pro"
chatbot = GeminiChat(model_name_chat)

def chat_reponse():
    while True:
        print(chatbot.get_last_response())
        user_input = input("\nAsk: ")

        if user_input == "":
            break

        chatbot.request(user_input)


if __name__ == "__main__":

    # text-to-text
    prompt = "Tell me a joke."
    print(response(input))    
    
    
    # img-to-text
    """
    prompt = ""
    img = "text-2-img.png"
    print(img_response(input=prompt, img=img))    
    """

    # chat
    # chat_reponse()

