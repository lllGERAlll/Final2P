import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from fastapi import HTTPException

def createToken(datos:dict):
    token:str = jwt.encode(payload=datos, key='clave', algorithm='HS256')
    return token

def validateToken(token:str):
    try:
        data:dict = jwt.decode(token, key='clave', algorithms=['HS256'])
        return data
    except ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="El token ha expirado")
    except InvalidTokenError:
        raise HTTPException(status_code=403, detail="Token no autorizado")