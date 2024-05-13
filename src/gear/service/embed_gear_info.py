import discord


# gear : dict {"name": str, "description": str, "image": str}
def embed_gear_info(gear_type, gear):
    gear_name = gear["name"]
    gear_description = gear["description"]
    image = gear["image"]

    try:
        image = discord.File(f"../data/gear/imgs/{image}", filename="image.png")
    except:
        image = discord.File(f"../data/rick.jpg", filename="image.png")

    title = f"{gear_name} ({gear_type})"
    embed = discord.Embed(title=title, color=0xC71585)
    embed.set_thumbnail(url="attachment://image.png")
    embed.add_field(name="Description", value=gear_description, inline=False)

    return embed, image
