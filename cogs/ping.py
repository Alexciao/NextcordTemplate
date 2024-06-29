import nextcord
from nextcord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="Test command!")
    async def ping(self, interaction: nextcord.Interaction):
        embed = nextcord.Embed(
            title="🏓 Pong!",
            color=nextcord.Color.red(),
            description=f"Ping: {round(self.bot.latency * 1000)}ms",
        )


def setup(bot):
    bot.add_cog(Ping(bot))
