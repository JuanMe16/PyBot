from discord import Cog, Bot, slash_command, ApplicationContext
from app.utils import embed_generator

class MiscellaniousCog(Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='ping', description='Does pong!')
    async def ping(self, ctx: ApplicationContext):
        bot_latency = round(ctx.bot.latency * 1000)
        message = f"Pong! {bot_latency}ms :ping_pong:"
        message_embed = embed_generator.simple_embed('Ping', message)
        await ctx.respond(embed=message_embed)

def setup(bot: Bot):
    bot.add_cog(MiscellaniousCog(bot))