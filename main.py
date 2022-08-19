import os
import disnake
from dotenv import load_dotenv
from disnake.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

description = """The undertale RPG Beta bot."""

intents = disnake.Intents.default()
intents.members = True
intents.message_content = True

class SpamtonBot(commands.AutoShardedBot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.BotToken = os.getenv("TOKEN")
        self.vote_url = "https://top.gg/bot/815153881217892372"
        self.activity = disnake.Game("Together with all of you")
        self.help_command = None
        self.MongoUrl = os.getenv("MONGO_URL")
        self.cluster = AsyncIOMotorClient(self.MongoUrl)
        self.db = self.cluster["database"]
        self.boosters = self.db["boosters"]

    def load_all_cogs(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and not filename.startswith("_"):
                self.load_extension(f"cogs.{filename[:-3]}")
                print(f"🔁 cogs.{filename[:-3]} is loaded and ready.")
        return


bot = SpamtonBot(
    description=description,
    intents=intents,
    owner_ids=[536538183555481601, 513351917481623572]
)


bot.load_all_cogs()
bot.run(bot.BotToken)