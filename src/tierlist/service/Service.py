import discord

kor_eng_name = {
    "아이.미" : "AiMi",
    "애셔"    : "Asher",
    "아틀라스": "Atlas",
    "드렉카르": "Drek'ar",
    "두부"    : "Dubu",
    "에라"    : "Era",
    "에스텔"  : "Estelle",
    "피니"    : "Finii",
    "줄리엣"  :"",
    "주노"    : "Juno",
    "카이"    : "Kai",
    "카잔"    : "Kazan",
    "루나"    : "Luna",
    "마코"    : "Mako",
    "나오"    : "Nao",
    "옥타비아": "",
    "라스무스": "Rasmus",
    "룬"      : "Rune",
    "바이스"  : "Vyce",
    "엑스"    : "",
    "젠타로"  : ""
}


def get_name(name):
    return kor_eng_name[name]


def get_image(name):
    try:
        image = discord.File(f"../data/tierlist/imgs/{name}_Goalie_Tierlist.png", filename=f"image.png")
    except:
        image = discord.File("../data/rick.jpg", filename=f"image.png")

    return image
