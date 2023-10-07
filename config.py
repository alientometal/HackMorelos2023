import os
from uuid import uuid4

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    FLASK_ENV = 'developement'
    DEBUG = False
    TESTING = False
    # TODO: 'default' can be any string, if problems arrise, change it.
    SECRET_KEY = os.getenv('SECRET_KEY', default=str(uuid4()))
    
    if os.getenv('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    else:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASEDIR, 'instance', 'app.db')}"
        
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # TODO: Logging?
    
class ProductionConfig(Config):
    FLASK_ENV = 'production'
    
class DevelopementConfig(Config):
    DEBUG = True
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI',
                                        default=f"sqlite:///{os.path.join(BASEDIR, 'instance', 'test.db')}")
    WTF_CSRF_ENABLED = False
    