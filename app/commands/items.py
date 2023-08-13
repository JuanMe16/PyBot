from discord import Cog, Bot, slash_command, ApplicationContext, OptionChoice, Option
from app.utils import embed_generator
from app.database import bot_db

class ItemsCog(Cog):
    __misc_choice = OptionChoice('Misc', 'Misc')
    __food_choice = OptionChoice('Food', 'Food')
    __chest_choice = OptionChoice('Chest', 'Chest')
    __category_filter_option = Option(str, 'Choose a filter option', choices=[__misc_choice, __food_choice, __chest_choice], required=False)
    __item_quantity = Option(int, 'Choose a quantity to buy', required=False)
    
    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx: ApplicationContext, error: Exception) -> None:
        error_embed = embed_generator.error_embed(error.args[0][52:])
        return await ctx.respond(embed=error_embed, ephemeral=True)   

    @slash_command(name='item_shop', description='Shows all the items on the shop.')
    async def item_shop(self, ctx: ApplicationContext, filter: __category_filter_option):
        get_item_result = bot_db.item_controller.get_item_shop(filter)
        shop_embed = embed_generator.items.item_shop_embed(get_item_result)
        await ctx.respond(embed=shop_embed, ephemeral=True)

    @slash_command(name='buy_item', description="Buy an item from the shop with it's ID.")
    async def buy_item(self, ctx: ApplicationContext, item_id: int, item_quantity: __item_quantity):
        item_quantity = 1 if not item_quantity else item_quantity
        add_item_result = bot_db.item_controller.add_item(ctx.author.id, item_id, item_quantity)
        order_embed = embed_generator.simple_embed('Added to backpack!', add_item_result)
        await ctx.respond(embed=order_embed)

    @slash_command(name='sell_item', description="Sell an item from your backpack with it's ID.")
    async def sell_item(self, ctx: ApplicationContext, item_id: int, item_quantity: __item_quantity):
        pass

    @slash_command(name='show_backpack', description='Shows the items that you have stored in your backpack.')
    async def show_backpack(self, ctx: ApplicationContext):
        backpack_list = bot_db.item_controller.get_backpack(ctx.author.id)
        backpack_embed = embed_generator.items.backpack_embed(ctx.author.name, backpack_list)
        await ctx.respond(embed=backpack_embed)


def setup(bot: Bot):
    bot.add_cog(ItemsCog(bot))