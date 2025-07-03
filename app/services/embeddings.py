import numpy as np
from openai import OpenAI
from app.core.config import settings
from app.services.faq_data import get_faq_data

# Initialize OpenAI client with API key from config
client = OpenAI(api_key=settings.openai_api_key)

def compute_embedding(text: str) -> list:
    """
    Computes an embedding for a given text.
    """

    # Use real OpenAI embedding call in production:
    response = client.embeddings.create(
        input=text,
        model=settings.embedding_model
    )

    # Mocked embedding for dev/testing:
    #return np.random.rand(1536).tolist()

    return response.data[0].embedding


# Global cache for embedded FAQs
_embedded_cache = None

def get_embedded_faqs():
    """
    Returns FAQ questions with their embeddings, cached after first load.
    """
    global _embedded_cache
    if _embedded_cache is None:
        faq_items = get_faq_data()
        _embedded_cache = []

        for item in faq_items:
            embedding = compute_embedding(item["question"])
            _embedded_cache.append({
                "id": item.get("id"),
                "question": item["question"], # Cleaned/preprocessed version
                "original_question": item["original_question"],  # Raw original from file
                "answer": item["answer"],
                "embedding": embedding
            })

    return _embedded_cache

