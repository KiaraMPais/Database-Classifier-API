from fastapi import FastAPI
from app.api import database, scan

app = FastAPI()

# Registrar los endpoints
app.include_router(database.router)
app.include_router(scan.router)

# Levanta el swagger
@app.get("/")
def root():
    return {"message":"Database Classifier API is running"}