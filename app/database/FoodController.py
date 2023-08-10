from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.Models import Food

class FoodController:
    session: Session

    def __init__(self, created_session):
        self.session = created_session

    def get_food_shop(self):
        db_foods = self.session.execute(select(Food)).all()
        foods_list = [pet.tuple() for pet in db_foods]
        return foods_list