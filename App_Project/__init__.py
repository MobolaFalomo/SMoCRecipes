from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '081013'
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')







    return app

