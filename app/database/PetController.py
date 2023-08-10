from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.Models import Pet

class PetController:
    session: Session

    def __init__(self, created_session):
        self.session = created_session

    def get_pet_shop(self):
        db_pets = self.session.execute(select(Pet)).all()
        pets_list = [pet.tuple() for pet in db_pets]
        return pets_list