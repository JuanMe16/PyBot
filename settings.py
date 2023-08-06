import dotenv
import os
dotenv.load_dotenv()

token = str(os.getenv("TOKEN"))
db_uri = str(os.getenv("SQLALCHEMY_DATABASE_URI"))