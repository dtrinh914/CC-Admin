from flask import Blueprint, jsonify, request
from app.database.db_utils import get_movies

movies = Blueprint('movies', __name__, url_prefix='/movies')


@movies.route('/', methods=['GET'])
def get_route():
    data = get_movies()

    if isinstance(data, str):
        return jsonify({'error': data}), 500 
    else:
        for item in data:
            item['avg_review_score'] = str(item['avg_review_score'])
            
        return jsonify(data)

# @movies.route('/', methods=['POST'])
# def post_route():
#     username = request.form.get('username');
#     password = request.form.get('password');

#     response = add_user(username, password);

#     if response is True:
#         return jsonify({'status': 200})
#     else:
#         return jsonify({'error': response}), 500

# @movies.route('/<movie_id>', methods=['PUT'])
# def put_route(movie_id):
#     username = request.form.get('username');
#     password = request.form.get('password')
#     response = edit_user(int(user_id), username, password);

#     if response is True:
#         return jsonify({'status': 200})
#     else:
#         return jsonify({'error': response}), 500

# @movies.route('/<user_id>', methods=['DELETE'])
# def delete_route(user_id):
#     response = delete_user(int(user_id));

#     if response is True:
#         return jsonify({'status': 200})
#     else:
#         return jsonify({'error': response}), 500


