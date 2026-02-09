from flask import Blueprint, jsonify, request
from database.db import get_db_connection

dashboard_routes = Blueprint("dashboard_routes", __name__)

@dashboard_routes.route("/dashboard/<int:user_id>", methods=["GET"])
def dashboard(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, role FROM users WHERE id = ?",
        (user_id,)
    )
    user = cursor.fetchone()

    if not user:
        conn.close()
        return jsonify({"message": "User not found"}), 404

    role = user["role"]

    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE role = ?",
        (role,)
    )
    total_tasks = cursor.fetchone()[0]

    completed_tasks = 0  # will connect submissions later
    active_tasks = total_tasks - completed_tasks

    conn.close()

    return jsonify({
        "name": user["name"],
        "role": role,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "active_tasks": active_tasks
    }), 200
