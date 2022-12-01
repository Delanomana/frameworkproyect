from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Data": "home"}

@app.get("/about")
def about():
    return {"Data": "Acerca"}