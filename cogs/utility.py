import disnake
from disnake.ext import commands


class Utility(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(description="List of all our team members")
	@commands.cooldown(1, 12, commands.BucketType.user)
	async def team(self, inter):
		guild = self.bot.get_guild(inter.guild.id)
		admins = guild.get_role(849635343891955802)
		managers = guild.get_role(989189354847109122)
		admin_members = "".join(f"• {member.name}\n" for member in admins.members)
		manager_members = "".join(f"• {member.name}\n" for member in managers.members)

		em = disnake.Embed(
			title=f"Our staff team!",
			color=0xF99244
		)
		em.set_thumbnail(url=inter.guild.icon)
		em.add_field(name="Admins", value=f"{admin_members}")
		em.add_field(name="Managers", value=f"{manager_members}")
		await inter.send(embed=em)

	@commands.slash_command(description="Mark a form as solved")
	@commands.cooldown(1, 12, commands.BucketType.user)
	async def solved(self, inter):
		if not isinstance(inter.channel.parent, disnake.ForumChannel):
			return print("test")
		
		em = disnake.Embed(
			title="Solved!",
			color=0xF99244,
			description="This tread has been marked as solved, if your question has not been answered open a new tread in <#1047304462710079549> or <#1047304535074422864>"
		)
		await inter.send(embed=em)

def setup(bot):
	bot.add_cog(Utility(bot))