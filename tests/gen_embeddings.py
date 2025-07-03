from app.services.embeddings import embed_faq_questions

def main():
    faq_embeddings = embed_faq_questions()

    # test: print one to verify it's working
    for item in faq_embeddings[:1]:
        print("Sample question:", item["question"])
        print("Sample embedding (first 5 values):", item["embedding"][:5])

if __name__ == "__main__":
    main()
