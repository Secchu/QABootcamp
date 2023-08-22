from flask import Flask, request, render_template
from config import Config
from app.extensions import db
from app.models.models import movie, director, writer
from app.models.models import moviestar, genre, review

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    from app.extensions import db
    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app.main import main_bp
    app.register_blueprint(main_bp)

    from app.movies import movies_bp
    app.register_blueprint(movies_bp, url_prefix='/movies')

    from app.directors import directors_bp
    app.register_blueprint(directors_bp, url_prefix="/directors")

    from app.writers import writers_bp
    app.register_blueprint(writers_bp, url_prefix="/writers")

    from app.moviestars import moviestars_bp
    app.register_blueprint(moviestars_bp, url_prefix="/moviestars")

    from app.reviews import reviews_bp
    app.register_blueprint(reviews_bp, url_prefix="/reviews")

    from app.genres import genres_bp
    app.register_blueprint(genres_bp, url_prefix="/genres")

    @app.route('/test/')
    def test_page():
        return """<h1>Test Page for development purposes only</h1>

                  <h3>Author: Sec Chu</h3>

               """

    @app.context_processor
    def genres():
        return dict(genres=genre.query.all())

    return app

