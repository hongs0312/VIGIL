from ability.service.embed_info import *
from discord.ext import commands


class Ability(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="skl")
    async def ability(self, ctx, *args):
        if len(args) != 2:
            await ctx.send("Invalid arguments")
            return

        character_name = "".join(args[:-1])
        skill_type = args[-1]

        embed, image = embed_info(character_name, skill_type)

        if isinstance(embed, discord.Embed):
            await ctx.send(embed=embed, file=image)
        else:
            await ctx.send(embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Ability(bot))
