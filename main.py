import nextcord
from nextcord.ext import commands

import logging
from sys import stdout
import os

import dotenv

bot = commands.Bot(intents=nextcord.Intents.default(), command_prefix="!")


@bot.event
async def on_ready():
    logging.info("Logged in as {0.user}!".format(bot))


if __name__ == "__main__":
    # Load environment variables
    dotenv.load_dotenv()

    # Setup basic logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.StreamHandler(stdout)
        ]
    )

    # Load all extensions
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            logging.info(f"Registering cog {file[:-3]}...")
            bot.load_extension(f"cogs.{file[:-3]}")

    # Run the bot
    bot.run(os.getenv("DISCORD_TOKEN"))
