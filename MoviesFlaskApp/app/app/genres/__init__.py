from flask import Blueprint

genres_bp = Blueprint('genres', __name__)

from app.genres import routes