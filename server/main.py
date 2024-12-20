from flask import Flask, request, jsonify
from flask_cors import CORS
from friendly_reminder import reminder


app = Flask(__name__)
CORS(app)

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

    response = reminder(name, ethnicity, age, height, weight)



    return jsonify({
        "message": "Data received successfully",
        "received_data": data
    }), 200


if __name__ == '__main__':
    app.run(debug=True, port=5001)
