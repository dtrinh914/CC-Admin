from app.database import db_connection

@db_connection.error_handler
def get_reviews_api():
    """retrieves username data"""
    conn = db_connection.get_conn()
    cur = conn.cursor(dictionary = True)
    query = (
            'SELECT reviews.review_id as review_id, reviews.date_created as data_created,\n'
            'users.user_id as author_id, movies.movie_id as movie_id,\n'
            'users.username as author_name\n'
            ', movies.title as movie_title, reviews.review_text as review_text,\n'
            'reviews.review_score as review_score\n'
            'FROM reviews\n'
            'LEFT JOIN users ON reviews.author_id = users.user_id \n'
            'JOIN movies ON reviews.movie_id = movies.movie_id'
            )
            
    cur.execute(query)
    review_list = cur.fetchall()
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
    """Delete review database info"""

    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'DELETE FROM reviews WHERE review_id=?'
    cur.execute(query, (int(review_id),))
    conn.close()
    return True