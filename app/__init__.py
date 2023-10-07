import os

from flask import Flask
from sqlalchemy import create_engine, inspect
from flask_sqlalchemy import SQLAlchemy
# from flask_bootstrap import Bootstrap5

# -------------
# Configuration
# -------------

db = SQLAlchemy()
# bootstrap = Bootstrap5()

#-----------------------------
# Application Factory Function
#-----------------------------

def create_app(config_filename=None):
    # Flask application instance
    app = Flask(__name__)
    
    # Flask application configuration
    config_type = os.getenv("CONFIG_TYPE", default='config.DevelopementConfig')
    app.config.from_object(config_type)
    
    db.init_app(app)
    # bootstrap.init_app(app)
    register_blueprints(app)
    
    # DB initialization check
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    inspector = inspect(engine)
    # TODO: add tables to check
    # if not inspector.has_table("") or not inspector.has_table(""):
    #     with app.app_context():
    #         db.drop_all()
    #         db.create_all()
    #         print("Database initialized.")
    # else:
    #     print("Database already contains metadata table")
    
    return app

# ----------------
# Helper Functions
# ----------------

def register_blueprints(application):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    
    from app.conekta import conekta_blueprint
    application.register_blueprint(conekta_blueprint)
    
def register_cli_commands(app):
    @app.cli.command('init_db')
    def initialize_database():
        db.drop_all()
        db.create_all()
        print('Database initialized.')