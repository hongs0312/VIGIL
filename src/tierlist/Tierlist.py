import discord
from discord.ext import commands
from get_info_embed import get_info_embed
from tierlist.service.Service import get_image, get_name

info_msg = [
    ["?tierlist goalie (캐릭터 이름)", "골리 티어리스트를 확인할 수 있어요.\nex) ?tierlist goalie 아이.미"],
]


class Tierlist(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.group(name="tierlist")
    async def tierlist(self, ctx: discord.ext.commands.Context):
        if ctx.invoked_subcommand is None:
            embed = get_info_embed("Tierlist command info", info_msg)
            await ctx.send(embed=embed)

    @tierlist.command(name="goalie")
    async def goalie(self, ctx: discord.ext.commands.Context, *args):
        kor_name = " ".join(args)

        if kor_name.replace(" ", "") == "아이미":
            kor_name = "아이.미"

        eng_name = get_name(kor_name)
        image = get_image(eng_name)

        if image is None:
            await ctx.send(f"{kor_name}은/는 골리로 적합하지 않습니다.")
            return

        await ctx.send(file=image)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Tierlist(bot))
