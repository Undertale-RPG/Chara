import disnake
from disnake.ext import commands


class Info(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command()
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
	
	@commands.slash_command()
	@commands.cooldown(1, 12, commands.BucketType.user)
	async def server(self, inter):
		em = disnake.Embed(
			title="Server Info",
			color=0x5bb95d
		)
		em.set_thumbnail(url=inter.guild.icon)
		em.add_field(name="👑Owner", value=f"```{inter.guild.owner}```")
		em.add_field(name="👪Members", value=f"```{inter.guild.member_count}```")
		em.add_field(name="🔖Roles", value=f"```{len(inter.guild.roles)}```")
		em.add_field(name="🗃️Categories", value=f"```{len(inter.guild.categories)}```")
		em.add_field(name="📚Text channels", value=f"```{len(inter.guild.text_channels)}```")
		em.add_field(name="🙊Voice channels", value=f"```{len(inter.guild.voice_channels)}```")
		em.add_field(name="💥Creation date", value=f"```{inter.guild.created_at.ctime()}```", inline=False)

		await inter.send(embed=em)

	@commands.slash_command()
	@commands.cooldown(1, 12, commands.BucketType.user)
	async def roles(self, inter):
		guild_roles = []
		for role in inter.guild.roles:
			if role.is_bot_managed() == False:
				guild_roles.append(role)
			else:
				pass
		roles = "".join(f"• {role.mention}`({len(role.members)} members)`\n" for role in guild_roles)
		em = disnake.Embed(
			title="List of all our roles",
			color=0x5bb95d,
			description=roles
		)
		await inter.send(embed=em)

def setup(bot):
	bot.add_cog(Info(bot))