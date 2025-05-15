from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter(prefix="/warehouses", tags=["Warehouses"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.Warehouse])
def list_warehouses(db: Session = Depends(get_db)):
    return db.query(models.Warehouse).all()

@router.post("/", response_model=schemas.Warehouse)
def create_warehouse(warehouse: schemas.WarehouseCreate, db: Session = Depends(get_db)):
    db_warehouse = models.Warehouse(**warehouse.dict())
    db.add(db_warehouse)
    db.commit()
    db.refresh(db_warehouse)
    return db_warehouse