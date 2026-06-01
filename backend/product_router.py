
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category: str
    in_stock: bool

@app.get("/products/", response_model=List[Product])
async def get_products():
    products = [
        Product(id=1, name="Laptop", description="High-performance laptop", price=1200.00, category="Electronics", in_stock=True),
        Product(id=2, name="Mouse", description="Wireless mouse", price=25.00, category="Electronics", in_stock=True),
        Product(id=3, name="T-Shirt", description="Cotton T-Shirt", price=15.00, category="Clothing", in_stock=False),
    ]
    return products

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    product = next((p for p in [
        Product(id=1, name="Laptop", description="High-performance laptop", price=1200.00, category="Electronics", in_stock=True),
        Product(id=2, name="Mouse", description="Wireless mouse", price=25.00, category="Electronics", in_stock=True),
        Product(id=3, name="T-Shirt", description="Cotton T-Shirt", price=15.00, category="Clothing", in_stock=False),
    ]), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products/", response_model=Product)
async def create_product(product: Product):
    # In a real application, you would save the product to a database here
    return product

@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: Product):
    # In a real application, you would update the product in a database here
    if product_id not in [p.id for p in [
        Product(id=1, name="Laptop", description="High-performance laptop", price=1200.00, category="Electronics", in_stock=True),
        Product(id=2, name="Mouse", description="Wireless mouse", price=25.00, category="Electronics", in_stock=True),
        Product(id=3, name="T-Shirt", description="Cotton T-Shirt", price=15.00, category="Clothing", in_stock=False),
    ]]:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
