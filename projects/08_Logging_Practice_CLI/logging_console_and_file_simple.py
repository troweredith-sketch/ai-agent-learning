import logging
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "app_both.log"


# handlers 表示日志要发到哪些地方
# StreamHandler(sys.stdout) 表示发到屏幕
# FileHandler(...) 表示写到文件
# 这里固定写到脚本所在目录，避免从别的目录运行时把日志写到仓库根目录
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
    ],
)


print("程序开始运行。")

logging.info("这是一条 info 日志。")
logging.warning("这是一条 warning 日志。")
logging.error("这是一条 error 日志。")

print(f"日志已经同时输出到屏幕和 {LOG_FILE}")
