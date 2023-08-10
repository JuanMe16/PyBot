from .UserController import UserController
from .PetController import PetController
from .FoodController import FoodController
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from app.models import load_models
from settings import db_uri

class Database():
    engine: Engine
    session: Session
    user_controller: UserController
    pet_controller: PetController
    food_controller: FoodController

    def __init__(self):
        self.engine = create_engine(db_uri)
        self.base = load_models()
        making_session = sessionmaker(self.engine)
        self.session = making_session()
        self.user_controller = UserController(self.session)
        self.pet_controller = PetController(self.session)
        self.food_controller = FoodController(self.session)

    def build_db(self):
        #self.base.metadata.drop_all(self.engine)
        self.base.metadata.create_all(self.engine)