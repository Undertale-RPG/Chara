import disnake
from disnake.ext import commands, tasks

class Announce(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.boost_stats.start()

	@commands.has_role(1023724498060578876)
	@commands.command()
	async def announce(self, inter):
		return
    

def setup(bot):
	bot.add_cog(Announce(bot))