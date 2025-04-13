from fastapi import HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from modelsPydantic import modelPelicula
from middleWares import BearerJWT
from DB.conexion import Session
from models.modelsDB import Movie
from fastapi import APIRouter

routerPelicula = APIRouter()

#Endpoint para guardar peliculas
@routerPelicula.post("/peliculas/", response_model=modelPelicula, tags=["Peliculas CRUD"])
def guardarPelicula(peliculaNueva:modelPelicula):
    db = Session()
    try:
        db.add(Movie(**peliculaNueva.model_dump()))
        db.commit()
        return JSONResponse(status_code=201, content={"Mensaje": "Pelicula guardada", "Pelicula": peliculaNueva.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"Mensaje": "Error al guardar la pelicula", "Error": str(e)})
    finally:
        db.close()
        
#Endpoint para editar una pelicula
@routerPelicula.put("/peliculas/{pelicula_id}", response_model=modelPelicula, tags=["Peliculas CRUD"])
def editarPelicula(pelicula_id:int, peliculaActualizada:modelPelicula):
    db = Session()
    try:
        pelicula = db.query(Movie).filter(Movie.id == pelicula_id).first()
        if not pelicula:
            raise JSONResponse(status_code=404, content={"Mensaje": "Pelicula no encontrada"})
        
        for key, value in peliculaActualizada.model_dump().items():
            setattr(pelicula, key, value)
        db.commit()
        return JSONResponse(status_code=200, content={"Mensaje": "Pelicula actualizada", "Pelicula": peliculaActualizada.model_dump()})
    except Exception as g:
        db.rollback()
        return JSONResponse(status_code=500, content={"Mensaje": "Error al actualizar la pelicula", "Error": str(g)})
    finally:
        db.close()
        
#Endpoint para eliminar una pelicula
@routerPelicula.delete("/peliculas/{pelicula_id}",dependencies = [Depends(BearerJWT())], tags=["Peliculas CRUD"])
def eliminarPelicula(pelicula_id:int):
    db = Session()
    try:
        pelicula = db.query(Movie).filter(Movie.id == pelicula_id).first()
        if not pelicula:
            raise JSONResponse(status_code=404, content={"Mensaje": "Pelicula no encontrada"})
        db.delete(pelicula)
        db.commit()
        return JSONResponse(status_code=200, content={"Mensaje": "Pelicula eliminada"})
    except Exception as h:
        db.rollback()
        return JSONResponse(status_code=500, content={"Mensaje": "Error al eliminar la pelicula", "Error": str(h)})
    finally:
        db.close()
        
#Enpoint para consultar todas las peliculas
@routerPelicula.get("/peliculas", tags=["Peliculas CRUD"])
def consultarPeliculas():
    db = Session()
    try:
        consulta = db.query(Movie).all()
        return JSONResponse(content= jsonable_encoder(consulta))
    except Exception as i:
        return JSONResponse(status_code=500, content={"Mensaje": "Error al consultar las peliculas", "Error": str(i)})
    finally:
        db.close()
        
#Endpoint para consultar una pelicula
@routerPelicula.get("/peliculas/{pelicula_id}", tags=["Peliculas CRUD"])
def consultarPelicula(pelicula_id:int):
    db = Session()
    try:
        consulta = db.query(Movie).filter(Movie.id == pelicula_id).first()
        if not consulta:
            raise JSONResponse(status_code=404, content={"Mensaje": "Pelicula no encontrada"})
        return JSONResponse(content= jsonable_encoder(consulta))
    except Exception as j:
        return JSONResponse(status_code=500, content={"Mensaje": "Error al consultar la pelicula", "Error": str(j)})
    finally:
        db.close()