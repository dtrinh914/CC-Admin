from flask import Blueprint, jsonify, request
import app.database.following as f
followings = Blueprint('followings', __name__, url_prefix='/followings')


@followings.route('/', methods=['GET'])
def get_route():
    res = f.get_follow_list()

    if isinstance(res, str):
        return jsonify({'error': res}), 500 
    else:
        return jsonify(res)

@followings.route('/', methods=['POST'])
def post_route():
    follower_id = request.form.get('follower_id')
    followee_id = request.form.get('followee_id')

    res = f.add_to_following(follower_id, followee_id)


    if res is True:
        return jsonify({'status':200})
    else:
        return jsonify({'error':res}), 500

@followings.route('/<following_id>', methods=['PUT'])
def put_route(following_id):
    follower_id = request.form.get('follower_id')
    followee_id = request.form.get('followee_id')
    res = f.edit_followings(follower_id, followee_id, following_id)

    if res is True:
        return jsonify({'status':200})
    else:
        return jsonify({'error':res}), 500

@followings.route('/<following_id>', methods=['DELETE'])
def delete_route(following_id):
    
    res = f.delete_followings(following_id)
    
    if res is True:
        return jsonify({'status':200})
    else:
        return jsonify({'error':res}), 500 