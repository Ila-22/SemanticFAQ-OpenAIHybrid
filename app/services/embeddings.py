import numpy as np
from openai import OpenAI
from app.core.config import OPENAI_API_KEY, EMBEDDING_MODEL
from app.services.faq_data import get_faq_data

_embedded_cache = None
client = OpenAI(api_key=OPENAI_API_KEY)

def compute_embedding(text: str) -> list:
    """
    response = client.embeddings.create(
        input=text,
        model=EMBEDDING_MODEL
    )
    return response['data'][0]['embedding']
    """
    return np.random.rand(1536).tolist()


def embed_faq_questions():
    faq_items = get_faq_data()
    embedded_faqs = []

    for item in faq_items:
        question = item["question"]
        embedding = compute_embedding(question)
        embedded_faqs.append({
            "question": question,
            "answer": item["answer"],
            "embedding": embedding
        })

    return embedded_faqs

def get_embedded_faqs():
    global _embedded_cache
    if _embedded_cache is None:
        _embedded_cache = embed_faq_questions()
    return _embedded_cache