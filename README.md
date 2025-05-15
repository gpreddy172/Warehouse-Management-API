# 📦 Warehousing Management System API

This is a RESTful API for managing inventory, suppliers, warehouses, and orders in a warehousing system. It is built using **FastAPI**, **SQLite**, and **SQLAlchemy**.

---

## 🚀 Features

- **Product Management**: Create, read, update, delete products, and update stock.
- **Supplier Management**: Manage suppliers who provide products.
- **Warehouse Management**: Track multiple warehouse locations and their capacities.
- **Order Management**: Manage customer orders and track order items.
- **Order Items**: Track items within each order.
- **Search & Status Update**: Search products and update order statuses.

---

## 🛠️ Tech Stack

- **FastAPI** – Web framework
- **SQLite** – Lightweight file-based database
- **SQLAlchemy** – ORM for database interaction
- **Uvicorn** – ASGI server for running FastAPI
- **Passlib & bcrypt** – Password hashing (optional for future extensions)

---

## 📁 Project Structure

```
warehouse-api/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── routers/
│   ├── products.py
│   ├── suppliers.py
│   ├── warehouses.py
│   ├── orders.py
│   └── order_items.py
└── warehouse.db  ← (auto-generated)
```

---

## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/warehouse-api.git
cd warehouse-api
```

### 2. Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt]
```

### 3. Run the App

```bash
uvicorn main:app --reload
```

---

## 📂 API Endpoints

### 🔹 Products

- `GET /products`: List all products
- `POST /products`: Add a new product
- `GET /products/{id}`: Get product by ID
- `PUT /products/{id}`: Update a product
- `DELETE /products/{id}`: Delete a product
- `PATCH /products/{id}/stock`: Update stock
- `GET /products/search?name=...&supplier=...`: Search products

### 🔹 Suppliers

- `GET /suppliers`: List all suppliers
- `POST /suppliers`: Create a new supplier

### 🔹 Warehouses

- `GET /warehouses`: List all warehouses
- `POST /warehouses`: Add a new warehouse

### 🔹 Orders

- `GET /orders`: List all orders
- `POST /orders`: Create a new order with items
- `GET /orders/{id}`: Get order by ID
- `PATCH /orders/{id}/status`: Update order status
- `GET /orders/{id}/items`: Get order items

### 🔹 Order Items

- `GET /order-items`: List all order items
- `GET /order-items/{id}`: Get an order item
- `DELETE /order-items/{id}`: Delete an order item

---

## 📄 Database

The database is SQLite and will automatically be created as `warehouse.db` in the project root when the app is first run.

---
