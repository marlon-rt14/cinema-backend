from http.client import ACCEPTED, CREATED

from flask import Blueprint, request

from helpers.error_handler import error_handler
from helpers.responses import bad_response, success_response
from models.models import Movie
from utils.db import db

movies = Blueprint('movies', __name__)

@movies.route('', methods=['GET'])
def get_movies():
    try:
        movies = Movie.query.all()
        data = [ movie.serialize() for movie in movies]
        return success_response(data, msg='Movies retrieved successfully', ok=True, status=ACCEPTED) 
    except Exception as e:
        return error_handler(e)

@movies.route('/<int:id>', methods=['GET'])
def get_movie(id):
    try:
        movie = Movie.query.get_or_404(id)
        data = movie.serialize()
        return success_response(data, msg='Movie retrieved successfully', ok=True, status=ACCEPTED) 
    except Exception as e:
        return error_handler(e)

@movies.route('/<int:id>', methods=['DELETE'])
def delete_movie():
    try:
        movie = Movie.query.get_or_404(id)
        db.session.delete(movie)
        db.session.commit()
        return success_response(msg='Movie deleted successfully', ok=True, status=CREATED) 
    except Exception as e:
        return error_handler(e)

@movies.route('', methods=['POST'])
def create_movie():
    try:
        movie = Movie(**request.json)
        db.session.add(movie)
        db.session.commit()
        return success_response(msg='Movie created successfully', ok=True, status=CREATED) 
    except Exception as e:
        return error_handler(e)

@movies.route('/<int:id>', methods=['PUT'])
def update_movie():
    try:
        movie = Movie.query.get_or_404(id)
        movie.update(**request.json)
        db.session.commit()
        return success_response(msg='Movie updated successfully', ok=True, status=ACCEPTED) 
    except Exception as e:
        return error_handler(e)