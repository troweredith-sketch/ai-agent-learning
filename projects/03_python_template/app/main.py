from dotenv import load_dotenv
from pydantic import BaseModel
import os
import requests

load_dotenv()


class AppConfig(BaseModel):
    app_env: str = "development"
    api_key: str = ""


def get_config() -> AppConfig:
    return AppConfig(
        app_env=os.getenv("APP_ENV", "development"),
        api_key=os.getenv("API_KEY", "")
    )


def main() -> None:
    config = get_config()
    print("当前环境：", config.app_env)
    print("API_KEY 是否已设置：", bool(config.api_key))

    response = requests.get("https://httpbin.org/get", timeout=10)
    print("请求状态码：", response.status_code)


if __name__ == "__main__":
    main()
