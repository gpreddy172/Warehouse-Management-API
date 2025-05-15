from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class SupplierBase(BaseModel):
    name: str
    contact_info: str

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int
    class Config:
        orm_mode = True

class WarehouseBase(BaseModel):
    location: str
    capacity: int

class WarehouseCreate(WarehouseBase):
    pass

class Warehouse(WarehouseBase):
    id: int
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    supplier_id: int
    warehouse_id: int

class ProductCreate(ProductBase):
    pass

class ProductUpdateStock(BaseModel):
    stock: int

class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int
    price: float

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    id: int
    order_id: int
    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    customer_name: str
    customer_address: str
    order_date: date
    status: str

class OrderCreate(OrderBase):
    order_items: List[OrderItemCreate]

class OrderUpdateStatus(BaseModel):
    status: str

class Order(OrderBase):
    id: int
    class Config:
        orm_mode = True