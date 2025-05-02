import logging
from fastapi import FastAPI
from app.middleware.middleware import add_middlewares
from app.api.routes_config import include_routes

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(docs_url="/swagger")
add_middlewares(app)

# Include routes from routes_config
include_routes(app)
