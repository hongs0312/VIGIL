import discord
from discord.ext import commands
from tierlist.service.Service import get_image, get_name


class Tierlist(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.group(name="tierlist")
    async def tierlist(self, ctx: discord.ext.commands.Context):
        if ctx.invoked_subcommand is None:
            msg = "* ?tierlist <goalie> <캐릭터 이름> 으로 티어리스트를 확인할 수 있어요\n"

            embed = discord.Embed(title="Tierlist command info", color=0xC71585)
            embed.add_field(name="", value=msg, inline=False)

            await ctx.send(embed=embed)

    @tierlist.command(name="goalie")
    async def goalie(self, ctx: discord.ext.commands.Context, *args):
        kor_name = " ".join(args)
        eng_name = get_name(kor_name)

        if eng_name == "":
            await ctx.send(f"{kor_name}은/는 골리로 적합하지 않습니다.")
            return

        await ctx.send(file=get_image(eng_name))


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Tierlist(bot))
