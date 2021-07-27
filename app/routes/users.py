from flask import Blueprint, jsonify, request
from app.database.db_utils import get_users, add_user, edit_user, delete_user

users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/', methods=['GET'])
def get_route():
    data = get_users()

    if isinstance(data, str):
        return jsonify({'error': data}), 500 
    else:
        return jsonify(data)

@users.route('/', methods=['POST'])
def post_route():
    username = request.form.get('username');
    password = request.form.get('password');

    response = add_user(username, password);

    if response is True:
        return jsonify({'status': 200})
    else:
        return jsonify({'error': response}), 500

@users.route('/<user_id>', methods=['PUT'])
def put_route(user_id):
    username = request.form.get('username');
    password = request.form.get('password')
    response = edit_user(int(user_id), username, password);

    if response is True:
        return jsonify({'status': 200})
    else:
        return jsonify({'error': response}), 500

@users.route('/<user_id>', methods=['DELETE'])
def delete_route(user_id):
    response = delete_user(int(user_id));

    if response is True:
        return jsonify({'status': 200})
    else:
        return jsonify({'error': response}), 500



