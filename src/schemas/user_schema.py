from marshmallow import Schema, validate, validates, validates_schema

from src import db, ma
from src.models.user_model import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        include_fk = True
        ordered = True

    id = ma.auto_field(dump_only=True)
    name = ma.auto_field(dump_only=True)
    email = ma.auto_field(dump_only=True, validate=validate.Email())
    timestamp = ma.auto_field(dump_only=True)
