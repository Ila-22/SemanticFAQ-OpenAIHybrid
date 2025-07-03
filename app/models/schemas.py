from pydantic import BaseModel, Field

class QuestionRequest(BaseModel):
    user_question: str = Field(..., example="How do I change my password?")

class QuestionResponse(BaseModel):
    source: str = Field(..., example="local")  # or "openai"
    matched_question: str = Field(..., example="How can I change my password?")
    answer: str = Field(..., example="Go to settings > password and follow the steps.")
    score: float = Field(..., example=0.89)
