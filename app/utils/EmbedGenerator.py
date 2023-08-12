from discord import Embed, Colour
from datetime import datetime
from .ItemEmbeds import ItemEmbeds
from .UserEmbeds import UserEmbeds

class EmbedGenerator:
    items: ItemEmbeds
    user: UserEmbeds

    def __init__(self) -> None:
        self.items = ItemEmbeds()
        self.user = UserEmbeds()
    
    def simple_embed(self, message_title , message_value):
        new_embed = Embed(
            colour=Colour.teal(),
            timestamp=datetime.now()
        )
        new_embed.add_field(name=message_title, value=message_value)
        return new_embed
    
    def error_embed(self, error_value):
        error_embed = Embed(
            colour=Colour.red(),
            timestamp=datetime.now()
        )
        error_embed.add_field(name='Error message', value=error_value)
        return error_embed