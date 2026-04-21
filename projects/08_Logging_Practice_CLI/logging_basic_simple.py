import logging
import sys


# 配置最基础的日志输出
# level=logging.INFO 表示显示 INFO、WARNING、ERROR
# format 表示日志显示成什么样子
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stdout,
)


print("这是 print 输出，主要是给用户看的。")

logging.info("程序开始运行。")
logging.warning("这是一个 warning 示例。")
logging.error("这是一个 error 示例。")

print("程序结束。")
