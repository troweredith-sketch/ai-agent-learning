"""Week 2 Day 3: logging practice CLI.

Practice ideas:
1. Enter an invalid age once to trigger a warning log.
2. Choose "y" when asked about simulating a file save failure to trigger an error log.
3. Open logs/logging_practice.log after running and compare it with the console output.
4. Change logging.INFO to logging.WARNING and rerun to observe the difference.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Callable, TypeVar

T = TypeVar("T")

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "logging_practice.log"
REPORT_FILE = BASE_DIR / "practice_result.txt"

logger = logging.getLogger(__name__)


def setup_logging(enable_file_logging: bool = True) -> None:
    """Configure logging for console output and optional file output."""
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.handlers.clear()

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    if enable_file_logging:
        LOG_DIR.mkdir(exist_ok=True)
        file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)


def parse_name(raw: str) -> str:
    """Validate and return a cleaned name."""
    name = raw.strip()
    if len(name) < 2:
        raise ValueError("姓名至少输入 2 个字符。")
    return name


def parse_age(raw: str) -> int:
    """Validate and return age as an integer."""
    text = raw.strip()
    if not text:
        raise ValueError("年龄不能为空。")

    try:
        age = int(text)
    except ValueError as exc:
        raise ValueError("年龄必须是整数，例如 18。") from exc

    if not 1 <= age <= 120:
        raise ValueError("年龄必须在 1 到 120 之间。")

    return age


def parse_score(raw: str) -> float:
    """Validate and return score as a float."""
    text = raw.strip()
    if not text:
        raise ValueError("成绩不能为空。")

    try:
        score = float(text)
    except ValueError as exc:
        raise ValueError("成绩必须是数字，例如 88.5。") from exc

    if not 0 <= score <= 100:
        raise ValueError("成绩必须在 0 到 100 之间。")

    return score


def prompt_until_valid(
    prompt: str,
    parser: Callable[[str], T],
    field_name: str,
) -> T:
    """Keep asking for input until the parser accepts it."""
    while True:
        raw = input(prompt)
        try:
            value = parser(raw)
        except ValueError as exc:
            logger.warning(
                "Field validation failed: %s raw=%r error=%s",
                field_name,
                raw,
                exc,
            )
            print(f"[输入错误] {exc}")
            print("请再试一次。\n")
            continue

        logger.info("Field validation passed: %s=%s", field_name, value)
        return value


def prompt_yes_no(prompt: str) -> bool:
    """Prompt until the user enters y or n."""
    while True:
        raw = input(prompt).strip().lower()

        if raw in {"y", "yes"}:
            logger.info("User chose to simulate a file save error.")
            return True

        if raw in {"n", "no"}:
            logger.info("User chose normal file saving.")
            return False

        logger.warning("Invalid yes/no input: raw=%r", raw)
        print("请输入 y 或 n。\n")


def build_summary(name: str, age: int, score: float) -> str:
    """Build a short summary for the current practice run."""
    return (
        "姓名: {name}\n"
        "年龄: {age}\n"
        "成绩: {score:.1f}\n"
        "状态: 已完成一次 logging 基础练习"
    ).format(name=name, age=age, score=score)


def save_summary(summary: str, simulate_error: bool) -> Path:
    """Write the practice summary to a file.

    When simulate_error is True, this intentionally writes to a missing
    directory so you can observe an error log.
    """
    output_path = REPORT_FILE

    if simulate_error:
        output_path = BASE_DIR / "missing_dir" / "practice_result.txt"

    output_path.write_text(summary + "\n", encoding="utf-8")
    return output_path


def main() -> None:
    """Run the interactive logging practice program."""
    logger.info("Logging practice script started.")

    print("=== logging 练习脚本 ===")
    print("这个脚本会同时演示 print 和 logging 的区别。")
    print(f"日志文件默认输出到: {LOG_FILE}")
    print("你可以故意输错一次年龄，观察 warning 日志。")
    print("你也可以选择模拟文件保存失败，观察 error 日志。\n")

    name = prompt_until_valid("请输入姓名: ", parse_name, "name")
    age = prompt_until_valid("请输入年龄: ", parse_age, "age")
    score = prompt_until_valid("请输入成绩(0-100): ", parse_score, "score")

    summary = build_summary(name, age, score)

    simulate_error = prompt_yes_no(
        "是否模拟一次文件保存失败，观察 error 日志? (y/n): "
    )

    try:
        report_path = save_summary(summary, simulate_error)
    except OSError as exc:
        logger.error("Failed to save practice summary: %s", exc)
        print("\n[保存失败] 结果文件没有写入成功，请查看日志。")
    else:
        logger.info("Practice summary saved successfully: %s", report_path)
        print("\n[保存成功] 练习结果已写入文件。")
        print(f"结果文件路径: {report_path}")

    print("\n=== 本次输入结果 ===")
    print(summary)

    logger.info("Logging practice script finished.")


if __name__ == "__main__":
    setup_logging(enable_file_logging=True)

    try:
        main()
    except EOFError:
        logger.error("Input stream ended early.")
        print("\n检测到输入提前结束，程序已退出。")
    except KeyboardInterrupt:
        logger.warning("User cancelled the program.")
        print("\n用户主动取消了程序。")
