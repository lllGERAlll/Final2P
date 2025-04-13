from pydantic import BaseModel, Field, EmailStr
from typing import Literal

class modelPelicula(BaseModel):
    titulo: str = Field(..., min_length=2, description="Título de la película")
    genero: str = Field(...,min_length=4, description="Género de la película")
    anio: int = Field(..., ge=1000, le=9999, description="Año de la película")
    clasificacion: Literal['A', 'B', 'C'] = Field(..., description="Clasificación de la película (A, B o C)")
    
class modelAuth(BaseModel):
    correo: EmailStr = Field(..., description="Correo del admin")
    passw: str = Field(..., min_length=8, strip_whitespace=True, description="Contraseña del admin")