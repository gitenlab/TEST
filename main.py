from loguru import logger
import urllib3
import sys
import asyncio
import platform

from process import start
        import src


# SETTING POLICY FOR WINDOWS
# config = src.utils.get_config()
# using_playwright = 'faucet' in str(config.FLOW.TASKS) or 'dusted' in str(config.FLOW.TASKS)


# if not using_playwright:
# if platform.system() == "Windows":
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
