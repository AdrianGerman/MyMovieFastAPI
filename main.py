from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from config.database import engine, Base
from middleware.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.login import login_router



app = FastAPI()
app.title = 'Mi primer app con FasAPI'
app.version = '0.0.1'
app.include_router(movie_router)
app.include_router(login_router)

app.add_middleware(ErrorHandler)

Base.metadata.create_all(bind=engine)

movies = [
    {
    "id": 1,
    "title": "Avatar",
    "overview": "Domina todos los elementos",
    "year": "2009",
    "rating": 7.8,
    "category": "Accion"
    },
    {
    "id": 2,
    "title": "Avatar 2",
    "overview": "Domina todos los elementos",
    "year": "2009",
    "rating": 7.8,
    "category": "Accion"
    }
]

@app.get('/', tags=['German'])
def message():
    return HTMLResponse('<h1>Hello world!</h1>')


        

    
    