import disnake
from disnake.ext import commands
import datetime
import asyncio

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.slash_command()
    async def announce(self, inter, ping:disnake.Role, channel:disnake.TextChannel):

        await inter.response.send_modal(
        title="Content for the announcement",
        custom_id="announce",
        components=[
            disnake.ui.TextInput(
                label="Title",
                placeholder="Announcement title",
                custom_id="title",
                style=disnake.TextInputStyle.short,
                min_length=5,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Content",
                placeholder="Announcement content",
                custom_id="content",
                style=disnake.TextInputStyle.paragraph,
                min_length=5,
                max_length=1024,
            ),
        ],
        )

        try:
            modal_inter: disnake.ModalInteraction = await self.bot.wait_for(
                "modal_submit",
                check=lambda i: i.custom_id == "announce" and i.author.id == inter.author.id,
                timeout=600,
            )
        except asyncio.TimeoutError:
            return

        tag_title = modal_inter.text_values["title"]
        tag_content = modal_inter.text_values["content"]

        em = disnake.Embed(
            title=f"`{tag_title}`",
            color=0xF99244,
            description=f"{tag_content}"
        )

        cha = self.bot.get_channel(channel.id)
        await cha.send(content=f"* {ping.mention}", embed=em)

        await inter.send(f"The announcement has been send in {channel.mention}", ephemeral=True)

def setup(bot):
	bot.add_cog(Owner(bot))