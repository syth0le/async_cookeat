from typing import List, Union

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from api.handlers.creators import CreatorsRepository as creators
from api.schemas.creators import CreatorsGetResponse, CreatorsPostRequest, CreatorGetResponse, CreatorItem, \
    CreatorsIds, CreatorsIdsError, CreatorUpdateRequest
from api.utils.db_init import get_db
from api.utils.exceptions import Exception_404, Exception_409

router = APIRouter(
    prefix="/creators",
    tags=['creators'],
    responses={404: {"description": "Not found"}}
)


@router.get("",
            response_model=Union[CreatorsGetResponse, CreatorsIdsError],
            response_model_exclude_none=True,
            responses={200: {"model": CreatorsGetResponse}, 404: {"model": CreatorsIdsError}},
            status_code=200)
async def router_get_creators(_response: Response,
                              db: Session = Depends(get_db)):
    try:
        response = await creators.get_creators(db)
    except Exception_404 as ex:
        _response.status_code = 404
        return CreatorsIdsError(status=404, name=ex.name)
    return CreatorsGetResponse(data=response)


@router.post("",
             response_model=Union[CreatorsIds, CreatorsIdsError],
             response_model_exclude_none=True,
             responses={200: {"model": CreatorsIds}, 404: {"model": CreatorsIdsError}},
             status_code=200)
async def router_post_creators(schema: CreatorsPostRequest,
                               _response: Response,
                               db: Session = Depends(get_db)):
    try:
        response = await creators.post_creators(db=db, schema=schema)
    except Exception_409 as ex:
        _response.status_code = 409
        return CreatorsIdsError(status=409, name=ex.name)
    return CreatorsIds(creators_ids=response)


@router.get("/{creator_id}",
            response_model=Union[CreatorGetResponse, CreatorsIdsError],
            response_model_exclude_none=True,
            responses={200: {"model": CreatorGetResponse}, 404: {"model": CreatorsIdsError}},
            status_code=200)
async def router_get_single_creator(creator_id: int,
                                    _response: Response,
                                    db: Session = Depends(get_db)):
    try:
        response = await creators.get_single_creator(db=db, creator_id=creator_id)
    except Exception_404 as ex:
        _response.status_code = 404
        return CreatorsIdsError(status=404, name=ex.name)
    return response


@router.patch("/{creator_id}",
              response_model=Union[CreatorGetResponse, CreatorsIdsError],
              response_model_exclude_none=True,
              responses={200: {"model": CreatorGetResponse}, 404: {"model": CreatorsIdsError}},
              status_code=200)
async def router_patch_single_creator(creator_id: int,
                                      schema: CreatorUpdateRequest,
                                      _response: Response,
                                      db: Session = Depends(get_db)):
    try:
        response = await creators.patch_single_creator(db=db, schema=schema, creator_id=creator_id)
    except Exception_404 as ex:
        _response.status_code = 404
        return CreatorsIdsError(status=404, name=ex.name)
    return response


@router.delete("/{creator_id}",
               response_model=CreatorsIdsError,
               response_model_exclude_none=True,
               responses={200: {"model": CreatorsIdsError}, 404: {"model": CreatorsIdsError}},
               status_code=200)
async def router_delete_single_creator(creator_id: int,
                                       _response: Response,
                                       db: Session = Depends(get_db)):
    try:
        response = await creators.delete_single_creator(db=db, creator_id=creator_id)
    except Exception_404 as ex:
        _response.status_code = 404
        return CreatorsIdsError(status=404, name=ex.name)
    return response
