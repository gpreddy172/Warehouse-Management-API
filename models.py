from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum

class OrderStatus(str, enum.Enum):
    pending = "Pending"
    fulfilled = "Fulfilled"
    cancelled = "Cancelled"

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_info = Column(String)

class Warehouse(Base):
    __tablename__ = "warehouses"
    id = Column(Integer, primary_key=True, index=True)
    location = Column(String)
    capacity = Column(Integer)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"))

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    customer_address = Column(String)
    order_date = Column(Date)
    status = Column(Enum(OrderStatus))

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    price = Column(Float)