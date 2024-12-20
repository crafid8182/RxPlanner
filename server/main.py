from flask import Flask, request, jsonify
from flask_cors import CORS


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

    

    return jsonify({
        "message": "Data received successfully",
        "received_data": data
    }), 200


if __name__ == '__main__':
    app.run(debug=True, port=5001)
