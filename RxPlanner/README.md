import { useState } from "react";

function Start() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isPending, setIsPending] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    const login = { username, password };

    setIsPending(true);

    fetch("http://localhost:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(login),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          return response.json();
        })
        .then((data) => {
          console.log("Login successful:", data);
          setIsPending(false);
        })
        .catch((error) => {
          console.error("Error during fetch:", error);
          setIsPending(false);
        });
      


  };

  return (
    <>
      <h1>Get started by filling out some basic information!</h1>

      <form onSubmit={handleSubmit}>
        <div>
          <label>Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            required
            onChange={(e) => setUsername(e.target.value)}
          ></input>
        </div>

        <div>
          <label>Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            required
            onChange={(e) => setPassword(e.target.value)}
          ></input>
        </div>

        <div className="card">
          <button>Log in</button>
        </div>

      </form>
    </>
  );
}

export default Start;




from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
##import requests
import prescription_analyzer

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

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