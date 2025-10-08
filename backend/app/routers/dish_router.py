from fastapi import APIRouter, HTTPException
from ..database import db
from ..models.dish_model import Dish

router = APIRouter(prefix="/dishes", tags=["Dishes"])

@router.post("/")
async def create_dish(dish: Dish):
    new_dish = await db.dishes.insert_one(dish.model_dump(by_alias=True))
    return {"id": str(new_dish.inserted_id), "message": "Dish added"}

@router.get("/")
async def get_all_dishes():
    dishes = await db.dishes.find().to_list(100)
    return dishes

@router.get("/{name}")
async def get_dish(name: str):
    dish = await db.dishes.find_one({"name": name})
    if not dish:
        raise HTTPException(status_code=404, detail="Dish not found")
    return dish

@router.put("/{name}")
async def update_dish(name: str, data: dict):
    result = await db.dishes.update_one({"name": name}, {"$set": data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Dish not found")
    return {"message": "Dish updated"}

@router.delete("/{name}")
async def delete_dish(name: str):
    result = await db.dishes.delete_one({"name": name})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Dish not found")
    return {"message": "Dish deleted"}
