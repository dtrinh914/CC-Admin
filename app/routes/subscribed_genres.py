from flask import Blueprint, jsonify, request
import app.database.genre_api as g
subscribed_genres = Blueprint('subscribed_genres', __name__, url_prefix='/subscribed_genres')


@subscribed_genres.route('/', methods=['GET'])
def get_route():
    """returns list of subscribed genres"""
    subscribed_list = g.get_subscribed_genres()

    if isinstance(subscribed_list, str):
        return jsonify({'error':subscribed_list}), 500
    else:
        return jsonify(subscribed_list)

@subscribed_genres.route('/', methods=['POST'])
def post_route():
    user_id = request.form.get('user_id')
    genre_id = request.form.get('genre_id')

    res = g.add_genre_subscribe(genre_id, user_id)

    if res is True:
        return jsonify({'status':200})
    else:
        return jsonify({'error':res}), 500

@subscribed_genres.route('/<subscribed_id>', methods=['PUT'])
def put_route(subscribed_id):
    user_id = request.form.get('user_id')
    genre_id = request.form.get('genre_id')

    res = g.update_subscribed_genres(user_id, genre_id, subscribed_id)

    if res is True:
        return jsonify({'status':200})
    else:
        return jsonify({'error':res}), 500

@subscribed_genres.route('/<subscribed_id>', methods=['DELETE'])
def delete_route(subscribed_id):

    res = g.delete_subscribed_genres(int(subscribed_id))

    if res is True:
        return jsonify({'status':200})
    else:
        return jsonify({'error':res}), 500