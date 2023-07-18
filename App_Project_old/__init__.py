from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '081013'
    app.config.from_object(Config)


    from .models import User
    
    with app.app_context():
        app = SQLALchemy(app)
        db.create_all()

        login_manager = LoginManager()
        login_manager.login_view = 'auth.login'
        login_manager.init_app(app)
        migrate = Migrate(app, db)

        from App_Project import views, models

        @login_manager.user_loader
        def load_user(id):
            return User.query.get(int(id))

    return app
app = create_app()
