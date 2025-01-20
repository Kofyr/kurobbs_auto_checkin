import os

import requests
from loguru import logger


def send_bark_notification(message):
    """Send a notification via Bark."""
    bark_device_key = os.getenv("BARK_DEVICE_KEY")
    bark_server_url = os.getenv("BARK_SERVER_URL")

    if not bark_device_key or not bark_server_url:
        logger.warning("Bark secrets are not set. Skipping notification.")
        return

    # 构造 Bark API URL
    title = "库街区自动签到任务"
    url = f"{bark_server_url}/{bark_device_key}/{title}/{message}"
    try:
        requests.get(url)
    except Exception:
        pass
