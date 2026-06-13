from fastapi import FastAPI, Depends
app = FastAPI()
class Database():
    def get_users(self):
        return ["Baba", "Tony"]
class Products:
    def get_products(self):
        return ["Laptop", "Phone"]
    
def get_p():
    return Products()
def get_db():
    return Database()
@app.get("/users")
def get_users(db: Database = Depends(get_db)):
    print("reached")
    return db.get_users()

@app.middleware("http")
async def logger(request , call_next):
    print("Request started")
    response = await call_next(request)
    print("Request finished")
    return response

@app.get("/products")
def get_products(p: Products = Depends(get_p)):
    return p.get_products()