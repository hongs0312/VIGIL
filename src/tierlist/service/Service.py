import discord
from kor_eng_name import kor_eng_name


def get_name(name):
    return kor_eng_name[name]


def get_image(name):
    try:
        image = discord.File(f"../data/tierlist/imgs/{name}_Goalie_Tierlist.png", filename=f"image.png")
        return image
    except:
        return None
