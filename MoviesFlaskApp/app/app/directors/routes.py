from flask import render_template, request
from flask import redirect, url_for, flash
from app.directors import directors_bp
from app.extensions import db, getBulletNumFromBulletString
from app.models.models import director, movie

@directors_bp.route("/", methods=['GET','POST'])
@directors_bp.route("/index", methods=['GET','POST'])
def index():

    order = request.args.get('order')

    #If the page URL is missing than supply default value of 1
    page = request.args.get('page', 1, type=int)

    pagination = None
    title = None

    if order == "name":
        pagination = director.query.order_by(director.Director_Name).paginate(page=page, per_page=5)
        title = "All Directors order by Name"
    else:
        pagination = director.query.paginate(page=page, per_page=5)
        title = "All Directors"

    return render_template("directors/index.html", title=title,
                           pagination=pagination, order=order)

@directors_bp.route("/create", methods=['POST','GET'])
def create():
    if request.method == "POST":

        error = False

        #Even though we have the required attribute for this input text you could
        #enter white spaces and the form will be validated
        if request.form['name'].strip() == "":
            flash("Please enter the Director's name")
            error = True

        director_id = int(request.form['id'])

        if director.query.get(director_id) is not None:
            flash("The primary key has been taken. Please enter another")
            error = True

        if not error:
            _director = director(director_id, request.form['name'])
            db.session.add(_director)
            db.session.commit()

            return redirect(url_for('directors.directorDetails', Id=director_id, action='add'))



    return render_template("directors/create.html")

@directors_bp.route("/<int:Id>")
def directorDetails(Id):

    _director = director.query.get_or_404(Id)

    if request.args.get("action") == "add":
        flash(f"New Director with Id {Id} has been added")
    elif request.args.get('action') == "edit":
        flash(f"Director with Id {Id} has been sucessfully edited")

    return render_template("directors/director_details.html", director=_director)

@directors_bp.route("/edit/<int:Id>", methods=['POST','GET'])
def editDirector(Id):

    _director = director.query.get_or_404(Id)

    error = False

    if request.method == "POST":

        #Even though we have the required attribute for this input text you could
        #enter white spaces
        if request.form['name'].strip() == "":
            flash("The director name cannot be blank")
            error = True

        if not error:
            _director.Director_Name = request.form['name']
            db.session.commit()

            return redirect(url_for('directors.directorDetails', Id=Id, action='edit'))

    return render_template("directors/edit_director.html", director = _director)

@directors_bp.route("/search", methods=['POST'])
def search():
    like_query = "%{}%".format(request.form['keyword'])

    _directors = director.query.filter(
    director.Director_Name.like(like_query)).all()

    return render_template("directors/search.html",
                           directors=_directors, keyword=request.form['keyword'])

@directors_bp.route("/<int:Id>/add_movie", methods=['GET', 'POST'])
def addMovie(Id):
    _director = director.query.get_or_404(Id)

    if request.method == "POST":
        selected = request.form.get('Selected')

        if not selected:
            flash("You must select atleast one movie from the list")
        else:
            _movies = request.form.to_dict(flat=False)

            movie_names = getBulletNumFromBulletString(_movies['Selected'])

            movie_ids = []

            for Id in movie_ids:
                _movie = movie.query.get(Id)
                _director.movies.append(_movie)
                movie_names.append(_movie.Movie_Title)

            db.session.commit()

            return render_template("directors/add_confirmation.html",
                   to=_director.Director_Name, added=movie_names)

    availableMovies = movie.query.filter(
    ~movie.directed_movies.contains(_director)).all()

    return render_template("directors/add_movie.html",
           director=_director, movies=availableMovies)

@directors_bp.route("/delete/<int:Id>")
def delete(Id):
    _director = director.query.get(Id)

    if _director is None:
        return f"Director with Id {Id} could not be deleted", 404

    db.session.delete(_director)
    db.session.commit()

    return f"Director {_director.Director_Name} with Id {Id} has been successfully deleted", 200

@directors_bp.route("/<int:Id>/removeMovie/<int:movieId>")
def removeMovie(Id, movieId):

    _director = director.query.get(Id)

    if _director is None:
        return f"Director with Id {Id} could not be found"

    _movie = movie.query.get(movieId)

    if _movie is None:
        return f"Movie with Id {movieId} could not be found"

    _director.movie.remove(_movie)
    db.session.commit()

    msg = f"The movie {_movie.Movie_Title} is no longer directed by {_director.Director_Name}"

    return msg, 200