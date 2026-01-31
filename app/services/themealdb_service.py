import httpx
from app.core.config import THEMEALDB_BASE_URL,TIMEOUT

async def fetch_from_themealdb(endpoint: str,params: dict=None):
    url=f"{THEMEALDB_BASE_URL}/{endpoint}"
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        response= await client.get(url,params=params)

        response.raise_for_status()
        return response.json()