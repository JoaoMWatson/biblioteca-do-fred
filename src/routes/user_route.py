from http import HTTPStatus

from flask import Blueprint, abort
from apifairy import authenticate, body, response, other_responses

from src.app import db
from src.models.user_model import User
from src.schemas.user_schema import UserSchema 

users = Blueprint('users', __name__)
user_schema = UserSchema()


@users.route('/users', methods=['GET'])
@response(user_schema)
@other_responses({"message":"Not found", "code":HTTPStatus.NOT_FOUND})
def all():
    """Return all users"""
    return ("todos usuarios")
