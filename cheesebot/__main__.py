import asyncio
import logging
import sys
from pathlib import Path

from bot import CheeseBot


def load_token() -> str:
    with open(
        Path(__file__).parent.parent / ".token", "r", encoding="utf-8"
    ) as fp:
        return fp.read().strip()


async def main():
    # Setup logging
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(
        filename='discord.log', encoding='utf-8', mode='w'
    )
    fmt_str = "[%(asctime)s] [%(levelname)s] %(message)s"
    datefmt_str = "%Y-%m-%d %H:%M:%S"
    handler.setFormatter(logging.Formatter(fmt_str, datefmt_str))
    logger.addHandler(handler)

    # Construct the bot
    cogs = (
        "sys",
    )
    if len(sys.argv) >= 2:
        cogs = sys.argv[1].split(",")
        cogs = [i.strip() for i in cogs if i]

    cheese_bot = CheeseBot(cogs)
    cheese_bot.setup()
    await cheese_bot.start(load_token())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.warning("Killed the Bot by raising KeyboardInterrupt.")
    except Exception:
        logging.exception("Uncatched Exception occurred.")
        raise