# main.py

import os
import time
import openai
import psutil
import pyautogui
# import other libraries as needed

# Load API keys from .env (optional)
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize AI model (example with OpenAI API)
def ask_gpt(prompt):
    import openai
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

# Example task: simple system info
def system_status():
    print(f"CPU usage: {psutil.cpu_percent()}%")
    print(f"Memory usage: {psutil.virtual_memory().percent}%")

# Main loop
def main():
    while True:
        user_input = input("Command for AI Agent: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Shutting down...")
            break
        # Ask GPT for instructions
        gpt_response = ask_gpt(user_input)
        print("AI says:", gpt_response)
        # Here you could add code to execute tasks based on GPT response
        # For now, just print
        time.sleep(1)

if __name__ == "__main__":
    main()
