import discord
from awakening.repository.AwakeningRepo import AwakeningRepo

repo = AwakeningRepo()


def embed_info(name):
    awakening = find_awakening(name)

    if awakening is None:
        return "Awakening not found"

    image = discord.File(f"../data/awakening/imgs/{awakening['image']}", filename="image.png")

    title = awakening['name']
    embed = discord.Embed(title=title, color=0xC71585)
    embed.set_thumbnail(url="attachment://image.png")

    if awakening['aka'] != "":
        embed.add_field(name="Aka", value=awakening['aka'])

    embed.add_field(name="Rotation", value= "In" if awakening['rotation'] == b'\x01' else "Out")
    embed.add_field(name="Description", value=awakening['description'], inline=False)

    if awakening['ineffective_to'] != "":
        embed.add_field(name="Ineffective To", value=awakening['ineffective_to'], inline=False)

    return embed, image


def find_awakening(name):
    # 이름으로 우선 검색
    awakening = repo.get_awakening_by_name(name.lower())

    # 이름으로 검색했는데 없으면 aka로 검색
    if awakening is None:
        awakening = repo.get_awakening_by_aka(name.lower())

    return awakening
