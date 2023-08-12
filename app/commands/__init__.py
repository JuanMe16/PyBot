import os
from discord import Bot

def setup(bot: Bot):
    all_files = os.listdir('./app/commands')
    command_directories = [file.removesuffix('.py') for file in all_files if file.endswith('.py') and not file.startswith('__init__')]
    for module in command_directories:
        bot.load_extension(f"app.commands.{module}")
    print(f"{len(command_directories)} command modules has been loaded.")