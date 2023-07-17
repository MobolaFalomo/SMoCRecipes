from.import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class user(db.Model, UserMixin):
    id = db.Column(db.Integer, Primary_key=True)
    email = db.Column(db.String(150), Unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

