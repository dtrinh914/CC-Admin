import os
from dotenv.main import load_dotenv
import requests
from requests.models import Response
from app.database import db_connection
from dotenv import load_dotenv, find_dotenv
import json
from flask import session, jsonify
load_dotenv(find_dotenv())
api_key = os.environ.get("TMDB_APIKEY")
host_name = 'https://api.themoviedb.org/3'



@db_connection.error_handler
def get_reviews_api():
    """retrieves username data"""
    conn = db_connection.get_conn()
    cur = conn.cursor(dictionary = True)
    query = (
            'SELECT reviews.review_id as review_id, reviews.date_created as\n'
            'data_created, users.username as author_name\n'
            ', movies.title as movie_title, reviews.review_text as review_text,\n'
            'reviews.review_score as review_score\n'
            'FROM reviews\n'
            'INNER JOIN users ON reviews.author_id\n'
            'INNER JOIN movies ON reviews.movie_id\n'
            'WHERE users.user_id = reviews.author_id AND\n'
            'movies.movie_id = reviews.movie_id\n')
    
    cur.execute(query)
    review_list = cur.fetchall()
    review_list = jsonify(review_list)
    conn.close()

    return review_list

@db_connection.error_handler
def add_reviews(author_id, movie_id, review_text, review_score):
    """adds to reviews"""
    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = (
        'INSERT INTO reviews (author_id, movie_id, review_text, review_score)\n'
        'VALUES (?,?,?,?)'
    )
    cur.execute(query, (author_id,movie_id,review_text,review_score))
    conn.close()

    return True

@db_connection.error_handler
def edit_reviews(review_id:int,author_id:int, movie_id:int, review_text, review_score:int ):
    """edits reviews"""

    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = ('UPDATE reviews SET author_id=?, movie_id=?\n'
    ', review_text=?, review_score=? WHERE review_id=?')
    cur.execute(query, (author_id, movie_id,review_text,review_score, review_id ))
    conn.close()
    return True
# SELECT * FROM reviews JOIN users ON reviews.review_id where author_id = user_id;

@db_connection.error_handler
def delete_reviews(review_id: int) -> bool:
    """Delete review data"""

    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'DELETE FROM reviews WHERE review_id=?'
    cur.execute(query, (int(review_id),))
    conn.close()
    return True