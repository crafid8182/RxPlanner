from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
##import requests
import prescription_analyzer

load_dotenv()

app = Flask(__name__)

openai_api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return "Backend Live"

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
    app.run(debug=True)