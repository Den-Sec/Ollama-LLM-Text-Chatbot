# Ollama-LLM-Text-Chatbot
This Python script enables users to interact with the Ollama LLM via text input. It offers a simple command-line interface to send questions and receive responses from the Ollama language model.

## Features

- **Dynamic Preprompt Customization:** Users can modify the preprompt context to change the AI's behavior or persona, making the interactions as flexible as needed.
- **Secure Configuration Management:** Utilizes environment variables to manage API configuration securely, ensuring sensitive information is kept out of the source code.
- **Robust Error Handling:** Includes mechanisms to gracefully handle network issues and API errors, ensuring the application remains responsive under various conditions.

## Requirements

- Python 3.6 or later.
- Internet connection to access the Ollama LLM API.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://your-repository-url-here
   cd your-repository-directory

2. **Setup Python Environment** (Optional but recommended)
You can use a virtual environment to isolate package dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use 'venv\Scripts\activate'

3. **Install Dependencies**
Install the required packages using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt

4. **Set Environment Variables**
Modify the `.env` file in the root of your project directory the following content:
    ```bash
    OLLAMA_URL=http://your-ollama-url:port
    MODEL_NAME=your-model-name

Replace `http://your-ollama-url:port` and `your-model-name` with your actual Ollama API URL and model name.

## Usage

Run the script from the command line:

    
    python3 main.py

Follow the prompts in the command line to enter questions. Type 'exit' to end the session.

## Contributing

Contributions to this project are more than welcome!

## License

Distributed under the MIT License. See LICENSE for more information.
