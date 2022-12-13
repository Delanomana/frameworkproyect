#fastapi 
from fastapi import FastAPI, Request 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates 
#database
from database import Users
from database import database as connection
#schema
from schemas import UserRequestModel
from schemas import UserResponseModel

app = FastAPI(title='Proyecto framework FLP',
            description='Testing web page',
            version='1.0.1')

templates = Jinja2Templates(directory="templates")


@app.on_event('startup')
def starup():
    if connection.is_closed():
        connection.connect()
    
    connection.create_table([Users])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()

@app.get('/index/',response_class= HTMLResponse"/")
async def index(request : Request):
    context = {'request':request}
    return templates.TemplatesResponse("index.html", context)

@app.post("/users")
async def create_user(user_request: UserRequestModel):
    user =User.create(
        username=user_request.name
        email=user_request.email
        password=user_request.password
    )
    return user_request

@app.get('/user/{user_id}')
async def get_user(user_id):
    user = Users.select().where(user.id== user_id).first()

    if user:
        return UserResponseModel(id=user.id,
                                username=user.username,
                                email=user.email)
    else:
        return HTTPException(404, 'User not found')

#@app.put("/about")
#def about():
#    return {"Data": "Acerca"}

#@app.delete("/about")
#def about():
#    return {"Data": "Acerca"}
