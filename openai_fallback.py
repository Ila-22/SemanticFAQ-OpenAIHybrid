from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

"""
def get_openai_answer(user_question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": user_question}
        ]
    )
    return response.choices[0].message.content.strip()
"""

def get_openai_answer(user_question: str) -> str:
    # Fake response for local testing
    return "I'm a mock GPT. This is only a fake answer for your question."
