from fastapi import APIRouter

router = APIRouter(
    prefix="/meal_plan",
    tags=['meal_plan'],
    responses={404: {"description": "Not found"}}
)


@router.get("")
async def get_meal_plan():
    return "MEAL PLAN"
