import discord
from settings import token

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"The bot is online {bot.user}")

@bot.slash_command(name='ping', description='Replies with the bot ping')
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.respond(f"Pong! {latency}ms :ping_pong:")

bot.run(token)