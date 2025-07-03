import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
print("Using key:", repr(openai.api_key))

try:
    response = openai.Client().models.list()
    print("✅ Success:", response)
except Exception as e:
    print("❌ Error:", e)
