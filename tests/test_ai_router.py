import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.ai_router import classify_question

def test_questions():
    questions = [
        "How do I reset my Outlook password?",
        "What are the rules for business casual dress?",
        "How can I access the VPN remotely?",
        "Can I expense a hotel for personal travel?",
        "What is DNS and how does it work?",
        "Am I allowed to bring my dog to the office?"
    ]

    for q in questions:
        try:
            result = classify_question(q)
            print(f"Q: {q}\n→ Classified as: {result}\n")
        except Exception as e:
            print(f"Error classifying: {q}\n→ {e}")
