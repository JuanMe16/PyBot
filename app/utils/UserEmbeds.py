from discord import Embed, Colour
from datetime import datetime

class UserEmbeds:

    def money_personal_info(self, wallet_message, bank_message):
        new_embed = Embed(
            colour=Colour.teal(),
            title='Money profile',
            timestamp=datetime.now()
        )
        new_embed.add_field(name='Wallet', value=wallet_message)
        new_embed.add_field(name='On bank', value=bank_message, inline=False)
        return new_embed
    
    def transaction_info(self, money_amount, transmitter_user, receiver_user, status_message):
        new_embed = Embed(
            colour=Colour.teal(),
            title='Bank transaction',
            timestamp=datetime.now()
        )
        new_embed.add_field(name='Status', value=status_message)
        new_embed.add_field(name='Transmitter', value=transmitter_user, inline=False)
        new_embed.add_field(name='Receiver',value=receiver_user, inline=True)
        new_embed.add_field(name='Money amount',value=f'${money_amount}', inline=False)
        return new_embed