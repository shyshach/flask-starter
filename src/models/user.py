from . import db
from .abc import BaseModel
from passlib.hash import pbkdf2_sha256 as sha256
import datetime


class User(db.Model, BaseModel):
    username = db.Column(
        db.String, primary_key=True, unique=True, nullable=False
    )
    avatar_url = db.Column(db.String, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    password = db.Column(db.String, nullable=True)

    def __init__(self, username: str, password: str, avatar_url: str = ''):
        self.username = username
        self.avatar_url = avatar_url
        self.password = password

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)