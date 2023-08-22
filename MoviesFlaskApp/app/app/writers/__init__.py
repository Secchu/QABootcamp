from flask import Blueprint

writers_bp = Blueprint('writers', __name__)

from app.writers import routes
