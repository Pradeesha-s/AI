import json
import os

# Resolve backend directory safely
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KNOWLEDGE_BASE_PATH = os.path.join(BASE_DIR, "data", "knowledge_base")

def load_knowledge():
    knowledge = {}

    if not os.path.exists(KNOWLEDGE_BASE_PATH):
        print("❌ Knowledge base path not found:", KNOWLEDGE_BASE_PATH)
        return knowledge

    for file in os.listdir(KNOWLEDGE_BASE_PATH):
        if file.endswith(".json"):
            file_path = os.path.join(KNOWLEDGE_BASE_PATH, file)
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                knowledge.update(data)

    return knowledge

def retrieve_knowledge(user_message: str):
    print("🔍 RAG CALLED")
    print("User message:", user_message)

    knowledge_base = load_knowledge()
    print("Knowledge base loaded:", knowledge_base)

    user_message = user_message.lower()

    for key, value in knowledge_base.items():
        key_words = key.lower().split()

        for word in key_words:
            if word in user_message:
                print("✅ MATCH FOUND:", word)
                return value

    print("❌ NO MATCH FOUND")
    return None
