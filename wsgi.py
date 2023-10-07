# TODO Filename must be changed to app

from app import create_app

# Call the application factory function to construct a Flask application
# instance using the development configuration
app = create_app('flask.cfg')
