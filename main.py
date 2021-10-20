import disnake
import os
import alive

from disnake.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient

bot = commands.Bot(
  command_prefix="s!", 
  intents=disnake.Intents.all(),
  test_guilds=[817437132397871135]
)

@bot.event
async def on_ready():
  print("im on!")
  
cogs = ["cogs.welcome", "jishaku"]

for i in cogs:
  bot.load_extension(i)
  
alive.keep_alive()
bot.run(os.environ['TOKEN'])