import os
import asyncio
import logging
from logging.handlers import RotatingFileHandler

from pyrogram import Client, idle
from pyromod import listen
import tgcrypto

from config import Config

# ---------------------------------------
#  Logging
# ---------------------------------------
LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    handlers=[
        RotatingFileHandler("log.txt", maxBytes=5_000_000, backupCount=10),
        logging.StreamHandler(),
    ]
)

# ---------------------------------------
#  Globals
# ---------------------------------------
AUTH_USERS = [int(x) for x in Config.AUTH_USERS.split(",") if x]
prefixes = ["/", "!", "?", "~"]

# ---------------------------------------
#  Bot Instance
# ---------------------------------------
bot = Client(
    "ExtractorBot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    sleep_threshold=20,
    plugins=dict(root="plugins"),
    workers=50
)

# ---------------------------------------
#  Start Bot
# ---------------------------------------
async def start_bot():
    await bot.start()
    me = await bot.get_me()
    LOGGER.info(f"Bot Started: @{me.username}")
    await idle()

if __name__ == "__main__":
    asyncio.run(start_bot())
