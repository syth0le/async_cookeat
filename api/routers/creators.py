from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.handlers.creators import *
from api.schemas.creators import CreatorsGetResponse, CreatorsPostRequest, CreatorGetResponse, CreatorItem, CreatorsIds, \
    CreatorsIdsError
from api.utils.db_init import get_db

router = APIRouter(
    prefix="/creators",
    tags=['creators'],
    responses={404: {"description": "Not found"}}
)


@router.get("", response_model=CreatorsGetResponse)
async def router_get_creators(db: Session = Depends(get_db)):
    response = await get_creators(db)
    # return CreatorsGetResponse("data" = response)
    return response


@router.post("", responses={404: {"model": CreatorsIdsError}})
async def router_post_creators(schema: CreatorsPostRequest, db: Session = Depends(get_db)):
    response = await post_creators(db=db, schema=schema)
    return response


@router.get("/{creator_id}", response_model=CreatorGetResponse)
async def router_get_single_creator(creator_id: int, db: Session = Depends(get_db)):
    response = await get_single_creator(db=db, creator_id=creator_id)
    return response


@router.patch("/{creator_id}", response_model=CreatorItem)
async def router_patch_single_creator(creator_id: int, db: Session = Depends(get_db)):
    response = await patch_single_creator(db=db, creator_id=creator_id)
    return response


# @router.delete("/{creator_id}", response_model=CreatorsIds)
@router.delete("/{creator_id}")
async def router_delete_single_creator(creator_id: int, db: Session = Depends(get_db)):
    response = await delete_single_creator(db=db, creator_id=creator_id)
    return response
