import numpy as np
from openai import OpenAI
from config import OPENAI_API_KEY, EMBEDDING_MODEL
from faq_data import get_faq_data


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