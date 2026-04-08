from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()


class AppConfig(BaseModel):
    app_name: str = "Python Template"
    app_env: str = "development"
    author: str = "we"


def load_config() -> AppConfig:
    return AppConfig(
        app_name=os.getenv("APP_NAME", "Python Template"),
        app_env=os.getenv("APP_ENV", "development"),
        author=os.getenv("AUTHOR", "we"),
    )