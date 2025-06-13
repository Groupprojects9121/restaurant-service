from fastapi import FastAPI, status

from code.database import create_db_and_tables
from code.routes.food import food_routes
from code.routes.restaurant import restaurant_rout

app = FastAPI()


app.include_router(food_routes)
app.include_router(restaurant_rout)


@app.on_event('startup')
def app_startup():
    create_db_and_tables()



