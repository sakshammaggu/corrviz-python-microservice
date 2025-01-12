from fastapi import FastAPI
from app.routes import csv_processor

app = FastAPI()

app.include_router(csv_processor.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Data Correlation and Relationship Visualization Microservice!"}