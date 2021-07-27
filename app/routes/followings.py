from flask import Blueprint, jsonify, request

followings = Blueprint('followings', __name__, url_prefix='/followings')


@followings.route('/', methods=['GET'])
def get_route():
    # TODO: add functionality
    pass

@followings.route('/', methods=['POST'])
def post_route():
    # TODO: add functionality
    pass

@followings.route('/<following_id>', methods=['PUT'])
def put_route(user_id):
    # TODO: add functionality
    pass

@followings.route('/<following_id>', methods=['DELETE'])
def delete_route(user_id):
    # TODO: add functionality
    pass