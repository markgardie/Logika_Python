from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI()

class User(BaseModel):
    login: str
    first_name: str
    last_name: str
    birth_year: int

    @property
    def age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year
    

class Response(BaseModel):
    status: str
    message: str
    data: Optional[dict] = None

users = []

@app.post("/user/add", response_model = Response)
async def add_user():
    
    return {
        
    }

@app.put("/user/edit/{login}", response_model = Response)
async def edit_user():
    pass

@app.delete("/user/delete/{login}", response_model = Response)
async def delete_user():
    pass

@app.get("/user/{login}", response_model = Response)
async def get_user():
    pass

@app.get("/user/get-all", response_model = Response)
async def get_all_users():
    pass