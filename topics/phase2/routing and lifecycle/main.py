from fastapi import FastAPI
app = FastAPI()

@app.get("/hello/{id}")
def say_hello(id: int):
    return {"uid":id}
@app.get("/bye")
def say_bye():
    return {
        "message":"akmkb"
    }
@app.get("/boom")
def boom():
    x=1/0

@app.get("/search")
def search(query=None,page:int=1):
    return {
        "query":query,
        "page":page
    }