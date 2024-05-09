from discord.ext import commands
from discord import Intents
from discord import Status

TOKEN = "MTIzNjMyNjcwNzA4NzE1MTE4OQ.GBPleF.7YYGXUPoVUU_Zj7eu-YusL6hT-JTKC7ZGVCZUo"


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='?',
            intents=Intents.all(),
            sync_command=True
        )
        self.initial_extension = [
            "ability.Cog",
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

        await self.change_presence(status=Status.online)


bot = MyBot()
bot.run(TOKEN)
