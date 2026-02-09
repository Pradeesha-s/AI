from flask import Blueprint, request, jsonify
from ai.responder import generate_ai_response

chat_routes = Blueprint("chat_routes", __name__)

@chat_routes.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"error": "Message is required"}), 400

    ai_reply = generate_ai_response(message)

    return jsonify({
        "reply": ai_reply
    })
