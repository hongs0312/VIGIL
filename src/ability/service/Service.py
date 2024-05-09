import os
import sys
import discord
#sys.path.append("src")
from ability.repository.CharacterRepository import *

cwd = os.getcwd()
print(cwd)

repo = CharacterRepository()


def embed_info(character_name, skill_type):
    character = repo.get_character(character_name)

    if character is None:
        return "Character not found"

    skill = repo.get_skill(character[skill_type])
    if skill is None:
        return "Skill not found"

    try:
        image = discord.File(f"../data/skill_imgs/{skill['image']}", filename="image.png")
    except:
        image = discord.File(f"../data/skill_imgs/rick.jpg", filename="image.png")

    title = skill['name']
    if skill_type == 'passive':
        title += " / 패시브"
    elif skill['damage'] != "0":
        title += " / 어택"

    embed = discord.Embed(title=title, color=0xC71585)
    embed.set_thumbnail(url="attachment://image.png")

    embed.add_field(name="Striker", value=character['name'])

    if skill['feature'] != "":
        embed.add_field(name="Feature", value=skill['feature'], inline=False)

    embed.add_field(name="Cooldown", value=skill['cooldown'], inline=False)

    if skill['damage'] != "0":
        embed.add_field(name="Damage", value=skill['damage'], inline=False)

    embed.add_field(name="Description", value=skill['description'], inline=False)

    return embed, image
