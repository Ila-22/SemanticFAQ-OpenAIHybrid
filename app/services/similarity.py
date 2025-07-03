import numpy as np
from app.services.embeddings import compute_embedding
from typing import List, Dict, Tuple

def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def find_most_similar_question(
    user_question: str, 
    embedded_faqs: List[Dict]
) -> Tuple[Dict, float]:
    user_embedding = compute_embedding(user_question)
    
    best_match = None
    best_score = -1.0

    for item in embedded_faqs:
        score = cosine_similarity(user_embedding, item["embedding"])
        if score > best_score:
            best_match = item
            best_score = score

    return best_match, best_score
