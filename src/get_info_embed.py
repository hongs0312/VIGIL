import discord


def get_info_embed(title, info_msg):
    embed = discord.Embed(title=title, color=0xC71585)
    for line in info_msg:
        embed.add_field(name=line[0], value=line[1], inline=False)

    return embed
