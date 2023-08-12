from discord import Cog, Bot, slash_command, ApplicationContext, OptionChoice, Option
from app.utils import embed_generator
from app.database import bot_db

class ItemsCog(Cog):
    __misc_choice = OptionChoice('Misc', 'Misc')
    __food_choice = OptionChoice('Food', 'Food')
    __chest_choice = OptionChoice('Chest', 'Chest')
    __category_filter_option = Option(str, 'Choose a filter option', choices=[__misc_choice, __food_choice, __chest_choice], required=False)
    
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='item_shop', description='Shows all the items on the shop.')
    async def item_shop(self, ctx: ApplicationContext, filter: __category_filter_option):
        get_item_result = bot_db.item_controller.get_item_shop(filter)
        shop_embed = embed_generator.items.item_shop_embed(get_item_result)
        await ctx.respond(embed=shop_embed, ephemeral=True)

def setup(bot: Bot):
    bot.add_cog(ItemsCog(bot))