import nextcord
from nextcord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="Test command!")
    async def ping(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("Pong!")


def setup(bot):
    bot.add_cog(Ping(bot))