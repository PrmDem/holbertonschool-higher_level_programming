from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager, get_jwt

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "map477bng74861xrvg18qtrzw"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username)["password"], password):
        return username

@app.route('/basic-protected')
@auth.login_required
def index():
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def user_login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user=users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify('{"error": "Unauthorized"}'), 401

    access_token = create_access_token(identity=username, additional_claims={"role": user["role"]})
    return jsonify(access_token=access_token)

@app.route('/jwt-protected')
@jwt_required()
def access_jwt():
    current_user = get_jwt_identity()
    return "JWT Auth: Access Granted"

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@app.route('/admin-only')
@jwt_required()
def access_admin():
    current_user = get_jwt()
    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

if __name__ == '__main__':
    app.run()
