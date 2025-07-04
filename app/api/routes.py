from fastapi import APIRouter, HTTPException, Depends
from app.models.schemas import QuestionRequest, QuestionResponse
from app.services.router import route_question
from app.core.auth import get_token
from app.core.logger import get_logger

router = APIRouter()
logger = get_logger(__name__)

@router.post("/ask-question", response_model=QuestionResponse)

def ask_question(payload: QuestionRequest, token: str = Depends(get_token)):
    """
    Handles a user question and returns an appropriate answer.

    - Matches the question to a semantically similar FAQ entry.
    - Falls back to OpenAI if similarity is low.
    - Requires valid authentication via Bearer token.
    """
    try:
        logger.info(f"Received question: {payload.user_question}")
        result = route_question(payload.user_question)
        score = result.get("score")
        if score is not None:
            logger.info(f"Matched via: {result['source']} | Score: {score:.4f}")
        else:
            logger.info(f"Matched via: {result['source']}")
        return QuestionResponse(**result)
    except Exception as e:
        logger.error(f"Failed to process question: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error.")
