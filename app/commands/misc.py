from discord import Cog, Bot, slash_command, ApplicationContext

class MiscellaniousCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='ping', description='Does pong!')
    async def ping(self, ctx: ApplicationContext):
        bot_latency = round(ctx.bot.latency * 1000)
        await ctx.respond(f"Pong! {bot_latency}ms :ping_pong:", ephemeral=True)

def setup(bot: Bot):
    bot.add_cog(MiscellaniousCog(bot))