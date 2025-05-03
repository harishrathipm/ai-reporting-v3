from dotenv import load_dotenv
import os

class Config:
    # Determine the environment file based on the ENV variable
    ENV = os.getenv("ENV", "development")
    print(f"Environment: {os.getenv('ENV', 'development')}")
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Update the environment file path to include the core directory
    if ENV == "production":
        env_file = os.path.join(base_dir, ".env.prod")
    elif ENV == "staging":
        env_file = os.path.join(base_dir, ".env.staging")
    else:
        env_file = os.path.join(base_dir, ".env.dev")
    print(f"Loading environment file: {env_file}")
    load_dotenv(env_file)

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    TEMP_DB_NAME = os.getenv("TEMP_DB_NAME", "temp_db")
    META_DB_NAME = os.getenv("META_DB_NAME", "meta_db")
    SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL", "sqlite:///./test.db")