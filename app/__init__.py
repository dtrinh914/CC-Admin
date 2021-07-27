from flask import Flask
from app.database import db_connection, db_utils, genre_api
from dotenv import load_dotenv, find_dotenv
import os


def create_app(env='DEV') -> Flask:
    """Assembles and returns CouchCritique Flask Application."""
    load_dotenv(find_dotenv())

    app = Flask(__name__)
    app.config['ENV'] = env

    # register blueprints to app
    with app.app_context():
        from app.routes.home import home
        from app.routes.users import users
        from app.routes.movies import movies
        from app.routes.reviews import reviews
        from app.routes.genres import genres
        from app.routes.followings import followings
        from app.routes.watched_movies import watched_movies
        from app.routes.subscribed_genres import subscribed_genres

        app.register_blueprint(home)
        app.register_blueprint(users)
        app.register_blueprint(movies)
        app.register_blueprint(reviews)
        app.register_blueprint(genres)
        app.register_blueprint(followings)
        app.register_blueprint(watched_movies)
        app.register_blueprint(subscribed_genres)
        
    if env == 'DEV':
        if os.environ.get('STARTUP_NEW_DB') == 'TRUE':
            db_utils.drop_and_create_db()
    elif env == 'TEST':
        db_utils.drop_and_create_db()

    db_utils.create_tables()
    
    return app
