from fastapi import FastAPI
from DB.conexion import Base, engine
from routers.peliculas import routerPelicula
from routers.auth import routerAuth

app = FastAPI(
    title="Final 2do Parcial",
    description="Mi primer final de FastAPI",
    version="1.0.0",
)

#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
app.include_router(routerPelicula)
app.include_router(routerAuth)

@app.get("/", tags=["Inicio"])
def main():
    return {"Mensaje": "Hola, este es mi primer final de FastAPI"}