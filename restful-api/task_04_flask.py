#!/usr/bin/python3

import json
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return ("<p>Welcome to the Flask API!</p>")


@app.route("/data")
def data_page():
    user_names = list(users.keys())
    return jsonify(user_names)


@app.route("/status")
def get_status():
    return ("<p>OK</p>")


@app.route("/user/<username>")
def user_page(username):
    for key, val in users.items():
        if key == username:
            return jsonify(val)
    if username not in users:
        return jsonify({"error": "User not found"})


@app.route("/add_user", methods=["POST"])
def add_new_user():
    data = request.get_json()
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    else:
        username = data['username']
        users[username] = data
        return jsonify({
            "message": "User added",
            "user": users[username]
            }), 201


if __name__ == "__main__":
    app.run()
