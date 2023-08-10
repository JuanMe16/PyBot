from discord import Embed, Colour
from datetime import datetime

class EmbedGenerator:
    
    def simple_embed(self, message_title , message_value):
        new_embed = Embed(
            colour=Colour.teal(),
            timestamp=datetime.now()
        )
        new_embed.add_field(name=message_title, value=message_value)
        return new_embed
    
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
    
    def pet_shop_embed(self, pet_list):
        pet_emojis = { 'Cat': '🐈', 'Dog': '🐕' }

        new_embed = Embed(
            colour=Colour.blue(),
            title='Welcome to the pet shop',
            timestamp=datetime.now()
        )
        for pet_object in pet_list:
            new_embed.add_field(name=f'{pet_emojis[pet_object[0].name]} {pet_object[0].name} `ID: {pet_object[0].id}`', value=f'Color: {pet_object[0].color} ${pet_object[0].price}', inline=False)
        
        new_embed.set_author(name='PyBot Pet Seller',icon_url='https://img.freepik.com/vector-gratis/tienda-mascotas-relacionada_24908-57968.jpg')
        new_embed.set_image(url='https://petindustry.co/wp-content/uploads/2022/02/PETSHOP-TENDENCIAS-PETINDUSTRY1.jpeg')
        return new_embed
    
    def food_shop_embed(self, food_list):
        food_emojis = { 'Apple': '🍎', 'Banana': '🍌' }

        new_embed = Embed(
            colour=Colour.blue(),
            title='Welcome to the market',
            timestamp=datetime.now()
        )
        for food_object in food_list:
            new_embed.add_field(name=f'{food_emojis[food_object[0].name]} {food_object[0].name} `ID: {food_object[0].id}`', value=f'Quality: {food_object[0].quality} ${food_object[0].price}', inline=False)
        
        new_embed.set_author(name='PyBot Food Market',icon_url='https://static.vecteezy.com/system/resources/previews/008/848/360/original/fresh-apple-fruit-free-png.png')
        new_embed.set_image(url='https://flavorsofbogota.com/wp-content/uploads/2013/05/Colombian-fruits-Paloquemao-960x540.jpg')
        return new_embed