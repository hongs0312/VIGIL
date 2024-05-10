import sys
sys.path.append("src")

from discord.ext import commands


class CooldownBot(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="awakening")
    async def awakening(self, ctx, *args):
        arg = " ".join(args)
        await ctx.send(arg)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CooldownBot(bot))