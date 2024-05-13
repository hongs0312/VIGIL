import discord
from discord.ext import commands
from gear.service.embed_info import embed_info


class Gear(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.group(name="gear")
    async def gear_group(self, ctx):
        msg = "* ?gear forward로 forward gear 정보를 확인할 수 있어요."
        msg += "* ?gear goalie로 goalie gear 정보를 확인할 수 있어요."

        embed = discord.Embed(title="Gear command info", color=0xC71585)
        embed.add_field(name="", value=msg, inline=False)

    @gear_group.command(name="forward")
    async def gear_forward(self, ctx):
        pass

    @gear_group.command(name="goalie")
    async def gear_goalie(self, ctx):
        pass


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Gear(bot))
