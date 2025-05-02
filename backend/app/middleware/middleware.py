from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ErrorLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as exc:
            logger.error(f"Error occurred: {exc}", exc_info=True)
            return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

def add_middlewares(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allow all origins temporarily
        allow_credentials=True,
        allow_methods=["*"],  # Allow all HTTP methods
        allow_headers=["*"],  # Allow all headers
    )
    app.add_middleware(ErrorLoggingMiddleware)