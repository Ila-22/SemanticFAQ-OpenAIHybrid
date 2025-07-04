from langchain_openai import ChatOpenAI
from app.core.config import settings

llm = ChatOpenAI(
    model=settings.chat_model,
    temperature=0.0,
    api_key=settings.openai_api_key
)

def get_openai_answer(question: str) -> str:
    return llm.invoke(question).content



