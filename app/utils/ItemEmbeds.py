from discord import Embed, Colour
from datetime import datetime

class ItemEmbeds:
    
    def item_shop_embed(self, item_list):
        item_emojis = { 'Apple': '🍎', 'Banana': '🍌' , 'Phone': '📱', 'Cap': '🧢', 'Wood Chest': '🪙'}

        new_embed = Embed(
            colour=Colour.blue(),
            title='Welcome to the market',
            timestamp=datetime.now()
        )
        for item_object in item_list:
            new_embed.add_field(name=f'{item_emojis[item_object[0].name]} {item_object[0].name} `ID: {item_object[0].id}`', value=f'Category: {item_object[0].category} | `${item_object[0].price}`', inline=False)
        
        new_embed.set_author(name='PyBot Item Market',icon_url='https://static.vecteezy.com/system/resources/previews/008/848/360/original/fresh-apple-fruit-free-png.png')
        new_embed.set_image(url='https://www.pngitem.com/pimgs/m/140-1408102_minecraft-png-apple-transparent-png.png')
        return new_embed