from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "hola fast api"

@app.get("/url")
async def url():
    return {"url" : "htpps://google.com"}

@app.get("/users")
async def users():
    return [{"name": "Lucas", "password": "lucas123"},
            {"name": "Leo", "password": "rolon123"}]