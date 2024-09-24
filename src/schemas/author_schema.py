from marshmallow import Schema, validate, validates, validates_schema

from src import db, ma
from src.models.author_model import Author


class AuthorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Author
        include_fk = True
        ordered = True

    id = ma.auto_field(dump_only=True)
    name = ma.auto_field(dump_only=True)
    timestamp = ma.auto_field(dump_only=True)
    origin = ma.auto_field(dump_only=True)
