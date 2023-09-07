from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from schemas.login import User


login_router = APIRouter()


@login_router.post('/login', tags=['auth'], status_code=200)
def login(user: User):
    if user.email == 'admin' and user.password == 'admin':
        token: str = create_token(user.dict())
        return JSONResponse(content=token, status_code=200)
    else: 
        return JSONResponse(content=['Credenciales invalidas'], status_code=401)

