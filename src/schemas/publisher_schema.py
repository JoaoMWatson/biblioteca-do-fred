from marshmallow import Schema, validate, validates, validates_schema

from src import db, ma
from src.models.publisher_model import Publisher


class PublisherSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Publisher
        include_fk = True
        ordered = True

    id = ma.auto_field(dump_only=True)
    name = ma.auto_field(dump_only=True)
    timestamp = ma.auto_field(dump_only=True)
    origin = ma.auto_field(dump_only=True)
