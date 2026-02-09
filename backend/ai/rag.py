import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# backend/data/knowledge_base
KNOWLEDGE_BASE_PATH = os.path.join(BASE_DIR, "data", "knowledge_base")

def load_knowledge():
    knowledge = {}

    if not os.path.exists(KNOWLEDGE_BASE_PATH):
        return knowledge

    for file in os.listdir(KNOWLEDGE_BASE_PATH):
        if file.endswith(".json"):
            with open(os.path.join(KNOWLEDGE_BASE_PATH, file), "r", encoding="utf-8") as f:
                knowledge.update(json.load(f))

    return knowledge


def retrieve_knowledge(message):
    knowledge = load_knowledge()
    message = message.lower()

    for key, value in knowledge.items():
        if key.replace("_", " ") in message:
            return value

    return None
