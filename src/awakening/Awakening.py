import discord
from discord.ext import commands
from get_info_embed import get_info_embed
from awakening.service.embed_info import embed_info
from awakening.service.AwakeningList import AwakeningList

info_msg = [
    ["?awk list (페이지 / \"all\")", "Awakening 목록을 확인할 수 있습니다.\nex) ?awk list 1"],
    ["?awk info (각성 이름 / aka)", "Awakening 정보를 확인할 수 있습니다.\nex) ?awk info 슈퍼 서지"]
]

awk_list = AwakeningList()


class Awakening(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.group(name="awk")
    async def awakening_group(self, ctx: discord.ext.commands.Context):
        if ctx.invoked_subcommand is None:
            embed = get_info_embed("Awakening command info", info_msg)
            await ctx.send(embed=embed)

    @awakening_group.command(name="list")
    async def awakening_list(self, ctx, *args):
        awakening_list = awk_list.get_list()
        total_page = awk_list.total_page

        if len(args) > 0:
            if args[0] == "all":       # ?awk list all
                awakening_name, rotation = awk_list.get_page(0, len(awakening_list), awakening_list)

                embed = discord.Embed(title="Awakening List", color=0xC71585)
                embed.add_field(name="Awakening", value=awakening_name)
                embed.add_field(name="* Rotation", value=rotation)

                await ctx.send(embed=embed)
            elif args[0].isdigit():     # ?awk list <page number>
                page = int(args[0])

                if page > total_page or page < 1:
                    await ctx.send("페이지가 존재하지 않아요.")
                    return

                start = (page - 1) * 5
                end = min(page * 5, len(awakening_list))

                awakening_name, rotation = awk_list.get_page(start, end, awakening_list)
                embed = discord.Embed(title=f"Awakening List - Page {page} / {total_page}", color=0xC71585)
                embed.add_field(name="Awakening", value=awakening_name)
                embed.add_field(name="Rotation", value=rotation)

                await ctx.send(embed=embed)
        else:   # ?awk list or ?awk list <invalid argument>
            embed = get_info_embed("Awakening command info", info_msg)
            embed.add_field(name="Total page", value=total_page)
            await ctx.send(embed=embed)

    @awakening_group.command(name="info")
    async def awakening_info(self, ctx, *args):
        arg = " ".join(args)
        embed, image = embed_info(arg)
        await ctx.send(file=image, embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Awakening(bot))
