from app.services.ai_router import classify_question
from app.core.config import settings
from app.services.similarity import find_most_similar_question
from app.services.embeddings import get_embedded_faqs, compute_embedding
from app.services.openai_fallback import get_openai_answer
from app.core.logger import get_logger

logger = get_logger(__name__)

# Load embedded FAQs once at startup
embedded_faqs = get_embedded_faqs()

def route_question(user_question: str) -> dict:
    """
    Routes question based on classification:
    - If IT: continue with similarity + OpenAI fallback
    - If COMPLIANCE: return default message
    """
    classification = classify_question(user_question)
    logger.debug(f"Classification result: {classification}")

    if classification == "COMPLIANCE":
        return {
            "source": "ComplianceAgent",
            "matched_question": "N/A",
            "answer": "This is not really what I was trained for, therefore I cannot answer. Try again."
        }
    
    # Otherwise continue with normal FAQ flow 
    try:
        match, score = find_most_similar_question(user_question, embedded_faqs)

        if score >= settings.similarity_threshold:
            logger.debug("Using local FAQ answer.")
            return {
                "source": "local",
                "matched_question": match.get("original_question", match["question"]),
                "answer": match["answer"],
                #"score": score
            }
        else:
            logger.debug("Using OpenAI fallback.")
            openai_answer = get_openai_answer(user_question)
            return {
                "source": "openai",
                "matched_question": "N/A",
                "answer": openai_answer,
                #"score": score
            }

    except Exception as e:
        logger.error(f"Routing failed: {e}", exc_info=True)
        raise RuntimeError("Failed to route the question.")
