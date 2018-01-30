# -*- coding: utf8 -*-
import os


class Config(object):
    """Parent configuration class
    """
    # mail server settings
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET', '#%$#%$^FDFGFGdf')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:@localhost:5432/microblog'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # administrator list
    ADMINS = ['dknderitu@gmail.com']

    # Pagination
    POSTS_PER_PAGE = 3

    # configuring whoose_base
    WHOOSH_BASE = os.path.join(basedir, 'search.db')

    MAX_SEARCH_RESULTS = 50

    LANGUAGES = {
        'en': 'English',
        'es': 'Espanol'
    }
    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'

    # microsoft translation service
    MS_TRANSLATOR_CLIENT_ID = '' # enter your MS translator app id here
    MS_TRANSLATOR_CLIENT_SECRET = '' # enter your MS translator app secret here


class DevelopmentConfig(Config):
    """Configurations for Development
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:@localhost:5432/microblog'


app_config = {
    'development': DevelopmentConfig,
    #You can add more configurations here
}



