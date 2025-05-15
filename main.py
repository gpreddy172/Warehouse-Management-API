from fastapi import FastAPI
from database import Base, engine
from routers import order_items, products, suppliers, warehouses, orders

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(products.router)
app.include_router(suppliers.router)
app.include_router(warehouses.router)
app.include_router(orders.router)
app.include_router(order_items.router)