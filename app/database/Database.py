from .UserController import UserController
from .ItemController import ItemController
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from app.models import load_models
from settings import db_uri

class Database():
    engine: Engine
    session: Session
    user_controller: UserController
    item_controller: ItemController

    def __init__(self):
        self.engine = create_engine(db_uri)
        self.base = load_models()
        making_session = sessionmaker(self.engine)
        self.session = making_session()
        self.user_controller = UserController(self.session)
        self.item_controller = ItemController(self.session)

    def build_db(self):
        #self.base.metadata.drop_all(self.engine)
        self.base.metadata.create_all(self.engine)