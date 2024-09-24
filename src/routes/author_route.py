from http import HTTPStatus

from flask import Blueprint, abort
from apifairy import authenticate, body, response, other_responses

from src.app import db
from src.models.author_model import Author
from src.schemas.author_schema import AuthorSchema

authors = Blueprint('authors', __name__)
author_schema = AuthorSchema()

@authors.route('/authors', methods=['GET'])
@response(author_schema)
@response("Ok", HTTPStatus.OK)
def all():
    """Return all authors"""
    return ("todos autores")