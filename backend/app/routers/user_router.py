from fastapi import APIRouter, HTTPException
from ..database import db
from ..models.user_model import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup")
async def signup(user: User):
    existing = await db.users.find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = await db.users.insert_one(user.model_dump(by_alias=True))
    return {"id": str(new_user.inserted_id), "message": "User created"}

@router.get("/{email}")
async def get_user(email: str):
    user = await db.users.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{email}")
async def update_user(email: str, data: dict):
    result = await db.users.update_one({"email": email}, {"$set": data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated"}

@router.delete("/{email}")
async def delete_user(email: str):
    result = await db.users.delete_one({"email": email})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
