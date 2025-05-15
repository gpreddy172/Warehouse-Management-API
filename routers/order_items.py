from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas
from typing import List

router = APIRouter(prefix="/order-items", tags=["Order Items"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.OrderItem])
def list_order_items(db: Session = Depends(get_db)):
    return db.query(models.OrderItem).all()

@router.get("/{item_id}", response_model=schemas.OrderItem)
def get_order_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.OrderItem).filter(models.OrderItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")
    return item

@router.delete("/{item_id}")
def delete_order_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.OrderItem).filter(models.OrderItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")
    db.delete(item)
    db.commit()
    return {"message": "Order item deleted"}
