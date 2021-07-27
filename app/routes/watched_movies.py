from flask import Blueprint, jsonify, request

watched_movies = Blueprint('watched_movies', __name__, url_prefix='/watched_movies')


@watched_movies.route('/', methods=['GET'])
def get_route():
    # TODO: add functionality
    pass

@watched_movies.route('/', methods=['POST'])
def post_route():
    # TODO: add functionality
    pass

@watched_movies.route('/<watched_id>', methods=['PUT'])
def put_route(watched_id):
    # TODO: add functionality
    pass

@watched_movies.route('/<watched_id>', methods=['DELETE'])
def delete_route(watched_id):
    # TODO: add functionality
    pass