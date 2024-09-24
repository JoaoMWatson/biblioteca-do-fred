from http import HTTPStatus

from flask import Blueprint, abort
from apifairy import authenticate, body, response, other_responses

from src.app import db
from src.models.item_model import Item
from src.schemas.item_schema import ItemSchema

items = Blueprint('items', __name__)
item_schema = ItemSchema()


@items.route('/items', methods=['GET'])
@response(item_schema)
@response("Ok", HTTPStatus.OK)
def all():
    """Return all items"""
    return ("todos itens")
