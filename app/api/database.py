# Gestionar el endpoint para registrar la base de datos que se va a escanear
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.db import DatabaseConnector

router = APIRouter()

# Toma los datos de la base de datos.
class DatabaseInfo(BaseModel):
    host: str
    port: int
    username: str
    password: str
    dbname: str

@router.post("/api/v1/database")
def add_database_connection(db_info: DatabaseInfo):
    try:
        connection = DatabaseConnector.connect(db_info)
        # persistir la conexion segura
        return {"message":"Database connection added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))