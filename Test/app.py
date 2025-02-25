import os
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS

API_KEY = os.getenv("AZURE_AI_TEXT_API_KEY")
API_ENDPOINT = os.getenv("AZURE_AI_TEXT_API_ENDPOINT")

if not API_KEY or not API_ENDPOINT:
    raise ValueError("AZURE_AI_TEXT_API_KEY and AZURE_AI_TEXT_API_ENDPOINT must be set in .env")

@app.route('/api/process_text', methods=['POST'])
def process_text():
    try:
        data = request.get_json()
        text_to_process = data.get('text')

        if not text_to_process:
            return jsonify({'error': 'No text provided'}), 400

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'  # Or however your API authenticates
        }

        payload = {
            "documents": [
                {
                    "id": "1",
                    "text": text_to_process
                }
            ]
        }

        api_url = f"{API_ENDPOINT}/sentiment" # Example.  CHANGE THIS!
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return jsonify(result), 200

    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return jsonify({'error': f'API request error: {e}'}), 500
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production!