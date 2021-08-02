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


@db_connection.error_handler
def get_watched_list(user_id: int) -> list:
    """Retrieves a user's watched list.

    Args:
        user_id: user id

    Returns:
        A list of a user's watched movies
    """
    conn = db_connection.get_conn()
    cur = conn.cursor(dictionary=True)
    query = """
            SELECT movies.movie_id, movies.title FROM movies
            JOIN watched_movies ON watched_movies.movie_id = movies.movie_id
            WHERE watched_movies.user_id=?
            """

    cur.execute(query, (user_id,))
    data = cur.fetchall()
    conn.close()
    return data


@db_connection.error_handler
def add_to_watched_list(user_id: int, movie_id: int) -> bool:
    """Adds a movie to a user's watched list

    Args:
        user_id: user id
        movie_id: movie id

    Returns:
        True if successful else return None
    """
    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'INSERT INTO watched_movies(user_id, movie_id) VALUES (?,?)'
    cur.execute(query, (user_id, movie_id))
    conn.close()
    return True


@db_connection.error_handler
def remove_from_watched_list(user_id: int, movie_id: int) -> bool:
    """Remove a movie from a user's watched list

    Args:
        user_id: user id
        movie_id: movie id

    Returns:
        True if successful else return None
    """
    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'DELETE FROM watched_movies WHERE user_id=? and movie_id=?'
    cur.execute(query, (user_id, movie_id))
    conn.close()
    return True


# watched movies
@db_connection.error_handler
def get_watched_movies():
    """retrieves watched movies"""
    conn = db_connection.get_conn()
    cur = conn.cursor(dictionary = True)

    query = ('SELECT watched_id, watched_movies.date_created as date_created, users.username as username, movies.title as movie_title\n'
            'FROM watched_movies\n'
            'INNER JOIN users ON watched_movies.user_id\n'
            'INNER JOIN movies ON watched_movies.movie_id\n'
            'WHERE users.user_id = watched_movies.user_id AND\n'
            'movies.movie_id = watched_movies.movie_id')

    cur.execute(query)
    response = cur.fetchall()
    conn.close()
    return jsonify(response)

@db_connection.error_handler
def add_watched_movies(user_id, movie_id):
    """adds watched movie using user_id and movie_id"""

    query = ('INSERT INTO watched_movies movie_id, user_id\n'
            ' VALUES (?,?)')
    conn = db_connection.get_conn()
    cur = conn.cursor(dictionary = True)
    

    cur.execute(query, (movie_id, user_id))
    conn.close()
    return True

@db_connection.error_handler
def delete_watched_movies(id):
    """deletes row from watched_movies"""
    