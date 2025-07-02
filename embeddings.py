import openai
from config import OPENAI_API_KEY, EMBEDDING_MODEL
from faq_data import get_faq_data


openai.api_key = OPENAI_API_KEY

def compute_embedding(text: str) -> list:
    response = openai.Embedding.create(
        input=text,
        model=EMBEDDING_MODEL
    )
    return response['data'][0]['embedding']


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