import sys
import asyncio
import importlib
import logging
import threading
import config
from ShrutiCHATBOT import ID_CHATBOT
from pyrogram import idle
from pyrogram.types import BotCommand
from config import OWNER_ID
from ShrutiCHATBOT import LOGGER, ShrutiCHATBOT, userbot, load_clone_owners
from ShrutiCHATBOT.modules import ALL_MODULES
#from ShrutiCHATBOT.modules.Clone import restart_bots
#from ShrutiCHATBOT.modules.Id_Clone import restart_idchatbots

from colorama import Fore, Style, init
init(autoreset=True)

class CustomFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: Fore.CYAN + "🐞 [DEBUG] " + Style.RESET_ALL + "%(message)s",
        logging.INFO: Fore.GREEN + "ℹ️ [INFO] " + Style.RESET_ALL + "%(message)s",
        logging.WARNING: Fore.YELLOW + "⚠️ [WARNING] " + Style.RESET_ALL + "%(message)s",
        logging.ERROR: Fore.RED + "❌ [ERROR] " + Style.RESET_ALL + "%(message)s",
        logging.CRITICAL: Fore.MAGENTA + "💥 [CRITICAL] " + Style.RESET_ALL + "%(message)s",
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

handler = logging.StreamHandler()
handler.setFormatter(CustomFormatter())
LOGGER.addHandler(handler)
LOGGER.setLevel(logging.INFO)

async def anony_boot():
    try:
        await ShrutiCHATBOT.start()
        try:
            await ShrutiCHATBOT.send_message(
                int(OWNER_ID),
                f"✨ {ShrutiCHATBOT.mention} is now <b>Alive & Running ✅</b>"
            )
            LOGGER.info(f"🚀 @{ShrutiCHATBOT.username} Started Successfully ✅")
        except Exception:
            LOGGER.warning(f"⚡ Please start @{ShrutiCHATBOT.username} from the owner account.")

        asyncio.create_task(restart_bots())
        asyncio.create_task(restart_idchatbots())
        await load_clone_owners()

        if config.STRING1:
            try:
                await userbot.start()
                try:
                    await ShrutiCHATBOT.send_message(int(OWNER_ID), "🤖 Id-Chatbot Also Started ✅")
                    LOGGER.info("🤖 Id-Chatbot started successfully ✅")
                except Exception:
                    LOGGER.warning("⚡ Please start Id-Chatbot from the owner account.")
            except Exception as ex:
                LOGGER.error(f"❌ Error in starting Id-Chatbot :- {ex}")
    except Exception as ex:
        LOGGER.critical(f"🔥 Bot failed to start: {ex}")

    # ✅ Module Loader
    for all_module in ALL_MODULES:
        importlib.import_module("ShrutiCHATBOT.modules." + all_module)
        LOGGER.info(f"📦 Loaded Module: {Fore.CYAN}{all_module}{Style.RESET_ALL}")


    LOGGER.info(f"🎉 @{ShrutiCHATBOT.username} is fully up & running! 🚀")
    await idle()


# 🚀 Start Point
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("🛑 Stopping ShrutiCHATBOT Bot...")
