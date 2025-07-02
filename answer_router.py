from config import SIMILARITY_THRESHOLD
from similarity import find_most_similar_question
from embeddings import embed_faq_questions, compute_embedding
from openai_fallback import get_openai_answer  # We'll create this next

embedded_faqs = embed_faq_questions()  # Load once at startup

def route_question(user_question: str):
    match, score = find_most_similar_question(user_question, embedded_faqs)

    if score >= SIMILARITY_THRESHOLD:
        return {
            "source": "local",
            "matched_question": match["question"],
            "answer": match["answer"],
            "score": score
        }
    else:
        openai_answer = get_openai_answer(user_question)
        return {
            "source": "openai",
            "matched_question": "N/A",
            "answer": openai_answer,
            "score": score
        }
