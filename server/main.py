import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from friendly_reminder import reminder
from prescription_analyzer import main as analyzer_main


app = Flask(__name__)
CORS(app)


@app.route('/api/img', methods=['POST'])
def analyze():
    # Check if 'image' is in the request
    if 'image' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['image']

    # Ensure a file was selected
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Step 3: Save the uploaded file
    # Define the upload directory
    UPLOAD_DIR = "/Users/moeraff/Documents/Coding/rx-project/data/img"
    os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure directory exists

    # Save the file
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    file.save(filepath)

    # Pass the saved file to the analyzer
    from prescription_analyzer import main as analyzer_main
    relative_path = f"/data/img/{file.filename}"  # Relative path for the analyzer
    ics_path = analyzer_main(relative_path)

    if ics_path:
        return jsonify({
            "message": "Image analyzed and ICS file generated",
            "ics_path": ics_path
        }), 200
    else:
        return jsonify({"error": "Error processing image"}), 500

    


@app.route('/api/submit', methods=['POST'])
def get_details():
    data = request.get_json()
    print(data)
    
    name = data.get('name', 'Unknown')
    age = data.get('age', 'Unknown')
    height = data.get('height', 'Unknown')
    weight = data.get('weight', 'Unknown')
    ethnicity = data.get('ethnicity', 'Unknown')

    #print(name, age, height, weight, ethnicity)

    message = reminder(name, ethnicity, age, height, weight)
    print(message)



    return jsonify({
        "message": "Data received successfully",
        "received_data": data,
        "advisory": message
    }), 200





if __name__ == '__main__':
    app.run(debug=True, port=5001)
