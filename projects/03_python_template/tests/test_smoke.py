import unittest
from src.utils import build_message


class TestUtils(unittest.TestCase):
    def test_build_message(self):
        message = build_message("DemoApp", "dev", "we")
        self.assertIn("DemoApp", message)
        self.assertIn("dev", message)
        self.assertIn("we", message)


if __name__ == "__main__":
    unittest.main()