# CouchCritique Admin
Group 12 cs340 project

1. Activate virtualenv.
2. Run 'pip install -r requirements.txt' to install dependencies. (MariaDB is also required for the application)
3. Rename .env-example to .env and edit the file with your DB configs.
4. To start app in debug mode for development run 'python3 wsgi.py'.
5. To deploy app using gunicorn run 'gunicorn wsgi:handler'.