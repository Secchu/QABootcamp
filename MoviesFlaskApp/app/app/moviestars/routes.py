from flask import render_template, request
from flask import redirect, url_for, flash
from app.moviestars import moviestars_bp
from app.extensions import db, getBulletNumFromBulletString
from app.models.models import moviestar, movie

@moviestars_bp.route("/", methods=['GET','POST'])
@moviestars_bp.route("/index", methods=['GET','POST'])
def index():

    order = request.args.get('order')

    #If the page URL is missing than supply default value of 1
    page = request.args.get('page', 1, type=int)

    pagination = None
    title = ""

    if order == "name":
        pagination = moviestar.query.order_by(moviestar.Star_Name).paginate(page=page, per_page=5)
        title = "All Moviestars order by Name"
    else:
        pagination = moviestar.query.paginate(page=page, per_page=5)
        title = "All Moviestars"

    return render_template("moviestars/index.html", title=title,
                           pagination=pagination, order=order)

@moviestars_bp.route("/create", methods=['POST','GET'])
def create():
    if request.method == "POST":

        error = False

        #Even though we have the required attribute for this input text you could
        #enter white spaces and the form will be validated
        if request.form['name'].strip() == "":
            flash("Please enter the Script star's name")
            error = True

        star_Id = int(request.form['id'])

        if moviestar.query.get(star_Id) is not None:
            flash("The primary key has been taken. Please enter another")
            error = True

        if not error:
            star = moviestar(star_Id, request.form['name'])
            db.session.add(star)
            db.session.commit()

            return redirect(url_for('moviestars.moviestarDetails', Id=star_Id, action='add'))

    return render_template("moviestars/create.html")

@moviestars_bp.route("/<int:Id>")
def moviestarDetails(Id):

    star = moviestar.query.get_or_404(Id)

    if request.args.get("action") == "add":
        flash(f"New Movie Star with Id {Id} has been added")
    elif request.args.get('action') == "edit":
        flash(f"Moviestar with Id {Id} has been sucessfully edited")

    return render_template("moviestars/moviestar_details.html", star=star)

@moviestars_bp.route("/edit/<int:Id>", methods=['POST','GET'])
def editMoviestar(Id):

    _moviestar = moviestar.query.get_or_404(Id)

    error = False

    if request.method == "POST":

        #Even though we have the required attribute for this input text you could
        #enter white spaces
        if request.form['name'].strip() == "":
            flash("The moviestar name cannot be blank")
            error = True

        if not error:
            _moviestar.Star_Name = request.form['name']
            db.session.commit()

            return redirect(url_for('moviestars.moviestarDetails', Id=Id, action='edit'))

    return render_template("moviestars/edit_moviestar.html", star = _moviestar)

@moviestars_bp.route("/search", methods=['POST'])
def search():
    like_query = "%{}%".format(request.form['keyword'])

    stars = moviestar.query.filter(
    moviestar.Star_Name.like(like_query)).all()

    return render_template("moviestars/search.html",
                           moviestars=stars, keyword=request.form['keyword'])

@moviestars_bp.route("/<int:Id>/add_movie", methods=['GET', 'POST'])
def addMovie(Id):
    _moviestar = moviestar.query.get_or_404(Id)

    if request.method == "POST":
        selected = request.form.get('Selected')

        if not selected:
            flash("You must select atleast one movie from the list")
        else:
            _movies = request.form.to_dict(flat=False)

            movie_ids = getBulletNumFromBulletString(_movies['Selected'])

            movie_names = []

            for Id in movie_ids:
                _movie = movie.query.get(Id)
                _moviestar.movie.append(_movie)
                movie_names.append(_movie.Movie_Title)

            db.session.commit()

            return render_template("moviestars/add_confirmation.html",
                   to=_moviestar.Star_Name, added=movie_names)

    availableMovies = movie.query.filter(
    ~movie.cast.contains(_moviestar)).all()

    return render_template("moviestars/add_movie.html",
           moviestar=_moviestar, movies=availableMovies)

@moviestars_bp.route("/delete/<int:Id>")
def delete(Id):

    star = moviestar.query.get(Id)

    if star is None:
        return f"Could not delete moviestar with Id {Id}", 404

    db.session.delete(star)
    db.session.commit()

    return f"Successfully deleted moviestar {star.Star_Name} with Id {Id}", 200

@moviestars_bp.route("/<int:Id>/removeMovie/<int:movieId>")
def removeMovie(Id, movieId):

    star = moviestar.query.get(Id)

    if star is None:
        return f"Could not delete moviestar with Id {Id}", 404

    _movie = movie.query.get(movieId)

    if _movie is None:
        return f"Movie with Id {movieId} could not be found"

    star.movie.remove(_movie)
    db.session.commit()

    msg = f"{star.Star_Name} no longer stars in {_movie.Movie_Title}"

    return msg, 200
