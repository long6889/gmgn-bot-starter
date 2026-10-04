from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("GMGN_BASE_URL", "https://api.gmgn.ai")
    api_key: str = os.getenv("GMGN_API_KEY", "")
    timeout: int = int(os.getenv("GMGN_TIMEOUT", "30"))


settings = Settings()
