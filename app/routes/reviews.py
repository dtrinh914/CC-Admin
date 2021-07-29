from flask import Blueprint, jsonify, request
from app.database.reviews import get_reviews_api
reviews = Blueprint('reviews', __name__, url_prefix='/reviews')


@reviews.route('/', methods=['GET'])
def get_route():
    return get_reviews_api()

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