from flask import Blueprint, jsonify, request
from app.database.genre_api import get_genre_names, add_db_genre, delete_genres, update_genres

genres = Blueprint('genres', __name__, url_prefix='/genres')


@genres.route('/', methods=['GET'])
def get_route():
    """retrieves all of the genre names in genre table"""
    genre_names = get_genre_names()

    if isinstance(genre_names, str):
        return jsonify({'error': genre_names}), 500 
    else:
        return jsonify(genre_names)

@genres.route('/', methods=['POST'])
def post_route():
    """posts genre name to genrea table"""
    # genre_name
    genre_name = request.form.get('genre_name')

    genre_name_res = add_db_genre(genre_name)
    
    if genre_name_res is True:
        return jsonify({'status': 200})
    else:
        return jsonify({'error': genre_name_res}), 500
    

@genres.route('/<genres_id>', methods=['PUT'])
def put_route(genres_id):
    genre_name = request.form.get('genre_name')
    res = update_genres(genres_id, genre_name)
    if res is True:
        return jsonify({'status':200})
    else:
        return jsonify({'error':res}), 500


@genres.route('/<genres_id>', methods=['DELETE'])
def delete_route(genres_id):

    res = delete_genres(int(genres_id))

    if res is True:
        return jsonify({'status':200})
    else:
        return jsonify({'error':res}), 500
    