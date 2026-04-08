from src.config import load_config
from src.utils import build_message


def main() -> None:
    config = load_config()
    message = build_message(config.app_name, config.app_env, config.author)
    print(message)


if __name__ == "__main__":
    main()