from fastapi import APIRouter, HTTPException
from app.services.themealdb_service import fetch_from_themealdb
from app.utils.transformers import transform_meal

router = APIRouter(prefix="/meals", tags=["Meals"])

@router.get("/search")
async def search_meal_by_name(name:str):
    data = await fetch_from_themealdb("search.php",{"s":name})
    meals = data.get("meals") or []

    return {
        "total": len(meals),
        "meals": [transform_meal(meal) for meal in meals]
    }

@router.get("/letter/{letter}")
async def serach_meal_by_letter(letter:str):
    data = await fetch_from_themealdb("search.php", {"f":letter})
    meals = data.get("meals") or []
    return {
        "total": len(meals),
        "meals": [transform_meal(meal) for meal in meals]
    }

@router.get("/{meal_id}")
async def serach_meal_by_id(meal_id:int):
    data = await fetch_from_themealdb("lookup.php", {"i":meal_id})
    meals = data.get("meals")

    if not meals:
        raise HTTPException(status_code=404, detail="Meal not found")
    return transform_meal(meals[0])

@router.get("/random/one")
async def random_meal():
    data = await fetch_from_themealdb("random.php")

    return transform_meal(data["meals"][0])