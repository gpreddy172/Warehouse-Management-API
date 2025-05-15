from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas
from typing import List
from datetime import date

router = APIRouter(prefix="/orders", tags=["Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.Order])
def list_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()

@router.post("/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    db_order = models.Order(
        customer_name=order.customer_name,
        customer_address=order.customer_address,
        order_date=order.order_date,
        status=order.status
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    for item in order.order_items:
        db_item = models.OrderItem(
            order_id=db_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price
        )
        db.add(db_item)
    db.commit()
    return db_order

@router.get("/{order_id}", response_model=schemas.Order)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.patch("/{order_id}/status")
def update_order_status(order_id: int, status_data: schemas.OrderUpdateStatus, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = status_data.status
    db.commit()
    return {"message": "Order status updated"}

@router.get("/{order_id}/items", response_model=List[schemas.OrderItem])
def list_order_items(order_id: int, db: Session = Depends(get_db)):
    return db.query(models.OrderItem).filter(models.OrderItem.order_id == order_id).all()