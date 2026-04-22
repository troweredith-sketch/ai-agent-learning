import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

# Load local environment variables from the project root.
load_dotenv(dotenv_path=ENV_FILE)


@dataclass
class AppConfig:
    app_name: str
    app_env: str
    app_debug: bool
    api_timeout: int
    model_name: str
    openai_api_key: str


def parse_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default

    normalized = value.strip().lower()
    return normalized in {"1", "true", "yes", "on"}


def load_config() -> AppConfig:
    app_name = os.getenv("APP_NAME", "Env Config Practice")
    app_env = os.getenv("APP_ENV", "development").strip().lower()
    app_debug = parse_bool(os.getenv("APP_DEBUG"), default=False)
    api_timeout = int(os.getenv("API_TIMEOUT", "30"))
    model_name = os.getenv("MODEL_NAME", "gpt-4.1-mini").strip()
    openai_api_key = os.getenv("OPENAI_API_KEY", "").strip()

    if app_env == "production" and not openai_api_key:
        raise ValueError("APP_ENV=production 时，必须配置 OPENAI_API_KEY。")

    return AppConfig(
        app_name=app_name,
        app_env=app_env,
        app_debug=app_debug,
        api_timeout=api_timeout,
        model_name=model_name,
        openai_api_key=openai_api_key,
    )