from app.database import start_db
from settings import token
import discord

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

start_db()
bot.run(token)