from src.models import Movie
from app import db
# TODO - Create SQLAlchemy DB and Movie model
class Movie(db.Model):
    __tablename__ = 'movie'
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    director = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)