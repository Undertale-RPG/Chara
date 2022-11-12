import disnake
from disnake.ext import commands


class Info(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(description="List of all our team members")
	@commands.cooldown(1, 12, commands.BucketType.user)
	async def team(self, inter):
		guild = self.bot.get_guild(inter.guild.id)
		developers = guild.get_role(971692834077962261)
		admins = guild.get_role(849635343891955802)
		managers = guild.get_role(989189354847109122)
		mods = guild.get_role(971681721445654678)
		helpers = guild.get_role(1009910347123138691)
		CT = guild.get_role(1022900923611222167)
		dev_members = "".join(f"• {member.name}\n" for member in developers.members)
		admin_members = "".join(f"• {member.name}\n" for member in admins.members)
		manager_members = "".join(f"• {member.name}\n" for member in managers.members)
		mod_members = "".join(f"• {member.name}\n" for member in mods.members)
		helper_members = "".join(f"• {member.name}\n" for member in helpers.members)
		ct_members = "".join(f"• {member.name}\n" for member in CT.members)

		em = disnake.Embed(
			title=f"Our staff team!",
			color=0x5bb95d
		)
		em.set_thumbnail(url=inter.guild.icon)
		em.add_field(name="Developers", value=f"{dev_members}")
		em.add_field(name="Admins", value=f"{admin_members}")
		em.add_field(name="Managers", value=f"{manager_members}")
		em.add_field(name="Moderators",value=f"{mod_members}")
		em.add_field(name="Helpers", value=f"{helper_members}")
		em.add_field(name="Community team", value=f"{ct_members}")
		await inter.send(embed=em)

def setup(bot):
	bot.add_cog(Info(bot))