from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as faq_router
from app.core.logger import get_logger
from contextlib import asynccontextmanager

logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Semantic FAQ API is up and running!")
    yield
    logger.info("🛑 Semantic FAQ API is shutting down.")

app = FastAPI(
    title="Semantic FAQ API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(faq_router)


# Run the server: uvicorn app.main:app --reload
# Access it and ask a question: http://127.0.0.1:8000/docs
