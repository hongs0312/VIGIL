import discord
from discord.ext import commands
from gear.service.Service import get_all_gear_info
from gear.service.embed_gear_info import embed_gear_info


class Gear(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.group(name="gear")
    async def gear_group(self, ctx):
        if ctx.invoked_subcommand is None:
            msg = "* ?gear forward로 forward gear 정보를 확인할 수 있어요.\n"
            msg += "* ?gear goalie로 goalie gear 정보를 확인할 수 있어요."

            embed = discord.Embed(title="Gear command info", color=0xC71585)
            embed.add_field(name="", value=msg, inline=False)

            await ctx.send(embed=embed)

    @gear_group.command(name="forward")
    async def gear_forward(self, ctx):
        for gear in get_all_gear_info("forward"):
            embed, image = embed_gear_info("forward", gear)
            await ctx.send(file=image, embed=embed)

    @gear_group.command(name="goalie")
    async def gear_goalie(self, ctx):
        for gear in get_all_gear_info("goalie"):
            embed, image = embed_gear_info("goalie", gear)
            await ctx.send(file=image, embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Gear(bot))
