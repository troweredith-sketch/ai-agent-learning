import unittest

from pydantic import ValidationError

from src.todo_item import TodoItem


class TestTodoItem(unittest.TestCase):
    def test_todo_item_uses_defaults(self) -> None:
        todo = TodoItem(id=1, title="学习 Pydantic")

        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.title, "学习 Pydantic")
        self.assertFalse(todo.completed)
        self.assertIsNotNone(todo.created_at)

    def test_todo_item_converts_string_id_to_int(self) -> None:
        todo = TodoItem(id="2", title="完成练习")

        self.assertEqual(todo.id, 2)
        self.assertIsInstance(todo.id, int)

    def test_todo_item_rejects_empty_title(self) -> None:
        with self.assertRaises(ValidationError):
            TodoItem(id=3, title="")

    def test_todo_item_schema_contains_expected_fields(self) -> None:
        schema = TodoItem.model_json_schema()

        self.assertEqual(schema["type"], "object")
        self.assertIn("properties", schema)
        self.assertIn("title", schema["properties"])
        self.assertEqual(schema["properties"]["title"]["minLength"], 1)


if __name__ == "__main__":
    unittest.main()
