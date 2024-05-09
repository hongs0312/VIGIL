import sys
sys.path.append("src")

from ability.service.Service import *
from discord.ext import commands


class CooldownBot(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="ability")
    async def cool(self, ctx, *args):
        if len(args) != 2:
            await ctx.send("Invalid arguments")
            return

        character_name = args[0]
        skill_type = args[1]

        embed, image = embed_info(character_name, skill_type)

        if isinstance(embed, discord.Embed):
            await ctx.send(embed=embed, file=image)
        else:
            await ctx.send(embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CooldownBot(bot))
