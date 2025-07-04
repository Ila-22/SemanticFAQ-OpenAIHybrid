import json
import os
import re

DATA_PATH = os.path.join(os.path.dirname(__file__), "faq_data.json")

def preprocess_question(text: str) -> str:
    """
    Normalize question for embedding: lowercase, remove punctuation, extra spaces.
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return re.sub(r"\s+", " ", text).strip()

def get_faq_data() -> list[dict]:
    """
    Load and preprocess FAQ data from a JSON file.
    """
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        raw_faqs = json.load(f)

    processed = []
    for item in raw_faqs:
        processed.append({
            "id": item.get("id"),
            "question": preprocess_question(item["question"]),
            "original_question": item["question"],  # Keep original for reference
            "answer": item["answer"]
        })
    return processed