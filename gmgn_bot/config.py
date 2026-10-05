from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration for GMGN Bot"""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )

    base_url: str = Field(
        default="https://api.gmgn.ai",
        validation_alias=AliasChoices("GMGN_BASE_URL", "base_url"),
    )
    api_key: str = Field(
        default="your_api_key_here",
        validation_alias=AliasChoices("GMGN_API_KEY", "api_key"),
    )
    timeout: int = Field(
        default=30,
        validation_alias=AliasChoices("GMGN_TIMEOUT", "timeout"),
    )


settings = Settings()
