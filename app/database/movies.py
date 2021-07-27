import os
import requests
from app.database import db_connection
from dotenv import load_dotenv, find_dotenv

from app.database.genre_api import get_genre_list
load_dotenv(find_dotenv())
api_key = os.environ.get("TMDB_APIKEY")
host_name = 'https://api.themoviedb.org/3'


def search_movies(search_str: str, page_num: int = 1) -> dict:
    """Retrieves the JSON data containing a list of movies from a given search string.

    Args:
        search_str: search string
        page_num: page number of results from API (defaults to first page)

    Returns:
        JSON data containing a list of movies.
    """
    
    search_str = search_str.replace(' ', '%20')
    page_num = str(page_num)
    url = f'{host_name}/search/movie?api_key={api_key}' \
          f'&language=en-US&query={search_str}' \
          f'&page={page_num}&include_adult=false'

    try:
        response = requests.get(url)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Error in retrieving data from {url}:{e}')
        return {}


def get_api_movie_data(movie_id: str) -> dict:
    """Retrieves the JSON data of a movie.

    Args:
        movie_id: string of movie id

    Returns:
        JSON data of the movie.
    """
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'

    try:
        response = requests.get(url)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Error in retrieving data from {url}:{e}')
        return {}


@db_connection.error_handler
def get_db_movie_data_by_title(movie_title: str) -> dict:
    """Retrieves movie data from the database by the title.

    Args:
        movie_title: movie title

    Returns:
        True if successful else return None.
    """
    conn = db_connection.get_conn()
    cur = conn.cursor(dictionary=True)
    query = 'SELECT * FROM movies WHERE title=?'
    cur.execute(query, (movie_title,))
    data = cur.fetchone()
    conn.close()

    return data


@db_connection.error_handler
def get_db_movie_data_by_id(movie_id: int) -> dict:
    """Retrieves movie data from the database by id.

    Args:
        movie_id: movie id

    Returns:
        True if successful else return None.
    """
    conn = db_connection.get_conn()
    cur = conn.cursor(dictionary=True)
    query = 'SELECT * FROM movies WHERE movie_id=?'
    cur.execute(query, (movie_id,))
    data = cur.fetchone()
    conn.close()

    return data


@db_connection.error_handler
def add_db_movie(movie_title: str) -> bool:
    """Retrieves the movie data from the database.

    Args:
        movie_title: movie title

    Returns:
        Dictionary of the movie data.
    """
    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'INSERT INTO movies (title) VALUES (?)'
    cur.execute(query, (movie_title, ))
    conn.close()
    return True


@db_connection.error_handler
def check_if_watched(user_id: int, movie_id: int) -> bool:
    """Check if a movie is in a user's watched list.

    Args:
        user_id: user id
        movie_id: movie id

    Returns:
        True if the movie is in the user's watched list else returns False.
    """
    conn = db_connection.get_conn()
    cur = conn.cursor(dictionary=True)
    query = 'SELECT COUNT(*) as count FROM watched_movies WHERE user_id = ? AND movie_id = ?'
    cur.execute(query, (user_id, movie_id))
    data = cur.fetchone()
    conn.close()

    if data['count'] > 0:
        return True
    else:
        return False


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
