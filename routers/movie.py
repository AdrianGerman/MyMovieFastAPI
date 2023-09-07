from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import List

from config.database import Sesion
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middleware.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()


@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() ->List[Movie] :
    db = Sesion()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie, status_code=200)
def get_movies(id: int = Path(ge=1,le=2000)) -> Movie:
    db = Sesion()
    result = MovieService(db).get_movie_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No se ha encontrado la película'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
    

@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie], status_code=200)
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie] :
    db = Sesion()
    result = MovieService(db).get_movies_by_category(category)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No se ha encontrado la película'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict :
    db = Sesion()
    MovieService(db).create_movie(movie)
    return JSONResponse(content={"message": "Se ha registrado la película"}, status_code=201)

@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict :
    db = Sesion()
    result = MovieService(db).get_movie_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No se ha encontrado la película'})
    MovieService(db).update_movie(id, movie)
    return JSONResponse(content={"message": "Se ha modificado la película"}, status_code=200)

        
@movie_router.delete('/movie/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict :
    db = Sesion()
    result = MovieService(db).get_movie_id(id)
    if not result:
        return JSONResponse(content=["No se ha encontrado el ID de la pelicula"], status_code=404)
    MovieService(db).delete_movie(id)
    return JSONResponse(content={"message": "Se ha eliminado la película"})