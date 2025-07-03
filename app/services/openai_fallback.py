from langchain_openai import ChatOpenAI
from app.core.config import settings

llm = ChatOpenAI(
    model=settings.chat_model,
    temperature=0.0,
    api_key=settings.openai_api_key
)

def get_openai_answer(question: str) -> str:
    return llm.invoke(question).content


#def get_openai_answer(user_question: str) -> str:
    # Fake response for local testing
    #return "I'm a mock GPT. This is only a fake answer for your question."

