import disnake
from disnake.ext import commands
import datetime

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.slash_command(description="a complete view of the bot's features and commands.")
    async def give(self, inter):
        return

def setup(bot):
	bot.add_cog(Owner(bot))