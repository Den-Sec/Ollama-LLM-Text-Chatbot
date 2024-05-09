import os
import requests
from datetime import datetime
import sys
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration settings from environment variables or defaults
OLLAMA_URL = os.getenv("OLLAMA_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

def ask_question(question):
    """
    Send a query to the Ollama LLM and get the response, with error handling.
    """
    date_and_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    context = f"""
    
    You are an AI assistant. Respond in less than 80 words. {date_and_time}
    
    """
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "messages": [{"role": "system", "content": context}, {"role": "user", "content": question}],
                "stream": False
            },
            timeout=10  # Timeout for the request
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        response_data = response.json()
        return response_data.get('message', {}).get('content', "No content in response.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return "Failed to get a response due to a network error."

def main():
    """
    Main function to interact with the user and LLM via text input and output.
    """
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print("Usage: python script_name.py")
        return
    
    print("Welcome to the chat! Type 'exit' to end the session.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = ask_question(user_input)
        print("Assistant:", response)

if __name__ == "__main__":
    main()
