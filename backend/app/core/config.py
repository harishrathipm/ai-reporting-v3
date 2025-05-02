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