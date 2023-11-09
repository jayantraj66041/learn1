from fastapi import FastAPI
from routes.user import user
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(user)
app.mount("/static", StaticFiles(directory="static"), name="static")
