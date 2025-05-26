from sqlmodel import create_engine, Session, SQLModel
from code.models import FoodItem

sqlite_file_name = "database.db"
sqlite_uri = f'sqlite:///{sqlite_file_name}'

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_uri, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session