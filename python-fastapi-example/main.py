from fastapi import FastAPI, HTTPException
from pip import List
from pydantic import UUID4
from models.user import Gender, Role, User
from models.UserUpdateRequest import UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(
        id=UUID4("ef69ce60-fcb0-4042-ac97-6b44458ce731"), 
        first_name="Rishant", 
        last_name="Gupta",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
    User(
        id=UUID4("afb16a31-b56b-42ab-86b1-cf37684cd195"), 
        first_name="Akshy", 
        last_name="Kumar",
        gender=Gender.male,
        roles=[Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello":"World1"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID4):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist."
    )

@app.put("/api/v1/users/{user_id}")
async def delete_user(user_update: UserUpdateRequest, user_id: UUID4):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist."
    )