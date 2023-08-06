from discord import Cog, Bot, slash_command, ApplicationContext
from app.models.Models import User
from app.database import bot_db

class EconomyCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='register', description='Registers you on the economy bot.')
    async def register(self, ctx: ApplicationContext):
        author_id = ctx.author.id
        new_user = User(id=author_id)
        insert_result = bot_db.insert_to_db(new_user)
        message = 'Successfully registed' if insert_result else 'You are already registered'
        await ctx.respond(message, ephemeral=True)

    @slash_command(name='wallet', description='Show your profit')
    async def wallet(self, ctx: ApplicationContext):
        await ctx.respond("You don't have a single dollar right now.", ephemeral=True)

def setup(bot: Bot):
    bot.add_cog(EconomyCog(bot))