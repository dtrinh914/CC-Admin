import os
from dotenv.main import load_dotenv
import requests
from requests.models import Response
from app.database import db_connection
from dotenv import load_dotenv, find_dotenv
import json
from flask import session
load_dotenv(find_dotenv())
api_key = os.environ.get("TMDB_APIKEY")
host_name = 'https://api.themoviedb.org/3'




def get_genre_list():
    """gets current list of movie genres from TMDB
        Returns list of dictionaries with keys: 'id' and 'name' """
    
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US'

    try:
        # send get request to retrieve genre list
        response = requests.get(url)
        response = response.json()
        
        # list of genres with id 
        genre_details = response['genres']
        
        return genre_details
    except requests.exceptions.RequestException as e:
        print(f'Error in retrieving data from {url}:{e}')

@db_connection.error_handler
def add_db_genre():
    """adds all genres to genre table"""
    genre_list = get_genre_list()
    genre_ids = {}
    genre_names = []

    for i in genre_list:
        genre_ids[i['name']] = i['id']
        genre_names.append(i['name'])

    conn = db_connection.get_conn()
    cur = conn.cursor()
    name = None
    
    #query = 'INSERT INTO genres (genre_name) VALUES (?)'
    # fixed so it doesn't add duplicates.
    for name in genre_names:
        cur.execute(f'insert into genres (genre_name) select "{name}" where not exists (select * from genres where genre_name = "{name}");')
        #cur.execute(query, (name,))

    conn.close()

    return True

@db_connection.error_handler
def get_subscribed_list():
    """returns list of subscribed genres"""
    conn = db_connection.get_conn()
    cur = conn.cursor(dictionary=True)
    query = (f'SELECT genre_id FROM subscribed_genres WHERE user_id = {session["user_id"]}')
    cur.execute(query)
    genre_ids = cur.fetchall()
    id_list = []
    for key in genre_ids:
        id_list.append(key['genre_id'])
    
    # now get list of genre names that are subscribed
    genre_names = []

    for id in id_list:
        cur.execute(f'SELECT genre_name from genres where genre_id ={id}')
        current_id = cur.fetchone()
        genre_names.append(current_id['genre_name'])

    conn.close()
    
    return genre_names

@db_connection.error_handler
def add_genre_subscribe(genre_name, username):  
    # query = (f'INSERT INTO subscribed_genres (user_id, genre_id)\n'
    # f'values ((SELECT user_id FROM users WHERE username ="{username}"),\n'
    # f'(SELECT genre_id FROM genres WHERE genre_name ="{genre_name}"))')

    query = (f'INSERT INTO subscribed_genres (user_id, genre_id)\n'
    f'values ((SELECT user_id FROM users WHERE username ="{username}"),\n'
    f'(SELECT genre_id FROM genres WHERE genre_name ="{genre_name}"))')

    conn = db_connection.get_conn()
    cur = conn.cursor()
    cur.execute(query) 

    conn.close()
    return True

    # INSERT INTO subscribed_genres (user_id, genre_id) 
    # values ((SELECT user_id FROM users 
    # WHERE username = 'jesse'),
    # (SELECT genre_id FROM genres WHERE genre_name = 'Drama'));

@db_connection.error_handler
def remove_genre_subscribe(name):
    """removes subscribed genre"""
    conn = db_connection.get_conn()
    cur = conn.cursor()

    for genre in name:
        cur.execute(f'DELETE from subscribed_genres WHERE genre_id\n'
        f'=(SELECT genre_id FROM genres where genre_name = "{genre}")\n'
        f'AND user_id = {session["user_id"]}')
    conn.close()

