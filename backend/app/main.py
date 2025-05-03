import logging
from fastapi import FastAPI
from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.middleware.middleware import add_middlewares
from app.api.routes_config import include_routes

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(docs_url="/swagger")
add_middlewares(app)

# MongoDB connection for temporary storage
mongo_client = MongoClient("mongodb://localhost:27017")
temp_db = mongo_client["temp_db"]

# SQLAlchemy setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Replace with your database URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.on_event("startup")
def startup_event():
    """Initialize database connections."""
    logging.info("Connecting to SQL and MongoDB databases...")
    # Test SQLAlchemy connection
    try:
        with engine.connect() as connection:
            logging.info("SQL database connected successfully.")
    except Exception as e:
        logging.error(f"Failed to connect to SQL database: {e}")

    # Test MongoDB connection
    try:
        mongo_client.admin.command('ping')
        logging.info("MongoDB connected successfully.")
    except Exception as e:
        logging.error(f"Failed to connect to MongoDB: {e}")


# Include routes from routes_config
include_routes(app)
