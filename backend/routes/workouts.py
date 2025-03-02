from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_workouts():
    return {"message": "Список тренировок"}