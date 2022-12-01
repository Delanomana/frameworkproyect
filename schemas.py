from pydantic import BaseModel

class UserRequestModel(BaseModel):
    username: str
    email: str
    password: str

class UserResponseModel(UserRequestModel):
    id: int 