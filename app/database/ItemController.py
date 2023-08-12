from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.Models import Item

class ItemController:
    session: Session

    def __init__(self, created_session):
        self.session = created_session

    def get_item_shop(self, filter):
        if filter:
            db_items = self.session.execute(select(Item).filter_by(category=filter)).all()
            items_list = [item.tuple() for item in db_items]
            return items_list
        else:
            db_items = self.session.execute(select(Item)).all()
            items_list = [item.tuple() for item in db_items]
            return items_list