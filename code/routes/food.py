from fastapi import APIRouter, status, Depends, HTTPException
from sqlmodel import Session, select

from code.schemas import FoodRequestModel, FoodResponseModel
from code.models import FoodItem
from code.database import get_session

food_routes = APIRouter()


@food_routes.get('/all_items', 
                 status_code=status.HTTP_200_OK, 
                 tags=['food'])
def get_all_items_view(db: Session = Depends(get_session)):
    return db.exec(select(FoodItem)).all()


@food_routes.get('/item/{id}', 
                 status_code=status.HTTP_200_OK, 
                 tags=['food'])
def get_item_view(id: int, db: Session = Depends(get_session)):
    instance = db.exec(select(FoodItem).where(FoodItem.id == id)).first()
    if not instance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Food with {id} not found.")
    return instance


@food_routes.post('/food', 
                  status_code=status.HTTP_201_CREATED, 
                  response_model=FoodResponseModel, 
                  tags=['food'])
def create_food_view(request: FoodRequestModel, db: Session = Depends(get_session)):
    instance = FoodItem(name=request.name, description=request.description)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


@food_routes.put('/item/{id}', 
                 status_code=status.HTTP_202_ACCEPTED, 
                 tags=['food'])
def update_food_view(id: int, request: FoodRequestModel, db: Session = Depends(get_session)):
    instance = db.get(FoodItem, id)
    if not instance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Food with {id} not found.")
    
    data = request.dict()

    for key, value in data.items():
        setattr(instance, key, value)
        
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


@food_routes.delete('/item/{id}',
                    status_code=status.HTTP_202_ACCEPTED,
                    tags=['food'])
def delete_food_view(id: int, db: Session = Depends(get_session)):
    instance = db.get(FoodItem, id)
    if not instance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Food with {id} not found.")
    db.delete(instance)
    db.commit()
    return {'data': f'Food with id {id} deleted.'}