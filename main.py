from fastapi import FastAPI
from db import engine, Base
from routes import router

app = FastAPI()

# Create all tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Backend running successfully 🚀"}