from discord import Cog, Bot, slash_command, ApplicationContext

class ModerationCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='kick', description='Kicks a member of the discord guild.')
    async def kick_command(self, ctx: ApplicationContext):
        await ctx.respond("Te kickeo", ephemeral=True)
    

def setup(bot: Bot):
    bot.add_cog(ModerationCog(bot))