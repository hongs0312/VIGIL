import discord
from ability.service import repo
from kor_eng_name import kor_eng_name


def embed_info(character_name, skill_type):
    character = repo.get_character(character_name.lower())

    if character is None:
        return "Character not found"

    skill = repo.get_skill(character[skill_type])
    if character[skill_type] == 0 or skill is None:
        return "Skill not found"

    try:
        image = discord.File(f"../data/ability/skl_imgs/{skill['image']}", filename="image.png")
    except:
        image = discord.File(f"../data/rick.jpg", filename="image.png")

    title = skill['name']
    if skill_type == "primary":
        title += " (주 스킬)"
    elif skill_type == "secondary":
        title += " (보조 스킬)"
    elif skill_type == "special":
        title += " (특수 스킬)"
    elif skill_type == "strike":
        title += " (스트라이크)"
    elif skill_type == "passive":
        title += " (패시브)"

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


def list_info(character_name):
    character = repo.get_character(character_name.lower())

    if character is None:
        return "Character not found"

    eng_name = kor_eng_name[character['name']]
    try:
        image = discord.File(f"../data/ability/striker_imgs/{eng_name}.png", filename="image.png")
    except:
        image = discord.File(f"../data/rick.jpg", filename="image.png")

    embed = discord.Embed(title=character['name'], color=0xC71585)
    embed.set_thumbnail(url="attachment://image.png")

    for key in character:
        if key in ["primary", "secondary", "special", "strike", "passive"]:
            if character[key] == 0:
                continue

            skill = repo.get_skill(character[key])

            if key == "primary":
                title = "* 주: "
            elif key == "secondary":
                title = "* 보조: "
            elif key == "special":
                title = "* 특수: "
            elif key == "strike":
                title = "* 스트라이크: "
            elif key == "passive":
                title = "* 패시브: "

            title += skill['name']
            text = f"cooldown: {skill['cooldown']}, damage: {skill['damage']}"

            embed.add_field(name=title, value=text, inline=False)

    return embed, image
