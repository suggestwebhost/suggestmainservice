from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define URLs for the internal microservices
ADDITION_SERVICE_URL = "https://suggestadd.onrender.com/add"
MULTIPLICATION_SERVICE_URL = "https://suggestmultiply.onrender.com/multiply"

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data.get('operation')
    a = data.get('a')
    b = data.get('b')

    # Forward request based on the requested operation
    if operation == 'add':
        response = requests.post(ADDITION_SERVICE_URL, json={"a": a, "b": b})
        return jsonify(response.json()), response.status_code
        
    elif operation == 'multiply':
        response = requests.post(MULTIPLICATION_SERVICE_URL, json={"a": a, "b": b})
        return jsonify(response.json()), response.status_code
        
    else:
        return jsonify({"error": "Unsupported operation. Use 'add' or 'multiply'."}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)
