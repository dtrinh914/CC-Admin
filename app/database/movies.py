from app.database import db_connection
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from flask import jsonify

@db_connection.error_handler
def get_movies() -> list:
    """Retrieves all users from the database

    Returns:
        List containing all users
    """
    conn = db_connection.get_conn()
    cur = conn.cursor(dictionary=True)
    query = 'SELECT * FROM movies'
    cur.execute(query)
    movie_data = cur.fetchall()
    conn.close()
    return movie_data

@db_connection.error_handler
def add_movie(movie_title: str, avg_review_score: float) -> bool:
    """Adds movie data to the database.

    Args:
        movie_title: movie title
        avg_review_score: average review score

    Returns:
        True if successful else returns error string.
    """
    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'INSERT INTO movies (title, avg_review_score) VALUES (?,?)'
    cur.execute(query, (movie_title, avg_review_score))
    conn.close()
    return True

def edit_movie(movie_id: int, movie_title: str, avg_review_score: float) -> bool:
    """Edits movie data to the database.

    Args:
        movie_id: movie id
        movie_title: movie title
        avg_review_score: average review score

    Returns:
        True if successful else returns error string.
    """
    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'UPDATE movies SET title=?, avg_review_score=? WHERE movie_id=?'
    cur.execute(query, (movie_title, avg_review_score, int(movie_id)))
    conn.close()
    return True


def delete_movie(movie_id: int) -> bool:
    """Delete movie data from the database.

    Args:
        movie_id: movie id

    Returns:
        True if successful else returns error string.
    """
    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'DELETE FROM movies WHERE movie_id=?'
    cur.execute(query, (int(movie_id),))
    conn.close()
    return True

# watched movies
@db_connection.error_handler
def get_watched_movies():
    """retrieves watched movies"""
    conn = db_connection.get_conn()
    cur = conn.cursor(dictionary = True)

    query = ('SELECT watched_id, watched_movies.user_id as user_id, watched_movies.movie_id as movie_id, \n'
            'watched_movies.date_created as date_created, users.username as username, movies.title as movie_title\n'
            'FROM watched_movies\n'
            'JOIN users ON users.user_id = watched_movies.user_id\n'
            'JOIN movies ON movies.movie_id = watched_movies.movie_id'
            )

    cur.execute(query)
    response = cur.fetchall()
    conn.close()
    return jsonify(response)

@db_connection.error_handler
def add_watched_movies(user_id, movie_id):
    """adds watched movie using user_id and movie_id"""

    query = ('INSERT INTO watched_movies (movie_id, user_id) VALUES (?,?)')
    conn = db_connection.get_conn()
    cur = conn.cursor(dictionary = True)
    

    cur.execute(query, (movie_id, user_id))
    conn.close()
    return True

@db_connection.error_handler
def delete_watched_movies(id):
    """deletes row from watched_movies"""

    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'DELETE FROM watched_movies WHERE watched_id = ?'
    cur.execute(query, (int(id),))
    conn.close()

    return True

@db_connection.error_handler
def edit_watched_movies(watched_id: int, movie_id: str, user_id: float) -> bool:
    """Edits watched movies"""

    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'UPDATE watched_movies SET movie_id=?, user_id=? WHERE watched_id=?'
    cur.execute(query, (int(movie_id), int(user_id), int(watched_id)))
    conn.close()
    return True