from fastapi import APIRouter

router = APIRouter(
    prefix="/creators",
    tags=['creators'],
    responses={404: {"description": "Not found"}}
)


@router.get("")
async def creators():
    return "/creators"


@router.get("/{creator_id}")
async def creators(creator_id: int):
    return f"/creators/{creator_id}"


# @router.get("/")
# async def creators():
#     return "/creators"
#
#
# @router.get("/")
# async def creators():
#     return "/creators"
