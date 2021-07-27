import os
import mariadb
from functools import wraps
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Set the variables in our application with those environment variables
db_host = os.environ.get("DBHOST")
db_user = os.environ.get("DBUSER")
db_password = os.environ.get("DBPW")
db_name = os.environ.get("DB")

def get_conn(host: str = db_host, user: str = db_user, password: str = db_password, name: str = db_name):
    """Connects to a database and returns a database objects"""
    try:
        conn = mariadb.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=name,
                    autocommit=True,
                )
        return conn
    except mariadb.Error as e:
        print(f'Error connecting to MariaDB Platform: {e}')
        return str(e)



def error_handler(func):
    """Decorator that wraps function with a try/except block and handles database errors.

    Args:
        func: function

    Returns:
        A decorated function.
    """
    @wraps(func)
    def wrapper_error_handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except mariadb.Error as e:
            print(f'Error in {func.__name__}: {e}')
            return str(e)

    return wrapper_error_handler
