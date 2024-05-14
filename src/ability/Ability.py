import discord
from discord.ext import commands
from ability.service.embed_info import *


class Ability(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.group(name="skl")
    async def ability_group(self, ctx: discord.ext.commands.Context):
        if ctx.invoked_subcommand is None:
            msg = "* ?skl list 로 목록을 확인할 수 있어요.\n"
            msg += "* ?skl info <name> <skill type> 으로 정보를 확인할 수 있어요."

            embed = discord.Embed(title="Ability command info", color=0xC71585)
            embed.add_field(name="", value=msg, inline=False)

            await ctx.send(embed=embed)

    @ability_group.command(name="info")
    async def ability_info(self, ctx, *args):
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
