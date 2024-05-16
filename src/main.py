from discord.ext import commands
from discord import Intents

import discord

TOKEN = input()     # input your token here


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='?',
            intents=Intents.all(),
            sync_command=True,
            help_command=None
        )
        self.initial_extension = [
            "help.Help",
            "ability.Ability",
            "awakening.Awakening",
            "gear.Gear",
            "tierlist.Tierlist",
        ]

    async def setup_hook(self):
        for ext in self.initial_extension:
            await self.load_extension(ext)
        await bot.tree.sync()

    async def on_ready(self):
        print("login")
        print(f"name: {self.user.name}")
        print(f"id: {self.user.id}")
        print("==============================")

        game = discord.Game("?release / Omega Strikers")
        status = discord.Status.online

        await self.change_presence(status=status, activity=game)


bot = MyBot()
bot.run(TOKEN)
