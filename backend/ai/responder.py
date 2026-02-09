from ai.intent_detector import detect_intent
from ai.rag import retrieve_knowledge

def generate_ai_response(user_message):
    intent = detect_intent(user_message)

    # RAG check for platform questions
    knowledge = retrieve_knowledge(user_message)
    if knowledge:
        return (
            f"{knowledge}\n"
            "If you need help with the next step, feel free to ask."
        )

    if intent == "emotional":
        return (
            "It’s completely okay to feel this way.\n"
            "Restarting something new can feel overwhelming.\n"
            "You’re showing courage by trying.\n"
            "We’ll take this one step at a time."
        )

    if intent == "technical":
        return (
            "That’s a good question.\n"
            "Technical concepts take time to understand.\n"
            "We’ll break it down slowly and clearly.\n"
            "You’re doing better than you think."
        )

    if intent == "career":
        return (
            "Career decisions can feel confusing at first.\n"
            "You don’t need to have everything figured out now.\n"
            "Exploring step by step helps build clarity.\n"
            "You’re on the right path."
        )

    return (
        "I’m here to support you.\n"
        "Feel free to ask anything.\n"
        "We can explore this together.\n"
        "You’re not alone."
    )
