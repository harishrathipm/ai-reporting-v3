import os
from fastapi import FastAPI
from app.middleware.middleware import add_middlewares
from app.api.routes_config import include_routes

app = FastAPI(docs_url="/swagger")
add_middlewares(app)

# Include routes from routes_config
include_routes(app)
