#!/usr/bin/python3

from flask import Flask, jsonify, request

# instantiate Flask webserver from Flask module
app = Flask(__name__)

users = {}

# define route for root URL (OK)
@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def data():
    # users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}
    usernames = list(users.keys())
    return jsonify(usernames)

# handling status route (OK)
@app.route('/status')
def status():
    return "OK"

@app.route("/users/<username>")
def get_username(username):
    if username in users:
        return jsonify(users[username])
    else:
        return (jsonify({"error": "User not found"}), 404)

@app.route('/add_user', methods=['POST'])
def add_user():
    # {"username": "john", "name": "John", "age": 30, "city": "New York"}
    # parses JSON data into Python dict
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    if username in data:
        return jsonify({"error": "Username already exists"}), 400
    
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run()