from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(String(20), primary_key=True, unique=True)
    wallet_money = Column(Integer, nullable=False, default=0)
    bank_money = Column(Integer, nullable=False, default=0)
    register_date = Column(Date, nullable=False, default=datetime.now())

    def __str__(self):
        return f"User Discord ID: {self.id}, haves {self.wallet_money} on hand, the bank haves: {self.bank_money} on his name, this member registered on the bot on {self.register_date}"

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(10), nullable=False)
    category = Column(String(30), nullable=False)
    price = Column(Integer, nullable=False, default=50)

    def __str__(self):
        return f'{self.name} it cost ${self.price}'
    
class UserItem(Base):
    __tablename__ = 'user_item'

    user_id = Column(ForeignKey(User.id), primary_key=True)
    item_id = Column(ForeignKey(Item.id), primary_key=True)
    quantity = Column(Integer, nullable=False, default=1)

    def __str__(self):
        return f'{self.quantity}'