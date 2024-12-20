import os
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from friendly_reminder import reminder
from prescription_analyzer import main as analyzer_main


app = Flask(__name__)
CORS(app)

# gets API sent from frontend with prescription image and returns ical file
@app.route('/api/img', methods=['POST'])
def analyze():
    # Check if 'image' is in the request
    if 'image' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['image']

    # Ensure a file was selected
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400


    # save uploaded file and define the upload directory
    UPLOAD_DIR = "/Users/moeraff/Documents/Coding/rx-project/data/img"
    os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure directory exists

    # save the file
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    file.save(filepath)

    # pass the saved file to the analyzer
    relative_path = f"/data/img/{file.filename}" 
    ics_path = analyzer_main(relative_path)

    # send the ical file to the frontend so the user can download it
    if ics_path:
        full_ics_path = os.path.join("/Users/moeraff/Documents/Coding/rx-project", ics_path.lstrip('/'))
        return send_file(full_ics_path, as_attachment=True, download_name=os.path.basename(ics_path))
    else:
        return jsonify({"error": "Error processing image"}), 500

    

# gets API sent from the front end about user biometrics
@app.route('/api/submit', methods=['POST'])
def get_details():
    data = request.get_json()
    print(data)
    
    # fill data based on user input otherwise prefill with 'Unknown'
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




# run the backend on port 5001 not the default flask 5000 
# because Mac uses 5000 for its internal purposes
if __name__ == '__main__':
    app.run(debug=True, port=5001)
