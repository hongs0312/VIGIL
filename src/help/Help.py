import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="help")
    async def help_command(self, ctx):
        embed = discord.Embed(title="Command info", color=0xC71585)
        embed.add_field(name="?release", value="릴리즈 정보를 확인할 수 있습니다.", inline=False)
        embed.add_field(name="?skl", value="skill 명령어 정보를 확인할 수 있습니다.", inline=False)
        embed.add_field(name="?awk", value="awakening 명령어 정보를 확인할 수 있습니다.", inline=False)
        embed.add_field(name="?gear", value="gear 명령어 정보를 확인할 수 있습니다.", inline=False)
        embed.add_field(name="?tierlist", value="tierlist 명령어 정보를 확인할 수 있습니다.", inline=False)

        await ctx.send(embed=embed)

    @commands.command(name="release")
    async def release_command(self, ctx):
        content = ("**minor update**\n"
                   "* ux 개선\n")
        embed = discord.Embed(title="Release info (Ver 1.0.2)", color=0xC71585)
        embed.add_field(name="Release date", value="2024.05.14", inline=False)
        embed.add_field(name="Developer", value="hongs0312, sp!", inline=False)
        embed.add_field(name="Content", value=content, inline=False)
        embed.add_field(name="Command", value="?help를 쳐서 확인해주세요!", inline=False)

        await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Help(bot))
