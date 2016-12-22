from extensions import db
from flask import Blueprint

class Author(db.Document):
    name = db.StringField()

class Book(db.Document):
    title = db.StringField()
    author = db.DocumentField(Author)
    year = db.IntField();


author_bp = Blueprint('author', __name__)

