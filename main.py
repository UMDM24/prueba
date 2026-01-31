from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import meals,filters,lists

app = FastAPI(
    title="Meal API wrapper",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(meals.router)
app.include_router(filters.router)
app.include_router(lists.router)