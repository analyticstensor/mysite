from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
import datetime
import jwt
from flask import current_app
from time import time
from werkzeug.security import generate_password_hash


db = SQLAlchemy()

class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False, unique=False)
    last_name = db.Column(db.String(20), nullable=False, unique=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False, unique=False)
    created_on = db.Column(db.DateTime, default=db.func.now())
    last_login = db.Column(db.DateTime, default=db.func.now(), index=False, nullable=True, unique=False)

    def get_id(self)-> str:
        """
        Overwrite `get_id`, since default `id` is changed to `user_id`.
        :return user_id int: User id is the attribute in user table.
        """
        return self.user_id

    def update_last_login(self):
        self.last_login = datetime.datetime.now()
        db.session.commit()

    def get_forget_password_token(self, expiry=300):
        return jwt.encode({'forget_password': self.user_id, 'exp': time() + expiry}, key=current_app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_forget_password_token(token):
        try:
            user_id = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])['forget_password']
        except:
            return
        return User.query.get(user_id)

    def hash_password(self, password):
        self.password = generate_password_hash(password, 'sha256')