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