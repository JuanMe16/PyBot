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

class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(15), nullable=False)
    color = Column(String(10), nullable=False)
    price = Column(Integer, nullable=False)

    def __str__(self):
        return f'{self.color} {self.name} it can be bought for {self.price}!'
    
class UserPet(Base):
    __tablename__ = 'user_pet'

    user_id = Column(ForeignKey(User.id), primary_key=True)
    pet_id = Column(ForeignKey(Pet.id), primary_key=True)
    experience = Column(Integer, nullable=False)

    def __str__(self):
        return f'{self.experience}'

class Food(Base):
    __tablename__ = 'foods'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(10), nullable=False)
    price = Column(Integer, nullable=False)
    quality = Column(Integer, nullable=False)

    def __str__(self):
        return f'{self.name} it cost ${self.price} and it haves a {self.quality} for your pet!'
    
class UserFood(Base):
    __tablename__ = 'user_food'

    user_id = Column(ForeignKey(User.id), primary_key=True)
    food_id = Column(ForeignKey(Food.id), primary_key=True)
    quantity = Column(Integer, nullable=False)

    def __str__(self):
        return f'{self.quantity}'