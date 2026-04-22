import unittest

from src.config import AppConfig
from src.utils import build_summary, mask_secret


class TestUtils(unittest.TestCase):
    def test_mask_secret_returns_placeholder_when_empty(self) -> None:
        self.assertEqual(mask_secret(""), "未配置")

    def test_mask_secret_masks_long_secret(self) -> None:
        self.assertEqual(mask_secret("abcdefgh12345678"), "abcd...5678")

    def test_build_summary_includes_model_name(self) -> None:
        config = AppConfig(
            app_name="Demo App",
            app_env="development",
            app_debug=True,
            api_timeout=30,
            model_name="gpt-4.1-mini",
            openai_api_key="abcdefgh12345678",
        )

        summary = build_summary(config)

        self.assertIn("模型名称: gpt-4.1-mini", summary)
        self.assertIn("API 超时时间: 30 秒", summary)


if __name__ == "__main__":
    unittest.main()
