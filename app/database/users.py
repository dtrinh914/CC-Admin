from app.database import db_connection

@db_connection.error_handler
def get_users() -> list:
    """Retrieves all users from the database

    Returns:
        List containing all users
    """
    conn = db_connection.get_conn()
    cur = conn.cursor(dictionary=True)
    query = 'SELECT * FROM users'
    cur.execute(query)
    user_data = cur.fetchall()
    conn.close()
    return user_data

@db_connection.error_handler
def add_user(username: str, password: str) -> bool:
    """Adds a user to the Users table.
    
    Args:
        username: name of user
        password: password hash for the user

    Returns:
        True if successful else returns error string.
    """
    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'INSERT INTO users (username,password) VALUES (?,?)'
    cur.execute(query, (username, password))
    conn.close()
    return True

@db_connection.error_handler
def edit_user(user_id: int, username: str, password: str) -> bool:
    """Edits a user in the table.
    
    Args:
        user_id: user id
        username: name of user
        password: password hash for the user

    Returns:
        True if successful else returns error string.
    """
    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'UPDATE users SET username=?, password=? WHERE user_id=?'
    cur.execute(query, (username, password, int(user_id)))
    conn.close()
    return True

@db_connection.error_handler
def delete_user(user_id: int) -> bool:
    """Removes a user from the table.
    
    Args:
        user_id: user id

    Returns:
        True if successful else returns error string.
    """
    conn = db_connection.get_conn()
    cur = conn.cursor()
    query = 'DELETE FROM users WHERE user_id=?'
    cur.execute(query, (user_id, ))
    conn.close()
    return True

@db_connection.error_handler
def search_user(search_str: str) -> list:
    """Retrieves all users whose username matches a search string.

    Args:
        search_str: username search string

    Returns:
        A list of user data that match the search string.
    """
    conn = db_connection.get_conn()
    cur = conn.cursor(dictionary=True)
    query = 'SELECT * FROM users WHERE username LIKE %s'
    cur.execute(query, ('%' + search_str + '%',))
    user_data = cur.fetchall()
    conn.close()
    return user_data
