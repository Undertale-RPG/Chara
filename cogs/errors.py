import disnake 
import requests
from disnake.ext import commands

class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_slash_command_error(self, inter, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = disnake.Embed(
                title="This command is on cooldown!",
                description=f"Try again in **{error.retry_after:.2f}** seconds",
                color=0xF99244
            )
            return await inter.send(embed=em, ephemeral=True)
        else:
            await inter.send("You have run into a Error the developer has been notified." ,ephemeral=True)
        
        url = inter.bot.error_webhook

        embed = {
            "description": f"{error}",
            "title": "An error has occured",
            "color": 0xF99244,
            "timestamp": ""
        }
        
        data = {
            "embeds": [embed]
        }
        result = requests.post(url, json=data)
        if 200 <= result.status_code < 300:
            print(f"Webhook sent {result.status_code}")
            raise error
        else:
            print(f"Not sent with {result.status_code}, response:\n{result.json()}")
            raise error


def setup(bot):
    bot.add_cog(Errors(bot))