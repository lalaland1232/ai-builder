from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
app=FastAPI()
class UserNotFound(Exception):
    pass
@app.exception_handler(UserNotFound)
def user_not_found(request,exc):
    return JSONResponse(
        status_code=404,
        content={"message":"User not found",
                
                }
    )

@app.get("/user/{id}")
def checker(id:int):
    if id== 999:
        raise UserNotFound()
    
    return {"message":"User found",
             }
