import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

import api

app = FastAPI()
app.include_router(api.router)

@app.get('/')
def root_api():
    return {"message": "Welcome to virtual Alexandria"}
    