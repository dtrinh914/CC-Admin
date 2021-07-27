from app.database import db_connection
from app.database.movies import *
from app.database.users import *


@db_connection.error_handler
def create_tables():
    """Create the tables for the application if they do not already exist."""
    conn = db_connection.get_conn()
    cur = conn.cursor()

    create_users = """CREATE TABLE IF NOT EXISTS users(
                        user_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        username VARCHAR(255) NOT NULL UNIQUE,
                        password VARCHAR(255) NOT NULL
                    )"""

    create_movies = """CREATE TABLE IF NOT EXISTS movies(
                        movie_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        title VARCHAR(255) NOT NULL UNIQUE,
                        avg_review_score DECIMAL(2,1) DEFAULT 0.0
                    )"""

    create_reviews = """CREATE TABLE IF NOT EXISTS reviews(
                            review_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                            author_id INT,
                            movie_id INT NOT NULL,
                            review_text VARCHAR(2000) NOT NULL,
                            review_score INT NOT NULL,
                            FOREIGN KEY (author_id) REFERENCES users(user_id) ON DELETE CASCADE,
                            FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE
                    )"""

    create_watched_movies = """CREATE TABLE IF NOT EXISTS watched_movies(
                                watched_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                movie_id INT NOT NULL,
                                user_id INT NOT NULL,
                                FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE,
                                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
                                UNIQUE relationship (movie_id, user_id)
                            )"""

    create_followings = """CREATE TABLE IF NOT EXISTS followings(
                            following_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                            follower_id INT NOT NULL,
                            followee_id INT NOT NULL,
                            FOREIGN KEY (follower_id) REFERENCES users(user_id) ON DELETE CASCADE,
                            FOREIGN KEY (followee_id) REFERENCES users(user_id) ON DELETE CASCADE,
                            UNIQUE relationship (follower_id, followee_id),
                            CONSTRAINT no_self_follow CHECK (follower_id <> followee_id)
                        )"""

    create_genres = """CREATE TABLE IF NOT EXISTS genres(
                            genre_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                            genre_name VARCHAR(255) NOT NULL
                    )"""
    
    create_subscribed_genres = """CREATE TABLE IF NOT EXISTS subscribed_genres(
                                    subscribed_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                                    user_id INT NOT NULL,
                                    genre_id INT NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
                                    FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE,
                                    UNIQUE relationship (user_id, genre_id)
                                )"""
    cur.execute(create_users)
    cur.execute(create_movies)
    cur.execute(create_reviews)
    cur.execute(create_watched_movies)
    cur.execute(create_followings)
    cur.execute(create_genres)
    cur.execute(create_subscribed_genres)

    conn.close()


@db_connection.error_handler
def drop_and_create_db():
    """Drop and create a new db."""
    conn = db_connection.get_conn()
    cur = conn.cursor()
    db_name = db_connection.db_name
    cur.execute(f'DROP DATABASE IF EXISTS {db_name}')
    cur.execute(f'CREATE DATABASE IF NOT EXISTS {db_name}')
    conn.close()
