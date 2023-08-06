from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from app.models import load_models
from settings import db_uri

class Database():
    engine: Engine
    session: Session

    def __init__(self):
        self.engine = create_engine(db_uri)
        self.base = load_models()
        making_session = sessionmaker(self.engine)
        self.session = making_session()

    def build_db(self):
        self.base.metadata.drop_all(self.engine)
        self.base.metadata.create_all(self.engine)

    def insert_to_db(self, model):
        try:
            self.session.add(model)
            self.session.commit()
            return True
        except:
            return False

    def delete_from_db(self):
        pass