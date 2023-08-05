import discord
from settings import token

bot = discord.Bot()

@bot.event
async def on_connect():
    bot.load_extension(name="app.commands", recursive=True)
    if bot.auto_sync_commands:
        await bot.sync_commands()
    print(f'Commands has been loaded.')

@bot.event
async def on_ready():
    print(f"!!! The bot is online {bot.user} !!!")

bot.run(token)