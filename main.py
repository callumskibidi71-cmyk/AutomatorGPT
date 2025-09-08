# main.py
import os
import time
from dotenv import load_dotenv
from executor import run_command
from gpt import ask_gpt
from utils.helpers import safe_print, format_output

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def main():
    safe_print("AI Agent Started. Type 'exit' to quit.")
    
    while True:
        user_input = input("Command for AI Agent: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            safe_print("Shutting down AI Agent...")
            break
        
        gpt_response = ask_gpt(user_input)
        safe_print(f"GPT Response: {gpt_response}")

        # Only run GPT commands prepended with "run:"
        if "run:" in gpt_response:
            command = gpt_response.split("run:")[1].strip()
            output = run_command(command)
            print(format_output(output))
        else:
            safe_print("No executable command detected.")

        time.sleep(1)

if __name__ == "__main__":
    main()
