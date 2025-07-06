# 📘 Semantic FAQ API

A FastAPI-powered backend that semantically matches user questions to a curated FAQ dataset using OpenAI embeddings, with intelligent classification and LLM fallback.

---

## 🚀 Features

- 🔐 **Token-based authentication using Bearer token format** 
- 🧠 **Semantic similarity matching** via OpenAI embeddings
- 🤖 **LLM-powered classification** (`IT` vs `COMPLIANCE`)
- 💬 **GPT-4o fallback** for unmatched questions
- ⚡ **LangChain integration** for prompt chaining
- 🧰 **Custom error handling**, logging, and config loading
- 📦 **Preprocessed and cached FAQs** for efficiency

---

## 🔧 Setup Instructions
1. **Clone the repository**
   ```bash
   git clone https://github.com/Ila-22/SemanticFAQ-OpenAIHybrid.git
   cd semantic-faq-api
3. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv\Scripts\activate on Windows
5. **Install dependencies**
   ```bash
   pip install -r requirements.txt
7. **Create your .env file**
   ```bash
   OPENAI_API_KEY=your_openai_key
   EMBEDDING_MODEL=text-embedding-3-small
   CHAT_MODEL=gpt-4o
   SIMILARITY_THRESHOLD=0.75

---

## ▶️ Running the App
```bash
uvicorn app.main:app --reload
```
Visit the auto-generated Swagger docs at: http://localhost:8000/docs

The authentication logic is implemented in app/core/auth.py using FastAPI’s APIKeyHeader:

```bash
VALID_TOKENS = {"ila_3f920e"}
```

To update valid tokens, modify the VALID_TOKENS set.
