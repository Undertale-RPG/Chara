import disnake
from disnake.ext import commands, tasks

class Announce(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command()
	async def test(self, inter):
		await inter.send("test")

	#@commands.has_role(1023724498060578876)
	@commands.slash_command()
	async def announce(self, inter, name: str, when: str, hosts: disnake.User, description: str, rules: str, prize:str=None):

		em = disnake.Embed(
			title=name,
			color=0x0077ff,
			description=f"""
			**When:** {when}
			**Hosts:** {hosts.mention}
			"""
		)
		em.add_field(name="Description of the event:", value=description, inline=False)
		em.add_field(name="Event Rules:", value=f"""
		{rules}
		All server rules still apply
		**Breaking any of the above rules will get you kicked out from the event and a warning**
		""", inline=False)
		em.add_field(name="Prize:", value=prize, inline=False)

		await inter.followup(embed=em)
    

def setup(bot):
	bot.add_cog(Announce(bot))