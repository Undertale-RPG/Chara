import disnake
import os
import alive

from disnake.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient

class Spamton(commands.Bot):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.MongoUrl = os.environ["MongoUrl"]
    self.cluster = AsyncIOMotorClient(self.MongoUrl)
    self.db = self.cluster["database"]
    self.boosters = self.db["boosters"]
    
bot = Spamton(
  command_prefix="s!", 
  intents=disnake.Intents.all(),
  test_guilds=[817437132397871135],
  sync_commands_debug=True
)
  
cogs = ["cogs.welcome", "jishaku"]

for i in cogs:
  bot.load_extension(i)
  
alive.keep_alive()
bot.run(os.environ['TOKEN'])