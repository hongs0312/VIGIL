import os
import sys
sys.path.append("src")

import discord
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

    image = discord.File(f"../data/imgs/{skill['image']}", filename="image.png")

    embed = discord.Embed(title=skill['name'], color=0x00ff00)
    embed.set_thumbnail(url="attachment://image.png")

    embed.add_field(name=f"Striker : {character['name']}", value="")

    embed.add_field(name="Feature", value=skill['feature'], inline=False)
    embed.add_field(name="Cooldown", value=f"{skill['cooldown']} (s)", inline=False)
    embed.add_field(name="Damage", value=skill['damage'], inline=False)

    embed.add_field(name="Description", value=skill['description'], inline=False)

    return embed, image
