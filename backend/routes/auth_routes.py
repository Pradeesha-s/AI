from flask import Blueprint, request, jsonify
from database.db import get_db_connection

auth_routes = Blueprint("auth_routes", __name__)

@auth_routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    if not all([name, email, password, role]):
        return jsonify({"message": "All fields are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
            (name, email, password, role)
        )
        conn.commit()
    except Exception:
        return jsonify({"message": "Email already exists"}), 409
    finally:
        conn.close()

    return jsonify({"message": "User registered successfully"}), 201

@auth_routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, email, role, password FROM users WHERE email = ?",
        (email,)
    )
    user = cursor.fetchone()
    conn.close()

    if user is None:
        return jsonify({"message": "User not found"}), 404

    if user["password"] != password:
        return jsonify({"message": "Invalid password"}), 401

    return jsonify({
        "message": "Login successful",
        "user": {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "role": user["role"]
        }
    }), 200
