from app.extensions import db

CategorizedMovie = db.Table('CategorizedMovie', db.metadata,
                   db.Column('Movie_ID', db.Integer, db.ForeignKey('movie.Movie_ID')),
                   db.Column('Category_ID', db.Integer, db.ForeignKey('genre.Category_ID')))

MovieCast = db.Table('MovieCast',
            db.Column('Movie_ID', db.Integer, db.ForeignKey('movie.Movie_ID')),
            db.Column('Star_ID', db.Integer, db.ForeignKey('moviestar.Star_ID')))

MovieScript =  db.Table('MovieScript', db.metadata,
               db.Column('Movie_ID', db.Integer, db.ForeignKey('movie.Movie_ID')),
               db.Column('Writer_ID', db.Integer, db.ForeignKey('writer.Writer_ID')))

DirectedMovies = db.Table('DirectedMovies', db.metadata,
               db.Column('Movie_ID', db.Integer, db.ForeignKey('movie.Movie_ID')),
               db.Column('Director_ID', db.Integer, db.ForeignKey('director.Director_ID')))


class movie(db.Model):
    Movie_ID = db.Column(db.Integer, primary_key=True)
    Movie_Title = db.Column(db.String(100), nullable=False)
    Duration = db.Column(db.Integer, nullable=False)
    Year = db.Column(db.Integer, nullable=False)

    directed_movies = db.relationship('director', secondary=DirectedMovies, backref='movie')
    categories = db.relationship('genre', secondary=CategorizedMovie, backref='movie')

    cast = db.relationship('moviestar', secondary=MovieCast, backref='movie')
    moviescripts = db.relationship('writer', secondary=MovieScript, backref='movie')

    movie_rating = db.relationship('review', backref='movie')

    def __init__(self, Movie_ID, Movie_Title, Duration, Year):
        self.Movie_ID = Movie_ID
        self.Movie_Title = Movie_Title
        self.Duration = Duration
        self.Year = Year

    def __repr__(self):
        return f'<Movie "{self.Movie_Title} Duration: {self.Duration} Year: {self.Year}">'

class director(db.Model):
    Director_ID = db.Column(db.Integer, primary_key=True)
    Director_Name = db.Column(db.String(100), nullable=False)

    def __init__(self, Director_ID, Director_Name):
        self.Director_ID = Director_ID
        self.Director_Name = Director_Name

    def __repr__(self):
        return f'<Director "{self.Director_Name}">'

class writer(db.Model):
    Writer_ID = db.Column(db.Integer, primary_key=True)
    Writer_Name = db.Column(db.String(100), nullable=False)

    def __init__(self, Writer_ID, Writer_Name):
        self.Writer_ID = Writer_ID
        self.Writer_Name = Writer_Name

    def __repr__(self):
        return f'<Writer "{self.Writer_Name}">'

class moviestar(db.Model):
    Star_ID = db.Column(db.Integer, primary_key=True)
    Star_Name = db.Column(db.String(100), nullable=False)

    def __init__(self, Star_ID, Star_Name):
        self.Star_ID = Star_ID
        self.Star_Name = Star_Name

    def __repr__(self):
        return f'<Star "{self.Star_Name}">'

class genre(db.Model):
    Category_ID = db.Column(db.Integer, primary_key=True)
    Category_Name = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, Category_ID, Category_Name):
        self.Category_ID = Category_ID
        self.Category_Name = Category_Name

    def __repr__(self):
        return f'<Category "{self.Category_Name}">'

class review(db.Model):
    Reviewer_ID = db.Column(db.Integer, primary_key=True)
    Reviewer_Name = db.Column(db.String(100), nullable=False)
    City = db.Column(db.String(100), nullable=False)
    Review = db.Column(db.Text, nullable=False)
    Rating = db.Column(db.Float, nullable=False)
    Movie_ID = db.Column(db.Integer, db.ForeignKey('movie.Movie_ID'), nullable=False)

    def __init__(self, Movie_ID, Reviewer_ID, Reviewer_Name,
                 City, Review, Rating):
                    self.Movie_ID = Movie_ID
                    self.Reviewer_ID = Reviewer_ID
                    self.Reviewer_Name = Reviewer_Name
                    self.City = City
                    self.Review = Review
                    self.Rating = Rating

    def __repr__(self):
        return f'<Reviewer {self.Reviewer_Name} from {self.City} {self.Review}>'

