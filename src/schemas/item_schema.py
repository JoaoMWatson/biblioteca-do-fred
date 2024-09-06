from marshmallow import Schema, validate, validates, validates_schema

from src import db, ma
from src.models.item_model import Item


class ItemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Item
        include_fk = True
        ordered = True

    id = ma.auto_field(dump_only=True)
    title = ma.auto_field(dump_only=True)
    gender = ma.auto_field(dump_only=True)
    release_date = ma.auto_field(dump_only=True)
    timestamp = ma.auto_field(dump_only=True)
    edition = ma.auto_field(dump_only=True)
