from discord import Embed, Colour
from datetime import datetime

class ItemEmbeds:
    item_emojis = { 1: '🍎', 2: '🍌' , 3: '📱', 4: '🧢', 5: '🪙'}
    
    def item_shop_embed(self, item_list):
        new_embed = Embed(
            colour=Colour.blue(),
            title='Welcome to the market',
            timestamp=datetime.now()
        )
        for item_object in item_list:
            new_embed.add_field(name=f'{self.item_emojis[item_object[0].id]} {item_object[0].name} `ID: {item_object[0].id}`', value=f'Category: {item_object[0].category} | `${item_object[0].price}`', inline=False)
        
        new_embed.set_author(name='PyBot Item Market',icon_url='https://i.pinimg.com/564x/6d/a4/08/6da4080433b069dde6e3646760647cad.jpg')
        new_embed.set_image(url='https://www.pngitem.com/pimgs/m/140-1408102_minecraft-png-apple-transparent-png.png')
        return new_embed
    
    def backpack_embed(self, user_name, backpack_list):
        new_embed = Embed(
            colour=Colour.teal(),
            title='You take a look at your backpack',
            timestamp=datetime.now()
        )
        for backpack_object in backpack_list:
            new_embed.add_field(name=f'{self.item_emojis[backpack_object[0].item_id]} `ID: {backpack_object[0].item_id}`', value=f'Quantity: {backpack_object[0].quantity}', inline=False)

        new_embed.set_author(name=f"{user_name.capitalize()}'s backpack")
        new_embed.set_image(url='https://i.pinimg.com/564x/bd/90/b0/bd90b0ed0a75b2986d9c3d778487b3b1.jpg')
        return new_embed