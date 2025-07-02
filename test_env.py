from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key loaded: {api_key[:5]}...")  # confirm it's working
print("test compeleted!")