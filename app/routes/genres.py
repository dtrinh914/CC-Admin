from flask import Blueprint, jsonify, request
from app.database.genre_api import get_genre_names

genres = Blueprint('genres', __name__, url_prefix='/genres')


@genres.route('/', methods=['GET'])
def get_route():
    genre_names = get_genre_names()

    if isinstance(genre_names, str):
        return jsonify({'error': data}), 500 
    else:
        return genre_names

@genres.route('/', methods=['POST'])
def post_route():
    # TODO: add functionality
    pass

@genres.route('/<genres_id>', methods=['PUT'])
def put_route(genres_id):
    # TODO: add functionality
    pass

@genres.route('/<genres_id>', methods=['DELETE'])
def delete_route(genres_id):
    # TODO: add functionality
    pass