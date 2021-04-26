from fastapi import APIRouter
from api.handlers.creators import *

router = APIRouter(
    prefix="/creators",
    tags=['creators'],
    responses={404: {"description": "Not found"}}
)


@router.get("")
async def router_get_creators():
    response = await get_creators()
    return response


@router.post("")
async def router_post_creators():
    response = await get_creators()
    return response


@router.get("/{creator_id}")
async def router_get_single_creator(creator_id: int):
    response = await get_single_creator(creator_id)
    return response


@router.patch("/{creator_id}")
async def router_patch_single_creator(creator_id: int):
    response = await patch_single_creator(creator_id)
    return response


@router.delete("/{creator_id}")
async def router_delete_single_creator(creator_id: int):
    response = await delete_single_creator(creator_id)
    return response
