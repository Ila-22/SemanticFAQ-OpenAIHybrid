from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from app.core.config import settings

# LLM to use
llm = ChatOpenAI(temperature=0.0, openai_api_key=settings.openai_api_key)

# Prompt to classify the question
classification_prompt = PromptTemplate(
    input_variables=["question"],
    template="""
            You are a classifier that determines if a question is IT-related and appropriate for an internal FAQ system.

            If the question is about IT topics (software, hardware, networks, SaaS tools, tech issues), respond with "IT".
            If not, respond with "COMPLIANCE".

            Question: {question}
            Answer (IT or COMPLIANCE):
            """.strip()
)

# Combine using LangChain Expression Language (LCEL)
router_chain = classification_prompt | llm

def classify_question(question: str) -> str:
    """
    Mocked version: classifies based on keywords without calling OpenAI.
    """
    try:
        response = router_chain.invoke({"question": question})
        classification = response.content.strip().upper()
        if classification not in {"IT", "COMPLIANCE"}:
            classification = "COMPLIANCE"  # Default fallback
        return classification
    except Exception as e:
        print(f"[Router] Error classifying question: {e}")
        return "COMPLIANCE"
    
