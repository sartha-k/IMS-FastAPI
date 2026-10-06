from urllib.parse import quote_plus

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
password = quote_plus("NewPassword123!")
db_url = f"mysql+pymysql://root:{password}@localhost:3306/fastapi_db"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False,autoflush=False,bind=engine)


