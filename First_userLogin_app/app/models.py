from app import db
from flask_login import UserMixin
from app import login_manager

class User(db.Model, UserMixin):
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))