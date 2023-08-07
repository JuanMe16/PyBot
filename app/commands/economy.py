from discord import Cog, Bot, slash_command, ApplicationContext
from app.models.Models import User
from app.database import bot_db
from random import random

class EconomyCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='register', description='Registers you on the economy bot.')
    async def register(self, ctx: ApplicationContext):
        author_id = ctx.author.id
        new_user = User(id=author_id)
        register_user_result = bot_db.user_controller.register_user(new_user)
        await ctx.respond(register_user_result, ephemeral=True)

    @slash_command(name='work', description='Work for money')
    async def work(self, ctx: ApplicationContext):
        gain = round((random() * 250) + 20)
        updated_money_result = bot_db.user_controller.pay_user(ctx.author.id, gain)
        await ctx.respond(updated_money_result, ephemeral=True)

    @slash_command(name='deposit', description='Deposit an amount of your in-wallet money')
    async def deposit(self, ctx: ApplicationContext, money: int):
        updated_bank_result = bot_db.user_controller.deposit_bank(ctx.author.id, money)
        await ctx.respond(updated_bank_result, ephemeral=True)

    @slash_command(name='wallet', description='Show your profit')
    async def wallet(self, ctx: ApplicationContext):
        get_wallet_result = bot_db.user_controller.get_wallet(ctx.author.id)
        await ctx.respond(get_wallet_result, ephemeral=True)

def setup(bot: Bot):
    bot.add_cog(EconomyCog(bot))