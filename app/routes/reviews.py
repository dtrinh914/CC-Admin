from flask import Blueprint, jsonify, request

reviews = Blueprint('reviews', __name__, url_prefix='/reviews')


@reviews.route('/', methods=['GET'])
def get_route():
    # TODO: add functionality
    pass

@reviews.route('/', methods=['POST'])
def post_route():
    # TODO: add functionality
    pass

@reviews.route('/<review_id>', methods=['PUT'])
def put_route(review_id):
    # TODO: add functionality
    pass

@reviews.route('/<review_id>', methods=['DELETE'])
def delete_route(review_id):
    # TODO: add functionality
    pass