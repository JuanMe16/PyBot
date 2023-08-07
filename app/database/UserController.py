from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.models.Models import User

class UserController:
    session: Session
    users_cooldown = {}
    
    def __init__(self, created_session):
        self.session = created_session

    def get_wallet(self, user_id):
        try:
            existing_user = self.session.execute(select(User).filter_by(id=user_id)).scalar()
            if not existing_user:
                return 'You are not registered.'
            
            return f'You have ${existing_user.wallet_money} on your wallet'
        except Exception as ex:
            print(ex)
            return 'Internal error'

    def register_user(self, new_user: User):

        try:
            user_id = new_user.id
            existing_user = self.session.execute(select(User).filter_by(id=user_id)).scalar()
            if existing_user:
                return 'You are already registered.'
            
            self.session.add(new_user)
            self.session.commit()
            return 'Successfully registered'
        except Exception as ex:
            print(ex)
            return 'Internal Error'

    def deposit_bank(self, user_id, value):

        try:
            user_found = self.session.execute(select(User).filter_by(id=user_id)).scalar()
            if user_found.wallet_money < value or value <= 0:
                return "Digit a valid money amount"
            
            user_found.wallet_money -= value
            user_found.bank_money += value
            self.session.commit()
            return "Successfully deposited."
        except Exception as ex:
            print(ex)
            return "Internal error"

    def pay_user(self, user_id, value):
        if float(self.users_cooldown.get(user_id, 0)) > datetime.now().timestamp():
            return "You are on cooldown"

        try:
            user_found = self.session.execute(select(User).filter_by(id=user_id)).scalar()
            user_found.wallet_money += value
            self.session.commit()
            self.users_cooldown[user_id] = (datetime.now() + timedelta(minutes=2)).timestamp()
            return f"You got paid ${value}"
        except Exception as ex:
            print(ex)
            return "Internal error"