from flask import Blueprint, jsonify, request

genres = Blueprint('genres', __name__, url_prefix='/genres')


@genres.route('/', methods=['GET'])
def get_route():
    # TODO: add functionality
    pass

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