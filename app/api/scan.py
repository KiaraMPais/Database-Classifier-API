# Inicia el proceso de clasificacion
from fastapi import APIRouter, HTTPException
from app.services.classification import classify_database

router = APIRouter()

@router.post("/api/v1/database/scan/{db_id}")
def scan_database(db_id: int):
    try:
        result = classify_database(db_id)
        return {"message":"Scan completed", "result":result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))