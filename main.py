from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from answer_router import route_question

app = FastAPI()

class QuestionRequest(BaseModel):
    user_question: str

@app.post("/ask-question")
def ask_question(request: QuestionRequest):
    try:
        result = route_question(request.user_question)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Run the server: uvicorn main:app --reload
# Access it and ask a question: http://127.0.0.1:8000/docs
