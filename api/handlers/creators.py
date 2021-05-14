from sqlalchemy.orm import Session

from api.handlers.base import BaseRepository
from api.models.creators import Creators
from api.schemas.creators import CreatorItem, CreatorsGetResponse


class CreatorsRepository(BaseRepository):

    async def get_creators(db: Session) -> CreatorsGetResponse:
        data = db.query(Creators).all()
        return CreatorsGetResponse(data=data)


    async def post_creators(db: Session, schema):
        temp = list()
        for elem in schema.data:
            creator = Creators(**elem.dict())
            db.add(creator)
            db.commit()
            db.refresh(creator)
            temp.append(elem)

        return temp


    async def get_single_creator(db: Session, creator_id):
        return db.query(Creators).filter_by(id=creator_id).first()


    async def patch_single_creator(db: Session, creator_id):
        creator = db.query(Creators).filter_by(id=creator_id).first()
        # stored_creator = CreatorItem(creator)
        # update_data = CreatorItem.dict(exclude_unset=True)
        # updated_item = stored_creator.copy(update=update_data)
        #
        # db.add(updated_item)
        # db.commit()
        return creator


    async def delete_single_creator(db: Session, creator_id):
        creator = db.query(Creators).filter_by(id=creator_id).first()
        db.delete(creator)
        db.commit()
        return f"delete single creator {creator_id}"
