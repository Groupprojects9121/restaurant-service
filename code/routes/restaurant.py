from fastapi import APIRouter, status, HTTPException, Depends
from sqlmodel import Session, select

from code.database import get_session
from code.models import Restaurant
from code.schemas import RestaurantRequestModel
restaurant_rout = APIRouter()


@restaurant_rout.get('/all_restaurent', 
                     status_code=status.HTTP_200_OK, 
                     tags=['Restaurant'])
def list_restaurant(db: Session = Depends(get_session)):
    return db.exec(select(Restaurant)).all()



@restaurant_rout.post('/create', 
                      status_code=status.HTTP_201_CREATED, 
                      tags=['Restaurant'])
def create_restaurent(request: RestaurantRequestModel):
    return request