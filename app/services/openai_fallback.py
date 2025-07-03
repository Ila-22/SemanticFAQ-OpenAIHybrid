from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from app.core.config import settings

llm = ChatOpenAI(
    model="gpt-4o",
    openai_api_key=settings.openai_api_key
)

def get_openai_answer(user_question: str) -> str:
    # Fake response for local testing
    return "I'm a mock GPT. This is only a fake answer for your question."


"""
def get_openai_answer(user_question: str) -> str:
    response = llm.invoke([HumanMessage(content=user_question)])
    return response.content.strip()
"""
