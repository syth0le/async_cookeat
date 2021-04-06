from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from sqlalchemy.orm import relationship
from rest_api.utils.db_init import db
from rest_api.models.categories import Category


class Top(db.Model):
    __tablename__ = 'top'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    child = relationship("Category", uselist=False, backref="top")

    def __repr__(self):
        return '<Top %r>' % self.name

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def get_all_top(cls):
        return cls.query.all()

    @classmethod
    def get_limit_top(cls, quantity):
        return cls.query.limit(quantity).all()


class TopSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Top
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)