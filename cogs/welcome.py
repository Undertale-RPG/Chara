import disnake
from disnake.ext import commands, tasks

class Welcome(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.boost_stats.start()

  @tasks.loop(minutes=5)
  async def boost_stats(self):
    await self.bot.wait_until_ready()
    guild = self.bot.get_guild(817437132397871135)
    lista = []
    for i in guild.premium_subscribers:
      lista.append(i.id)

    await self.bot.boosters.update_one({"_id" : 0}, {"$set" : {"boosters" : lista}})
    print("Boosters has been updated")

  @commands.slash_command()
  async def test(self, ctx: disnake.Interaction, member: disnake.Member= commands.Param(description="Choose a member")): 
    await ctx.response.send_message(content=f"Member passed: {member}")
    
  @commands.Cog.listener()
  async def on_member_join(self, member):
    embed = disnake.Embed()
    embed.set_thumbnail(member.guild.icon.url)
    embed.title=f"Welcome to {member.guild.name}"
    embed.set_author(name=str(member), icon_url=member.avatar.url)
    embed.set_footer(text=f"Thanks for joining, your the {member.guild.member_count}th member!", icon_url=self.bot.user.avatar.url)
    embed.description="• Be sure to read the <#827771691727716353>\n• You can chat with other people at <#827651362099036180>\n • Ask for support and help at <#827651414540943370>!\n• You can get some notification roles at <#846972481511227432>"
    embed.set_image("https://cdn.discordapp.com/attachments/899309915020095488/900106251256623154/You_Doodle_2021-10-19T19_40_42Z.jpg")
    cha = self.bot.get_channel(850282417017454602)
    await cha.send(content=f"* Welcome {member.mention}", embed=embed)
    

def setup(bot):
  bot.add_cog(Welcome(bot))