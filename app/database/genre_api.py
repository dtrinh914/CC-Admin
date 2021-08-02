from app.database import db_connection

@db_connection.error_handler
def get_genre_names():
    """retrieves genre name data from genres database"""
    conn = db_connection.get_conn()
    cur = conn.cursor(dictionary=True)
    query = ('SELECT * FROM genres ORDER BY genre_id')
    cur.execute(query)
    genre_names  = cur.fetchall()
    conn.close()

    return genre_names

@db_connection.error_handler
def add_db_genre(genre_name):
    """adds all genres to genre table"""
    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'INSERT into genres (genre_name) VALUES (?)'
    cur.execute(query, (genre_name,))
    conn.close()
    return True

@db_connection.error_handler
def add_genre_subscribe(genre_id, user_id):  
    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'INSERT INTO subscribed_genres (genre_id, user_id) VALUES (?,?)'
    cur.execute(query, (int(genre_id), int(user_id))) 
    conn.close()
    return True

@db_connection.error_handler
def delete_genres(id):
    """deletes from genres list"""
    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'DELETE FROM genres WHERE genre_id = ?'
    cur.execute(query, (int(id), ))
    conn.close()

    return True

@db_connection.error_handler
def update_genres(genre_id, genre_name):
    """updates genre in genres using id"""
    
    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'UPDATE genres SET genre_name=? where genre_id=?'
    cur.execute(query, (genre_name, int(genre_id)))
    conn.close()
    return True

### Subscribed genres
@db_connection.error_handler
def delete_subscribed_genres(id):
    """deletes subscribed genres row"""
    conn = db_connection.get_conn()
    cur = conn.cursor()

    cur.execute(f'DELETE FROM subscribed_genres WHERE subscribed_id = {id}')
    return True

@db_connection.error_handler
def update_subscribed_genres(user_id, genre_id, subscribed_id):
    """updates subscribed_genre user_id and genre_id"""

    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = ('UPDATE subscribed_genres SET user_id=?, genre_id=?\n'
                'WHERE subscribed_id =?')
    cur.execute(query, (int(user_id), int(genre_id), int(subscribed_id)))
    conn.close()

    return True

db_connection.error_handler
def get_subscribed_genres():
    """retrieves subscribed genres"""

    conn = db_connection.get_conn()
    cur = conn.cursor(dictionary=True)
    query = ('SELECT subscribed_id, users.user_id as user_id, genres.genre_id as genre_id,\n'
            'users.username as username, genres.genre_name as genre_name\n'
            'FROM subscribed_genres\n'
            'JOIN users ON subscribed_genres.user_id = users.user_id\n'
            'JOIN genres ON subscribed_genres.genre_id = genres.genre_id\n'
            'ORDER BY subscribed_id'
            )
    cur.execute(query)
    res = cur.fetchall()
    conn.close()

    return res