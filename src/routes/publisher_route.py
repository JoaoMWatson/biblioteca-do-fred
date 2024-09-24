from http import HTTPStatus

from flask import Blueprint, abort
from apifairy import authenticate, body, response, other_responses

from src.app import db
from src.models.publisher_model import Publisher
from src.schemas.publisher_schema import PublisherSchema 

publishers = Blueprint('publishers', __name__)
publisher_schema = PublisherSchema()


@publishers.route('/publishers', methods=['GET'])
@response(publisher_schema)
@response("Ok", HTTPStatus.OK)
def all():
    """Return all publishers"""
    return ("todos as editoras")
