from app.database import db_connection

@db_connection.error_handler
def get_follow_list():
    """retrieves followings data from db"""

    conn = db_connection.get_conn()
    cur = conn.cursor(dictionary=True)

    query = (
        'SELECT f.following_id as following_id, f.date_created as date_created,\n'
        'users.user_id as follower_id, users2.user_id as followee_id,\n' 
        'users.username as follower_name, users2.username as followee_name\n'
        'FROM followings f\n'
        'JOIN users ON users.user_id = f.follower_id\n'
        'INNER JOIN users users2 ON users2.user_id = f.followee_id\n'
    )
    cur.execute(query)

    res = cur.fetchall()
    conn.close()

    return res

@db_connection.error_handler
def add_to_following(follower_id, followee_id):
    """adds to followings db"""

    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = (
        'INSERT INTO followings\n'
        '(follower_id, followee_id)\n'
        'VALUES (?,?)'
    )
    cur.execute(query, (follower_id, followee_id))

    conn.close()
    return True

@db_connection.error_handler
def edit_followings(follower_id: int, followee_id: int, following_id:int):
    """Edits watched movies"""

    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'UPDATE followings SET follower_id=?, followee_id=? WHERE following_id=?'
    cur.execute(query, (follower_id, followee_id, following_id))
    conn.close()
    
    return True

@db_connection.error_handler
def delete_followings(following_id):
    """deletes followings row from database"""
    
    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = f'DELETE FROM followings WHERE following_id=?'
    cur.execute(query, (following_id,))
    conn.close()

    return True