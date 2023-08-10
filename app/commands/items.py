from discord import Cog, Bot, slash_command, ApplicationContext
from app.utils import embed_generator
from app.database import bot_db

class ItemsCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='item_shop', description='Shows all the items on the shop.')
    async def item_shop(self, ctx: ApplicationContext):
        get_food_result = bot_db.food_controller.get_food_shop()
        shop_embed = embed_generator.food_shop_embed(get_food_result)
        await ctx.respond(embed=shop_embed, ephemeral=True)

def setup(bot: Bot):
    bot.add_cog(ItemsCog(bot))