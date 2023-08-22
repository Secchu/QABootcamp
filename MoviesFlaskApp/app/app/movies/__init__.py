from flask import Blueprint

movies_bp = Blueprint('movies', __name__)

from app.movies import routes