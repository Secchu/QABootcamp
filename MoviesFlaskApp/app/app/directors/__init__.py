from flask import Blueprint

directors_bp = Blueprint('directors', __name__)

from app.directors import routes
