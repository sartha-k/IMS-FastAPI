from itertools import product
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from database import engine, session 
import database_model
from models import Products

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],

    allow_methods=["*"],
  
)
database_model.Base.metadata.create_all(bind=engine)

db = session()
@app.get("/")
def greet():
    return "hello this is fastapi backend code"

@app.get("/products")
def get_all_products():
   
    return db.query(database_model.Product).all()

@app.get("/products/{id}")
def get_by_id(id:int):
    db_product = db.query(database_model.Product).filter(database_model.Product.id==id).first()
    if db_product:
        return db_product
    return "product not found"
       

@app.post("/products")
def add(product:Products):
    db.add(database_model.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id:int,product:Products):
    db_product = db.query(database_model.Product).filter(database_model.Product.id==id).first()
    if db_product:
        db_product.name=product.name
        db_product.description=product.description
        db_product.quantity=product.quantity
        db_product.price=product.price
        db.commit()
        return "product updated"
    return "no product found for updated" 

@app.delete("/products/{id}")
def delete_product(id:int):
    db_product = db.query(database_model.Product).filter(database_model.Product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "product deleted successfully"
    return "product not found"
