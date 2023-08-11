from discord import Cog, Bot, slash_command, ApplicationContext, SlashCommandOptionType
from app.utils import embed_generator
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
        message_embed = embed_generator.simple_embed('Auth: Register',register_user_result)
        await ctx.respond(embed=message_embed, ephemeral=True)

    @slash_command(name='work', description='Work for money')
    async def work(self, ctx: ApplicationContext):
        gain = round((random() * 250) + 20)
        updated_money_result = bot_db.user_controller.pay_user(ctx.author.id, gain)
        message_embed = embed_generator.simple_embed('Work',updated_money_result)
        await ctx.respond(embed=message_embed, ephemeral=True)

    @slash_command(name='deposit', description='Deposit an amount of your in-wallet money')
    async def deposit(self, ctx: ApplicationContext, money: int):
        updated_bank_result = bot_db.user_controller.deposit_bank(ctx.author.id, money)
        message_embed = embed_generator.simple_embed('Bank deposit',updated_bank_result)
        await ctx.respond(embed=message_embed, ephemeral=True)

    @slash_command(name='withdraw', description='Withdraw an amount from your bank account')
    async def withdraw(self, ctx:ApplicationContext, money: int):
        updated_wallet = bot_db.user_controller.withdraw_bank(ctx.author.id, money)
        message_embed = embed_generator.simple_embed('Bank withdraw',updated_wallet)
        await ctx.respond(embed=message_embed, ephemeral=True)

    @slash_command(name='transfer', description='Transfer an amount of money to another discord user')
    async def transfer(self, ctx: ApplicationContext, user: SlashCommandOptionType.user, money: int):
        receiver_id = user.id
        transfer_result = bot_db.user_controller.transfer_money(receiver_id, ctx.author.id, money)
        message_embed = embed_generator.user.transaction_info(money, ctx.author.name, user.name, transfer_result)
        await ctx.respond(embed=message_embed)

    @slash_command(name='wallet', description='Show your profit')
    async def wallet(self, ctx: ApplicationContext):
        get_wallet_result = bot_db.user_controller.get_wallet(ctx.author.id)
        message_embed = embed_generator.user.money_personal_info(get_wallet_result[0], get_wallet_result[1])
        await ctx.respond(embed=message_embed)

def setup(bot: Bot):
    bot.add_cog(EconomyCog(bot))