from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from app.api.routes import router as faq_router
from app.core.logger import get_logger
from app.core.exception_handlers import exception_handlers


logger = get_logger(__name__)

# Lifespan event handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Semantic FAQ API is up and running!")
    yield
    logger.info("🛑 Semantic FAQ API is shutting down.")


# FastAPI app instance
app = FastAPI(
    title="Semantic FAQ API",
    version="1.0.0",
    lifespan=lifespan
)

# Register global exception handler
for exc_class, handler in exception_handlers.items():
    app.add_exception_handler(exc_class, handler)
    

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(faq_router)


# Run the server: uvicorn app.main:app --reload
# Access it and ask a question: http://127.0.0.1:8000/docs
