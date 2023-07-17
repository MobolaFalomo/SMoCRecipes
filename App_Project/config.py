import os

basedir = os.path.abspath(os.path.dirname(__file__)


class Config:
    SQLALCHEMY_DATABASE_URL = 'sqlite:///' + \
            os.path.join(basedir, 'new.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
