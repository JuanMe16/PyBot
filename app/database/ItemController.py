from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.Models import Item, UserItem
from app.utils.AuthFunctions import check_registered_user

class ItemController:
    __session: Session

    def __init__(self, created_session):
        self.__session = created_session

    def __check_item(self, item_id):
        item_object = self.__session.execute(select(Item).filter_by(id=item_id)).scalar()
        if not item_object:
            raise ValueError("This item doesn't exist")
        return item_object
    
    def __check_item_in_backpack(self, user_id, item_id):   
        backpack_entry = self.__session.execute(select(UserItem).filter_by(user_id=user_id, item_id=item_id)).scalar()
        if not backpack_entry:
            return False
        else:
            return backpack_entry

    def get_item_shop(self, filter):
        if filter:
            db_items = self.__session.execute(select(Item).filter_by(category=filter)).all()
            items_list = [item.tuple() for item in db_items]
            return items_list
        else:
            db_items = self.__session.execute(select(Item)).all()
            items_list = [item.tuple() for item in db_items]
            return items_list
        
    def get_backpack(self, user_id):
        registered_user = check_registered_user(user_id, self.__session)
        backpack_items = self.__session.execute(select(UserItem).filter_by(user_id=registered_user.id)).all()
        items_list = [bpack_item.tuple() for bpack_item in backpack_items]
        return items_list
        
    def add_item(self, user_id, item_id, quantity):
        user_object = check_registered_user(user_id, self.__session)
        item_object = self.__check_item(item_id)
        calculated_value = item_object.price*quantity
        if calculated_value > user_object.wallet_money:
            raise ValueError("Insufficient money or invalid quantity number.")

        entry_exists = self.__check_item_in_backpack(user_object.id, item_object.id)
        user_object.wallet_money -= calculated_value
        if not entry_exists:
            new_backpack_entry = UserItem(user_id=user_object.id, item_id=item_object.id, quantity=quantity)
            self.__session.add(new_backpack_entry)
            self.__session.commit()
        else:
            entry_exists.quantity += quantity
            self.__session.commit()

        return f'You have just bought {quantity} of {item_object.name}'
    
    def remove_item(self, user_id, item_id, quantity):
        user_object = check_registered_user(user_id, self.__session)
        item_object = self.__check_item(item_id)
        calculated_sell_value = round(item_object.price*0.85)
        object_in_backpack = self.__check_item_in_backpack(user_object.id, item_object.id)
        if not object_in_backpack or object_in_backpack.quantity < quantity:
            raise ValueError("You don't own that much of the item.")
        
        if (object_in_backpack.quantity-quantity) <= 0:
            self.__session.delete(object_in_backpack)
        else:
            object_in_backpack.quantity -= quantity

        user_object.wallet_money += calculated_sell_value*quantity
        self.__session.commit()
        return f'You have just sell {quantity} of {item_object.name}'
