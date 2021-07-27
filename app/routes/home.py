from flask import Blueprint, render_template

home = Blueprint('home', __name__, url_prefix='/')


@home.route('/', methods=['GET'])
def home_page():
    return render_template('home.html')

@home.route('/admin/users', methods=['GET'])
def users_page():
    return render_template('users.html')

@home.route('/admin/movies', methods=['GET'])
def movies_page():
    return render_template('movies.html')

@home.route('/admin/reviews', methods=['GET'])
def reviews_page():
    return render_template('reviews.html')

@home.route('/admin/followings', methods=['GET'])
def followings_page():
    return render_template('followings.html')

@home.route('/admin/watched_movies', methods=['GET'])
def watched_movies_page():
    return render_template('watched_movies.html')

@home.route('/admin/genres', methods=['GET'])
def genres_page():
    return render_template('genres.html')

@home.route('/admin/subscribed_genres', methods=['GET'])
def subscribed_genres_page():
    return render_template('subscribed_genres.html')