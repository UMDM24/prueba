from fastapi import APIRouter
from app.services.themealdb_service import fetch_from_themealdb

router = APIRouter(prefix="/filters", tags=["Filters"])

@router.get("/ingredients/{ingredient}")
async def filter_by_ingredient(ingredient:str):
    return await fetch_from_themealdb("filter.php",{"i":ingredient})

@router.get("/category/{category}")
async def filter_by_category(category:str):
    return await fetch_from_themealdb("filter.php",{"c":category})

@router.get("/area/{area}")
async def filter_by_area(area:str):
    return await fetch_from_themealdb("filter.php",{"a":area})