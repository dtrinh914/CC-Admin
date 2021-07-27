from flask import Blueprint, jsonify, request

subscribed_genres = Blueprint('subscribed_genres', __name__, url_prefix='/subscribed_genres')


@subscribed_genres.route('/', methods=['GET'])
def get_route():
    # TODO: add functionality
    pass

@subscribed_genres.route('/', methods=['POST'])
def post_route():
    # TODO: add functionality
    pass

@subscribed_genres.route('/<subscribed_id>', methods=['PUT'])
def put_route(subscribed_id):
    # TODO: add functionality
    pass

@subscribed_genres.route('/<subscribed_id>', methods=['DELETE'])
def delete_route(subscribed_id):
    # TODO: add functionality
    pass