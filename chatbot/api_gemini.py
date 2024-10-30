from dotenv import load_dotenv
import os
import google.generativeai as genai
import time

load_dotenv()

API_KEY = os.getenv('API_KEY')

def ai_response(user_input):
    #Fetching the Gemini API
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_input).text

    #splits response so it displays word after word
    response_list = response.split(' ')

    for word in response_list:
        print(f"{word} ", end='', flush=True)
        time.sleep(0.1)
