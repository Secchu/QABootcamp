from app.main import main_bp
from flask import render_template
from app.extensions import db

@main_bp.route('/')
@main_bp.route('/index')
def index():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template("about.html")