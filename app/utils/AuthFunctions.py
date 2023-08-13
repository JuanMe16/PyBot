from sqlalchemy import select
from app.models.Models import User

def check_registered_user(user_id, db_session):
        user_to_check = db_session.execute(select(User).filter_by(id=user_id)).scalar()
        if not user_to_check:
            raise ValueError('This user is not registered.')
        return user_to_check