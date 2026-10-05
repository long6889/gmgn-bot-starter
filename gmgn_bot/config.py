from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuration for GMGN Bot"""

    base_url: str = "https://api.gmgn.ai"
    api_key: str = "your_api_key_here"
    timeout: int = 30

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
