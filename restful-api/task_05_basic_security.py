#!/usr/bin/python3

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

app = Flask(__name__)
auth = HTTPBasicAuth()

# SECRET KEY (used to sign tokens)
app.config['SECRET_KEY'] = 'LOL@LM@O'

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    """
    Verifies that username and password combo provided by the client are valid. Returns user object if credentials valid, or None/False if not available.
    """
    if username in users and check_password_hash(users.get(username), password):
        return username
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Protected route using Basic Authentication"""
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """Login endpoint to get JWT token"""
    auth_data = request.get_json()
    if not auth_data or 'username' not in auth_data or 'password' not in auth_data:
                                          return jsonify({'error': 'Username and password required'}), 400
    username = auth_data['username']
    password = auth_data['password']

    if username in users and check_password_hash(users.get(username))
