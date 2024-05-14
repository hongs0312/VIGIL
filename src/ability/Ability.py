import discord
from get_info_embed import get_info_embed
from discord.ext import commands
from ability.service.embed_info import *

info_msg = [
    ["?skl info (스트라이커 이름) (primary/secondary/special/passive)", "스킬 정보를 확인할 수 있습니다.\nex) ?skl info 아이.미 primary"],
]


class Ability(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.group(name="skl")
    async def ability_group(self, ctx: discord.ext.commands.Context):
        if ctx.invoked_subcommand is None:
            embed = get_info_embed("Abliity command info", info_msg)
            await ctx.send(embed=embed)

    @ability_group.command(name="info")
    async def ability_info(self, ctx, *args):
        if len(args) < 2:
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
