class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    USER = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + USER + ':' + SECRET_KEY + '@localhost/adkintun'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
