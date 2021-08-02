from flask import Blueprint, jsonify, request
import app.database.movies as m
watched_movies = Blueprint('watched_movies', __name__, url_prefix='/watched_movies')


@watched_movies.route('/', methods=['GET'])
def get_route():
    res = m.get_watched_movies()

    if isinstance(res, str):
        return jsonify({'error': res}), 500 
    else:
        return res

@watched_movies.route('/', methods=['POST'])
def post_route():
    user_id = request.form.get('user_id')
    movie_id = request.form.get('movie_id')

    res = m.add_watched_movies(user_id, movie_id)

    if res is True:
        return jsonify({'status':200})
    else:
        return jsonify({'error':res}), 500

@watched_movies.route('/<watched_id>', methods=['PUT'])
def put_route(watched_id):
    movie_id = request.form.get('movie_id')
    user_id = request.form.get('user_id')

    res = m.edit_watched_movies(int(watched_id), int(movie_id), int(user_id))

    if res is True:
        return jsonify({'status':200})
    else:
        return jsonify({'error':res}), 500

@watched_movies.route('/<watched_id>', methods=['DELETE'])
def delete_route(watched_id):
    
    res = m.delete_watched_movies(int(watched_id))

    if res is True:
        return jsonify({'status':200})
    else:
        return jsonify({'error':res}), 500