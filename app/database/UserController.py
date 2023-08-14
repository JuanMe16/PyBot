from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.Models import User
from datetime import datetime, timedelta
from app.utils.AuthFunctions import check_registered_user

class UserController:
    __session: Session
    users_cooldown = {}
    
    def __init__(self, created_session):
        self.__session = created_session

    def get_wallet(self, user_id):
        found_user = check_registered_user(user_id, self.__session)
        return (f'You have ${found_user.wallet_money} on your wallet', f'And ${found_user.bank_money} on bank.')
        
    def transfer_money(self, receiver_id, transmitter_id, money):
        transfer_user = check_registered_user(transmitter_id, self.__session)
        receiver_user = check_registered_user(receiver_id, self.__session)
        if transfer_user.bank_money < money or money <= 0:
            raise ValueError("You don't have enough money on bank to transfer.")
            
        transfer_user.bank_money -= money
        receiver_user.bank_money += money
        self.__session.commit()
        return 'Successfull transaction'


    def register_user(self, new_user: User):
        user_id = new_user.id
        existing_user = self.__session.execute(select(User).filter_by(id=user_id)).scalar()
        if existing_user:
            raise ValueError('You are already registered.')
            
        self.__session.add(new_user)
        self.__session.commit()
        return 'Successfully registered'

    def deposit_bank(self, user_id, value):
        user_found = check_registered_user(user_id, self.__session)
        if user_found.wallet_money < value or value <= 0:
            raise ValueError("Digit a valid money amount")
            
        user_found.wallet_money -= value
        user_found.bank_money += value
        self.__session.commit()
        return "Successfully deposited."
        
    def withdraw_bank(self, user_id, value):
        user_found = check_registered_user(user_id, self.__session)
        if user_found.bank_money < value or value <= 0:
            raise ValueError("Digit a valid money amount")
            
        user_found.bank_money -= value
        user_found.wallet_money += value
        self.__session.commit()
        return f"Successfully withdraw {value}."

    def pay_user(self, user_id, value):
        if float(self.users_cooldown.get(user_id, 0)) > datetime.now().timestamp():
            raise ValueError("You are on cooldown")

        user_found = check_registered_user(user_id, self.__session)    
        user_found.wallet_money += value
        self.__session.commit()
        self.users_cooldown[user_id] = (datetime.now() + timedelta(minutes=10)).timestamp()
        return f"You got paid ${value}"