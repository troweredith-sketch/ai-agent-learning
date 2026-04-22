from src.config import load_config
from src.utils import build_summary


def main() -> None:
    config = load_config()
    print(build_summary(config))


if __name__ == "__main__":
    main()
