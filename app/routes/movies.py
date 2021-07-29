from flask import Blueprint, jsonify, request
from app.database.db_utils import get_movies, add_movie, edit_movie, delete_movie

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

@movies.route('/', methods=['POST'])
def post_route():
    title = request.form.get('title');
    avg_review_score = request.form.get('avg_review_score');

    response = add_movie(title, avg_review_score);

    if response is True:
        return jsonify({'status': 200})
    else:
        return jsonify({'error': response}), 500

@movies.route('/<movie_id>', methods=['PUT'])
def put_route(movie_id):
    title = request.form.get('title');
    avg_reveiw_score = request.form.get('avg_review_score')
    response = edit_movie(int(movie_id), title, avg_reveiw_score);

    if response is True:
        return jsonify({'status': 200})
    else:
        return jsonify({'error': response}), 500

@movies.route('/<movie_id>', methods=['DELETE'])
def delete_route(movie_id):
    response = delete_movie(int(movie_id));

    if response is True:
        return jsonify({'status': 200})
    else:
        return jsonify({'error': response}), 500


