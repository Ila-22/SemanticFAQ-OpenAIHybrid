from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as faq_router
from app.core.logger import get_logger

logger = get_logger(__name__)
app = FastAPI(title="Semantic FAQ API", version="1.0.0")

# Route registration
app.include_router(faq_router)

# Startup log
@app.on_event("startup")
def startup_event():
    logger.info("🚀 Semantic FAQ API is up and running!")

    
# Run the server: uvicorn main:app --reload
# Access it and ask a question: http://127.0.0.1:8000/docs
