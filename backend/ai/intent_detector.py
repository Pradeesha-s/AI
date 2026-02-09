def detect_intent(message: str) -> str:
    message = message.lower()

    emotional_keywords = [
        "sad", "confused", "lost", "stressed", "worried",
        "anxious", "scared", "overwhelmed", "not confident",
        "don’t know", "dont know"
    ]

    platform_keywords = [
        "task", "quiz", "dashboard", "login", "course",
        "assessment", "assignment", "submission"
    ]

    technical_keywords = [
        "react", "javascript", "python", "flask",
        "api", "backend", "frontend", "error", "bug"
    ]

    career_keywords = [
        "job", "career", "role", "roadmap",
        "interview", "resume", "cv"
    ]

    for word in emotional_keywords:
        if word in message:
            return "emotional_support"

    for word in platform_keywords:
        if word in message:
            return "platform_help"

    for word in technical_keywords:
        if word in message:
            return "technical_question"

    for word in career_keywords:
        if word in message:
            return "career_guidance"

    return "general_query"
