from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from answer_router import route_question
import logging

# logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class QuestionRequest(BaseModel):
    user_question: str

@app.post("/ask-question")
def ask_question(request: QuestionRequest):
    logger.info(f"Incoming question: {request.user_question}")

    try:
        result = route_question(request.user_question)
        logger.info(f"Matched via: {result['source']} | Similarity Score: {result['score']:.4f}")
        return result
    except Exception as e:
        logger.error("Error while processing question", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


# Run the server: uvicorn main:app --reload
# Access it and ask a question: http://127.0.0.1:8000/docs
