from pydantic_settings import BaseSettings
import logging
import reprlib


class Settings(BaseSettings):
    openai_api_key: str
    embedding_model: str = "text-embedding-3-small"
    chat_model: str = "gpt-4o"
    similarity_threshold: float = 0.75

    class Config:
        env_file = ".env"  # Pydantic will load this automatically

settings = Settings()

print(f">>>>>>>>> Raw API key: {repr(settings.openai_api_key)}")
#settings.openai_api_key = settings.openai_api_key.strip()

# debugging API key
logger = logging.getLogger(__name__)
logger.debug(f"OPENAI_API_KEY (partial): {reprlib.repr(settings.openai_api_key)}")