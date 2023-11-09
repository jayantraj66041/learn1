from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity

app = APIRouter()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_user(request: Request):
    docs = conn.learning1.user.find()
    users = []
    for doc in docs:
        users.append({
            'id': str(doc['_id'])[-5:],
            'name': doc['name'],
            'role': doc['role']
        })

    print(users)
    return templates.TemplateResponse("index.html", {
        'request': request, 
        'users': users
    })


@app.post("/")
async def add_user(request: Request):
    form = await request.form()
    print(form)
    print(dict(form))
    conn.learning1.user.insert_one(dict(form))
    return {"success": True}


@app.get("/delete/{id}")
async def delete_user(id: str):
    data = conn.learning1.user.delete_one({'_id':id})
    print(data)
    return {"delete success": True}
