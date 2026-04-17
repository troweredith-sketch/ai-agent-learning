"""Week 2 Day 2: exception handling practice script."""


class UserInputError(ValueError):
    """Raised when user input does not meet the program rules."""


def parse_name(raw: str) -> str:
    """Validate and return a cleaned name."""
    name = raw.strip()

    if not name:
        raise UserInputError("姓名不能为空，请至少输入 1 个字符。")

    if len(name) < 2:
        raise UserInputError("姓名至少需要 2 个字符，方便观察输入校验。")

    return name


def parse_age(raw: str) -> int:
    """Validate and return age as an integer."""
    text = raw.strip()

    if not text:
        raise UserInputError("年龄不能为空。")

    try:
        age = int(text)
    except ValueError:
        raise UserInputError("年龄必须是整数，例如 18。")

    if age <= 0 or age > 120:
        raise UserInputError("年龄不合理，请输入 1 到 120 之间的整数。")

    return age


def parse_score(raw: str) -> float:
    """Validate and return score as a float."""
    text = raw.strip()

    if not text:
        raise UserInputError("成绩不能为空。")

    try:
        score = float(text)
    except ValueError:
        raise UserInputError("成绩必须是数字，例如 89.5。")

    if not 0 <= score <= 100:
        raise UserInputError("成绩必须在 0 到 100 之间。")

    return score


def parse_divisor(raw: str) -> float:
    """Validate and return divisor as a float."""
    text = raw.strip()

    if not text:
        raise UserInputError("除数不能为空。")

    try:
        divisor = float(text)
    except ValueError:
        raise UserInputError("除数必须是数字，例如 2 或 0.5。")

    if divisor == 0:
        raise UserInputError("除数不能为 0，否则会触发除零错误。")

    return divisor


def prompt_until_valid(prompt: str, parser):
    """Keep asking for input until the parser accepts it."""
    while True:
        raw = input(prompt)
        try:
            return parser(raw)
        except UserInputError as exc:
            print(f"[输入错误] {exc}")
            print("请再试一次。\n")


def calculate_result(score: float, divisor: float) -> float:
    """Calculate a simple derived result."""
    return score / divisor


def main() -> None:
    """Run the interactive practice program."""
    print("=== 异常处理练习脚本 ===")
    print("你可以故意输入错误，观察程序如何进行健壮处理。\n")

    name = prompt_until_valid("请输入姓名: ", parse_name)
    age = prompt_until_valid("请输入年龄: ", parse_age)
    score = prompt_until_valid("请输入成绩(0-100): ", parse_score)
    divisor = prompt_until_valid("请输入除数(不能为 0): ", parse_divisor)

    result = calculate_result(score, divisor)

    print("\n=== 输入结果 ===")
    print(f"姓名: {name}")
    print(f"年龄: {age}")
    print(f"成绩: {score}")
    print(f"成绩 / 除数 = {result:.2f}")
    print("\n程序完成，没有因为错误输入而直接崩溃。")


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print("\n检测到输入提前结束，程序已退出。")
    except KeyboardInterrupt:
        print("\n用户主动取消了程序。")
