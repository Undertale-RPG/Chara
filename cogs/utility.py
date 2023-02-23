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
		mods = guild.get_role(971681721445654678)
		helpers = guild.get_role(1009910347123138691)
		CT = guild.get_role(1022900923611222167)
		admin_members = "".join(f"• {member.name}\n" for member in admins.members)
		manager_members = "".join(f"• {member.name}\n" for member in managers.members)
		mod_members = "".join(f"• {member.name}\n" for member in mods.members)
		helper_members = "".join(f"• {member.name}\n" for member in helpers.members)
		ct_members = "".join(f"• {member.name}\n" for member in CT.members)

		em = disnake.Embed(
			title=f"Our staff team!",
			color=0xF99244
		)
		em.set_thumbnail(url=inter.guild.icon)
		em.add_field(name="Admins", value=f"{admin_members}")
		em.add_field(name="Managers", value=f"{manager_members}")
		em.add_field(name="Moderators",value=f"{mod_members}")
		em.add_field(name="Helpers", value=f"{helper_members}")
		em.add_field(name="Community team", value=f"{ct_members}")
		await inter.send(embed=em)


	@commands.slash_command(description="ping users if you are lonely")
	@commands.cooldown(2, 43200, commands.BucketType.guild)
	async def pingfor(self, inter, ping: str = commands.Param(choices=["chat", "voice"])):
		if ping == "chat":
			await inter.send(f"<@&1041044007037448243> • {inter.author.mention} wants to chat!")
		if ping == "voice":
			await inter.send(f"<@&1041044062561648661> • {inter.author.mention} wants to voice chat!")
		return

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