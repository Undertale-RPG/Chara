import disnake
from disnake.ext import commands
import datetime

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="our github issue tracker")
    async def github(self, inter):
        em = disnake.Embed(
            title="Github issue tracker",
            url="https://top.gg/bot/748868577150369852",
            color=0xF99244,
            description="If you wish to report a bug/issue or add a feature request for our bot head over to our Github, there you can create a new issue or add addition information to a already existing issue.\n\n**bug reports and suggestions done outside of this issue tracker are invalid**\n\n*Note: The GitHub issue tracker is public. As such, you should avoid posting sensitive information.*"
        )
        await inter.send(embed=em)

def setup(bot):
	bot.add_cog(Info(bot))