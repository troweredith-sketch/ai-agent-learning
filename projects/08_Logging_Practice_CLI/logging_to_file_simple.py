import logging
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "app.log"


# 把日志写入文件
# filename 表示写到哪个文件
# 这里固定写到脚本所在目录，避免从别的目录运行时把日志写到仓库根目录
# filemode="a" 表示追加写入，不覆盖旧内容
# encoding="utf-8" 表示支持中文
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    filename=str(LOG_FILE),
    filemode="a",
    encoding="utf-8",
)


print("程序开始运行。")

logging.info("这是一条 info 日志。")
logging.warning("这是一条 warning 日志。")
logging.error("这是一条 error 日志。")

print(f"日志已经写入 {LOG_FILE}")
