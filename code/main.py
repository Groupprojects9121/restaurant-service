from fastapi import FastAPI, status

from code.database import create_db_and_tables
from code.routes.food import food_routes

app = FastAPI()


app.include_router(food_routes)


@app.on_event('startup')
def app_startup():
    create_db_and_tables()



