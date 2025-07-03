from fastapi import APIRouter, HTTPException
from app.models.schemas import QuestionRequest, QuestionResponse
from app.services.router import route_question
from app.core.logger import get_logger

router = APIRouter()
logger = get_logger(__name__)

@router.post("/ask-question", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):
    logger.info(f"Received question: {request.user_question}")

    try:
        result = route_question(request.user_question)
        logger.info(f"Matched via: {result['source']} | Score: {result['score']:.4f}")
        return QuestionResponse(**result)
    except Exception as e:
        logger.error(f"Failed to process question: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error.")
