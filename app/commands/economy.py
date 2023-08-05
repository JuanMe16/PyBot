from discord import Cog, Bot, slash_command, ApplicationContext

class EconomyCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='wallet', description='Show your profit')
    async def wallet(self, ctx: ApplicationContext):
        await ctx.respond("You don't have a single dollar right now.", ephemeral=True)

def setup(bot: Bot):
    bot.add_cog(EconomyCog(bot))