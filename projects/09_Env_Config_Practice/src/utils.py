from src.config import AppConfig


def mask_secret(secret: str) -> str:
    if not secret:
        return "未配置"

    if len(secret) <= 8:
        return "*" * len(secret)

    return f"{secret[:4]}...{secret[-4:]}"


def build_summary(config: AppConfig) -> str:
    masked_key = mask_secret(config.openai_api_key)
    key_status = "是" if config.openai_api_key else "否"

    return "\n".join(
        [
            f"应用名称: {config.app_name}",
            f"运行环境: {config.app_env}",
            f"调试模式: {config.app_debug}",
            f"API 超时时间: {config.api_timeout} 秒",
            f"模型名称: {config.model_name}",
            f"OPENAI_API_KEY: {masked_key}",
            f"是否已配置密钥: {key_status}",
        ]
    )
