from discord import Cog, Bot, slash_command, ApplicationContext
from app.utils import embed_generator
from app.database import bot_db

class PetCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='pet_shop', description='Shows all the pets on the shop.')
    async def pet_shop(self, ctx: ApplicationContext):
        get_pets_result = bot_db.pet_controller.get_pet_shop()
        shop_embed = embed_generator.pet_shop_embed(get_pets_result)
        await ctx.respond(embed=shop_embed, ephemeral=True)

def setup(bot: Bot):
    bot.add_cog(PetCog(bot))