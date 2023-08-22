from flask import Blueprint

moviestars_bp = Blueprint('moviestars', __name__)

from app.moviestars import routes