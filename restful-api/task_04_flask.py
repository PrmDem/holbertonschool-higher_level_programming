#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data_page():
    user_names = list(users.keys())
    return jsonify(user_names)


@app.route("/status")
def get_status():
    return "OK"


@app.route("/user/<username>")
def user_page(username):
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_new_user():
    data = request.get_json()
    if not data['username'] or not data:
        return jsonify({"error": "Username is required"}), 400
    else:
        username = data['username']
        users[username] = {
            "username": data.get['username'],
            "name": data.get['name'],
            "age": data.get['age'],
            "city": data.get['city']
        }
        return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
