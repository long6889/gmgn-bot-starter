import os
from pathlib import Path


class Settings:
    """Simple and robust settings loader for GMGN bot that works on Windows, macOS, and Linux."""

    def __init__(self):
        self.base_url = "https://api.gmgn.ai"
        self.api_key = "your_api_key_here"
        self.timeout = 30
        
        # Load from .env file first
        self._load_from_env_file()
        
        # Override with environment variables if present
        self._load_from_environment()

    def _load_from_env_file(self):
        """Read .env file from project root."""
        env_file = Path(__file__).resolve().parent.parent / ".env"
        
        if env_file.exists():
            try:
                for line in env_file.read_text(encoding="utf-8").splitlines():
                    raw = line.strip()
                    # Skip comments and empty lines
                    if not raw or raw.startswith("#") or "=" not in raw:
                        continue
                    
                    key, value = raw.split("=", 1)
                    key = key.strip()
                    value = value.strip()
                    
                    if key == "GMGN_BASE_URL":
                        self.base_url = value
                    elif key == "GMGN_API_KEY":
                        self.api_key = value
                    elif key == "GMGN_TIMEOUT":
                        try:
                            self.timeout = int(value)
                        except (ValueError, TypeError):
                            self.timeout = 30
            except Exception as e:
                print(f"[WARN] Failed to read .env file: {e}")

    def _load_from_environment(self):
        """Override with OS environment variables if they exist."""
        if "GMGN_BASE_URL" in os.environ:
            self.base_url = os.environ["GMGN_BASE_URL"]
        
        if "GMGN_API_KEY" in os.environ:
            self.api_key = os.environ["GMGN_API_KEY"]
        
        if "GMGN_TIMEOUT" in os.environ:
            try:
                self.timeout = int(os.environ["GMGN_TIMEOUT"])
            except (ValueError, TypeError):
                self.timeout = 30


# Global settings instance
settings = Settings()
