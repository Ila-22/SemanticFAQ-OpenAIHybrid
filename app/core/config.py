from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    openai_api_key: str
    embedding_model: str = "text-embedding-3-small"
    similarity_threshold: float = 0.82

    class Config:
        env_file = ".env"

settings = Settings()