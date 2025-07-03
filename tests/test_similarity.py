from app.services.similarity import find_most_similar_question
from app.services.embeddings import embed_faq_questions

faqs = embed_faq_questions()
user_question = "How do I change my name?"
match, score = find_most_similar_question(user_question, faqs)

print("Matched question:", match["question"])
print("Score:", score)
print("Answer:", match["answer"])
