from fastapi import FastAPI
from .routers import user_router, dish_router

app = FastAPI(title="Chat + Allergen-Aware Food Delivery Assistant")

app.include_router(user_router.router)
app.include_router(dish_router.router)

@app.get("/")
def root():
    return {"message": "Backend API is running!"}
