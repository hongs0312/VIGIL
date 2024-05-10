import sys
sys.path.append("src")

from awakening.service.embed_info import embed_info
from discord.ext import commands


class CooldownBot(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="awakening")
    async def awakening(self, ctx, *args):
        if len(args) == 1 and args[0] == "list":
            pass

        arg = " ".join(args)

        embed, image = embed_info(arg)
        await ctx.send(file=image, embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CooldownBot(bot))
