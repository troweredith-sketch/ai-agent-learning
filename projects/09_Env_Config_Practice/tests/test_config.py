import unittest
from unittest.mock import patch

from src.config import load_config, parse_bool


class TestConfig(unittest.TestCase):
    def test_parse_bool_returns_true_for_true_like_values(self) -> None:
        self.assertTrue(parse_bool("true"))
        self.assertTrue(parse_bool("YES"))
        self.assertTrue(parse_bool("1"))

    def test_parse_bool_returns_false_for_false_like_values(self) -> None:
        self.assertFalse(parse_bool("false"))
        self.assertFalse(parse_bool("0"))
        self.assertFalse(parse_bool(None))

    def test_load_config_reads_timeout_and_model_name(self) -> None:
        with patch.dict(
            "os.environ",
            {
                "APP_NAME": "Demo App",
                "APP_ENV": "development",
                "APP_DEBUG": "true",
                "API_TIMEOUT": "45",
                "MODEL_NAME": "gpt-4.1-mini",
                "OPENAI_API_KEY": "",
            },
            clear=False,
        ):
            config = load_config()

        self.assertEqual(config.app_name, "Demo App")
        self.assertEqual(config.app_env, "development")
        self.assertTrue(config.app_debug)
        self.assertEqual(config.api_timeout, 45)
        self.assertEqual(config.model_name, "gpt-4.1-mini")

    def test_load_config_raises_error_when_production_key_missing(self) -> None:
        with patch.dict(
            "os.environ",
            {
                "APP_ENV": "production",
                "OPENAI_API_KEY": "   ",
            },
            clear=False,
        ):
            with self.assertRaises(ValueError):
                load_config()


if __name__ == "__main__":
    unittest.main()
