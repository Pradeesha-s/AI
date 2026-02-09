from ai.intent_detector import detect_intent
from ai.rag import retrieve_knowledge

def generate_ai_response(user_message: str) -> str:
    # 1️⃣ Knowledge ALWAYS comes first
    knowledge = retrieve_knowledge(user_message)
    if knowledge:
        return knowledge

    # 2️⃣ Intent only if no knowledge found
    intent = detect_intent(user_message)

    if intent == "emotional_support":
        return (
            "I understand how you’re feeling.\n"
            "It’s okay to feel this way.\n"
            "You’re not alone — I’m here with you."
        )

    if intent == "technical_question":
        return (
            "This looks like a technical question.\n"
            "Can you share more details so I can help you clearly?"
        )

    if intent == "career_guidance":
        return (
            "Career decisions can feel overwhelming.\n"
            "Let’s take it one step at a time."
        )

    # 3️⃣ Final fallback
    return (
        "I’m here to help you.\n"
        "Please let me know what you’d like support with."
    )
