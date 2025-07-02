from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL = "text-embedding-3-small"  # or -3-large

print(f"API Key loaded: {OPENAI_API_KEY [:5]}...")  # for debugging purposes :)