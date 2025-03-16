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
async def add_user(new_user: User):
    for existing_user in users:
        if new_user.login == existing_user.login:
            raise HTTPException(
                status_code=400,
                detail=f"Користувач {new_user.login} вже існує"
            )
        
    users.append(new_user)

    return {
        "status": "success",
        "message": f"Користувача {new_user.login} додано успішно",
        "data": {
            "user": new_user.model_dump()
        }
    }


@app.put("/user/edit/{login}", response_model = Response)
async def edit_user(login: str, updated_user: User):
    if login != updated_user.login:
        raise HTTPException(
            status_code=400,
            detail="Логін в URL не відповідає логіну в даних"
        )
    
    for i, user in enumerate(users):
        if user.login == login:
            users[i] = updated_user
            return {
                "status": "success",
                "message": f"Інформація про {login} оновлена",
                "data": {
                    "user": updated_user.model_dump()
                }
            }
        
    raise HTTPException(
        status_code=404,
        detail=f"Користувач з логіном {login} не знайдений"
    )


@app.delete("/user/delete/{login}", response_model = Response)
async def delete_user(login: str):
    for i, user in enumerate(users):
        if user.login == login:
            deleted_user = users.pop(i)
            return {
                "status": "success",
                "message": f"Користувач {login} видалений",
                "data": {
                    "user": deleted_user.model_dump()
                }
            }
        
    raise HTTPException(
        status_code=404,
        detail=f"Користувач з логіном {login} не знайдений"
    )

@app.get("/user/{login}", response_model = Response)
async def get_user():
    pass

@app.get("/user/get-all", response_model = Response)
async def get_all_users():
    if not users:
        return {
            "status": "success",
            "message": "Користувачів немає",
            "data": {
                "users": []
            }
        }
    
    users_data = []
    for user in users:
        user_data = user.model_dump()
        users_data.append(user_data)

    return {
        "status": "success",
        "message": f"Знайдено {len(users)} користувачів",
        "data": {
            "users": users_data
        }
    }
    
