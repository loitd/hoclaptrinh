class DevelopmentConfig(object):
    # all config: https://flask.palletsprojects.com/en/1.1.x/config/
    ENV = 'development' #production
    DEBUG = True
    TESTING = True
    SESSION_COOKIE_SECURE=False
    SESSION_COOKIE_HTTPONLY=True
    SESSION_COOKIE_SAMESITE='Lax'
    SECRET_KEY = "34567890-cvnbm,./tyijlk;67890vbnm,;ltyuilk.,"