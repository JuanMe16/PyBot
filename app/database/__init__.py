from .Database import Database

bot_db = Database()

def start_db():
    bot_db.build_db()