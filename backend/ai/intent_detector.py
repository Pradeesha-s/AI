def detect_intent(message):
    message = message.lower()

    emotional_keywords = [
        "lost", "confused", "scared", "anxious",
        "tired", "demotivated", "stress", "worried"
    ]

    technical_keywords = [
        "what is", "how", "api", "react", "python",
        "flask", "database", "backend", "frontend"
    ]

    career_keywords = [
        "career", "role", "job", "restart",
        "which", "path", "learn"
    ]

    if any(word in message for word in emotional_keywords):
        return "emotional"

    if any(word in message for word in technical_keywords):
        return "technical"

    if any(word in message for word in career_keywords):
        return "career"

    return "general"
