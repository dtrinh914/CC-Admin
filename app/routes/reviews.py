from flask import Blueprint, jsonify, request
import app.database.reviews as r
reviews = Blueprint('reviews', __name__, url_prefix='/reviews')


@reviews.route('/', methods=['GET'])
def get_route():
    reviews = r.get_reviews_api()

    if isinstance(reviews, str):
        return jsonify({'error': reviews}), 500 
    else:
        return jsonify(reviews)

@reviews.route('/', methods=['POST'])
def post_route():
    author_id = request.form.get('author_id')
    movie_id = request.form.get('movie_id')
    review_text = request.form.get('review_text')
    review_score = request.form.get('review_score')

    res = r.add_reviews(author_id,movie_id,review_text,review_score)

    if res is True:
        return jsonify({'status':200})
    else:
        return jsonify({'error':res}), 500

@reviews.route('/<review_id>', methods=['PUT'])
def put_route(review_id):
    author_id = request.form.get('author_id')
    movie_id = request.form.get('movie_id')
    review_text = request.form.get('review_text')
    review_score = request.form.get('review_score')
    
    res = r.edit_reviews(int(review_id), int(author_id), int(movie_id), review_text, int(review_score))
    if res is True:
        return jsonify({'status':200})
    else:
        return jsonify({'error':res}), 500

@reviews.route('/<review_id>', methods=['DELETE'])
def delete_route(review_id):
    
    res = r.delete_reviews(review_id)
    
    if res is True:
        return jsonify({'status':200})
    else:
        return jsonify({'error':res}), 500