from fastapi.responses import JSONResponse
from modelsPydantic import modelAuth
from genToken import createToken
from fastapi import APIRouter

routerAuth = APIRouter()

#Endpoint para generar token
@routerAuth.post('/auth', tags=["Autenticación"])
def login(autorizado:modelAuth):
    if autorizado.correo == 'admin@admin.com' and autorizado.passw == '12345678':
        token:str = createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content={"Token": token})
    else:
        return {"Aviso": "Usuario no autorizado"}