from dotenv import load_dotenv
import os

class Config:
    # Determine the environment file based on the ENV variable
    ENV = os.getenv("ENV", "development")
    if ENV == "production":
        env_file = ".env.prod"
    elif ENV == "staging":
        env_file = ".env.staging"
    else:
        env_file = ".env.dev" 
    print(f"Loading environment file: {env_file}")
    load_dotenv(env_file)

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")