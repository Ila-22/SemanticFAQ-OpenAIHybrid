# a custom handler for RequestValidationError

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY, HTTP_500_INTERNAL_SERVER_ERROR
from app.core.logger import get_logger


logger = get_logger(__name__)

# Handles 422 Unprocessable Entity (validation errors)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning(f"Validation error on request {request.url}: {exc}")
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "detail": "Invalid input. Please check your request format and data.",
            "errors": exc.errors()
        },
    )

# Handles any uncaught exception (500 Internal Server Error)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An internal server error occurred. Please try again later."},
    )

# Exported dictionary for easy inclusion in FastAPI setup
exception_handlers = {
    RequestValidationError: validation_exception_handler,
    Exception: global_exception_handler,
}
