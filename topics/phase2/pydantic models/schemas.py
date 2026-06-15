from pydantic import BaseModel,Field,EmailStr,field_validator
class UserCreateRequest(BaseModel):
    name:str= Field(min_length=2)

    email:EmailStr
    @field_validator('name')
    def name_validator(cls,value):
        if value.strip=="":
            raise ValueError("Name cannot be empty")
        return value
    
class UserCreateResponse(BaseModel):
    id:int
    name:str
    email:EmailStr