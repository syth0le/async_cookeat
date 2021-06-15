import sqlalchemy
from fastapi import HTTPException
from sqlalchemy.orm import Session
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from api.handlers.base import BaseRepository
from api.models.creators import Creators
from api.schemas.creators import CreatorItem, CreatorsGetResponse, CreatorsIdsError
from api.utils.exceptions import Exception_404, Exception_409


class CreatorsRepository(BaseRepository):

    async def get_creators(db: Session):
        data = db.query(Creators).all()
        if data:
            raise Exception_404(name="Not found elements")
        return data

    async def post_creators(db: Session, schema):
        temp = list()
        errors = list()
        for elem in schema.data:
            creator = Creators(**elem.dict())
            try:
                db.add(creator)
                db.commit()
                db.refresh(creator)
            except:
                errors.append(elem.name)
            temp.append(elem.name)
        if errors:
            raise Exception_409(name=f"Elements: {temp} already exists.")
        return db.query(Creators).filter(Creators.name.in_(temp)).all()

    async def get_single_creator(db: Session, creator_id):
        data = db.query(Creators).filter_by(id=creator_id).first()
        if data is None:
            raise Exception_404(name=f"Not found element with id={creator_id}")
        return data

    async def patch_single_creator(db: Session, schema: CreatorItem, creator_id: int):
        print(schema.dict(), type(schema))
        stored_creator_data = db.query(Creators).filter_by(id=creator_id).first()
        print(stored_creator_data)
        stored_creator_model = CreatorItem.from_orm(stored_creator_data)
        print(stored_creator_model, type(stored_creator_model))
        update_data = schema.dict(exclude_unset=True)
        print(update_data)
        updated_item = stored_creator_model.copy(update=update_data)
        print(updated_item, type(schema))
        # db.
        db.add(*update_data)
        db.commit()
        db.refresh(**updated_item)
        # return updated_item

    async def delete_single_creator(db: Session, creator_id: int) -> dict:
        creator = db.query(Creators).filter_by(id=creator_id).first()
        if creator is None:
            raise Exception_404(name=f"Not found element with id={creator_id}")
        db.delete(creator)
        db.commit()
        return {"creator_id": creator_id, "status": 200, "name": f"Deleted single creator with id={creator_id}"}
