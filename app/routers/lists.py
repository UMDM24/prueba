from fastapi import APIRouter
from app.services.themealdb_service import fetch_from_themealdb

router = APIRouter(prefix="/lists", tags=["Lists"])

@router.get("/cactegories")
async def categories():
    return await fetch_from_themealdb("categories.php")

@router.get("/categories/all")
async def all_categories():
    return await fetch_from_themealdb("list.php", {"c":"list"})

@router.get("/areas")
async def areas():
    return await fetch_from_themealdb("list.php", {"a":"list"})

@router.get("/ingredients")
async def ingredients():
    return await fetch_from_themealdb("list.php", {"i":"list"})