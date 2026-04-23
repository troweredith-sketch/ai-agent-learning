from pprint import pprint

from pydantic import ValidationError

from src.todo_item import TodoItem


def print_section(title: str) -> None:
    print(f"\n=== {title} ===")


def show_valid_example() -> None:
    print_section("1. 正常创建 TodoItem")
    todo = TodoItem(id=1, title="学习 Pydantic")
    print(todo)
    pprint(todo.model_dump())


def show_type_conversion() -> None:
    print_section("2. 观察类型转换")
    todo = TodoItem(id="2", title="完成今日笔记")
    print(f"id: {todo.id}, type: {type(todo.id).__name__}")


def show_validation_error() -> None:
    print_section("3. 观察校验失败")
    try:
        TodoItem(id=3, title="")
    except ValidationError as exc:
        print(exc)


def show_schema() -> None:
    print_section("4. 查看 schema")
    pprint(TodoItem.model_json_schema())


def main() -> None:
    show_valid_example()
    show_type_conversion()
    show_validation_error()
    show_schema()


if __name__ == "__main__":
    main()
