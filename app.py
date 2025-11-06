from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded user credentials
USER_CREDENTIALS = {
    "username": "admin",
    "password": "password123"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
        return jsonify({"message": "Login successful", "user": username}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
