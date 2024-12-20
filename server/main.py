from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import prescription_analyzer

load_dotenv()

app = Flask(__name__)

# Enable CORS globally
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

openai_api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return "Backend Live"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'password':
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Login failed'}), 401

@app.route('/analyze', methods=['POST'])
def analyze():
    # user input
    image_path = request.json['prescription']
    ics_path = prescription_analyzer.main(image_path)

    print("ICS_PATH", ics_path)
    if not ics_path:
        json = {
            'success': False,
            'ics_path': ""
        }
    else:
        json = {
            'success': True,
            'ics_path': ics_path,
        }

    return jsonify(json)

if __name__ == '__main__':
    app.run(port=5000)
