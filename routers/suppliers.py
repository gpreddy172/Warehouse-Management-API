from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("", response_model=List[schemas.Supplier])
@router.get("/", response_model=List[schemas.Supplier])
def list_suppliers(db: Session = Depends(get_db)):
    return db.query(models.Supplier).all()

@router.post("", response_model=schemas.Supplier)
@router.post("/", response_model=schemas.Supplier)
def create_supplier(supplier: schemas.SupplierCreate, db: Session = Depends(get_db)):
    db_supplier = models.Supplier(**supplier.dict())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier
