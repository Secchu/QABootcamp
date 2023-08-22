from flask import Flask, render_template, request, flash
from flask import redirect, url_for, abort
from app.movies import movies_bp
from app.extensions import db, getBulletNumFromBulletString
from app.models.models import movie, genre, director
from app.models.models import writer, moviestar

@movies_bp.route("/")
@movies_bp.route("/index")
def index():

    order = request.args.get('order')

    #If the page URL is missing than supply default value of 1
    page = request.args.get('page', 1, type=int)

    pagination = None
    title = ""

    if order == "title":
        pagination = movie.query.order_by(movie.Movie_Title).paginate(page=page, per_page=5)
        title = "All Movies order by Title"
    elif order == "year":
        pagination = movie.query.order_by(movie.Year.desc()).paginate(page=page, per_page=5)
        title="All Movies order by Year"
    elif order == "duration":
        pagination = movie.query.order_by(movie.Duration).paginate(page=page, per_page=5)
        title = "All Movies order by Duration"
    else:
        pagination = movie.query.paginate(page=page, per_page=5)
        title = "All Movies"

    return render_template("movies/index.html",title=title,
                           category="", year="",
                           pagination=pagination, order=order)

@movies_bp.route("/genre/<category>")
def genres(category):
    _genre = genre.query.filter(genre.Category_Name == category).first()

    if _genre is None:
        return abort(404)


    order = request.args.get('order')

    #If the page URL is missing than supply default value of 1
    page = request.args.get('page', 1, type=int)

    pagination = None
    title = ""

    if order == "title":
        pagination = movie.query.filter(
                     movie.categories.contains(
                     _genre)).order_by(movie.Movie_Title).paginate(page=page,per_page=5)

        title = f"{category} Movies order by Title"

    elif order == "year":
        pagination = movie.query.filter(
                     movie.categories.contains(
                    _genre)).order_by(movie.Year).paginate(page=page,per_page=5)

        title = f"{category} Movies order by Year"

    elif order == "duration":
        pagination = movie.query.filter(
                     movie.categories.contains(
                     _genre)).order_by(movie.Duration).paginate(page=page,per_page=5)

        title = f"{category} Movies order by Duration"

    else:
        pagination = movie.query.filter(
                 movie.categories.contains(_genre)).paginate(page=page,per_page=5)

        title = f"{category} Movies"

    return render_template("movies/index.html", title=title,
                           category=category, year="",
                           pagination=pagination, order=order)

@movies_bp.route("/year/<int:year>")
def movie_by_year(year):
    _movies = movie.query.filter(movie.Year == year).all()

    order = request.args.get('order')

    #If the page URL is missing than supply default value of 1
    page = request.args.get('page', 1, type=int)

    pagination = None
    title = ""

    #Note there is no order by year because we just filtered by year

    if order == "title":
        pagination = movie.query.filter(movie.Year== year).order_by(
        movie.Year).paginate(page=page,per_page=5)

        title = f"{year} Movies order by Title"

    elif order == "duration":
        pagination = movie.query.filter(movie.Year == year).order_by(
        movie.Duration).paginate(page=page,per_page=5)

        title = f"{year} Movies order by Duration"

    else:
        pagination = movie.query.filter(
        movie.Year == year).paginate(page=page,per_page=5)

        title = f"{year} Movies"

    return render_template("movies/index.html", title=title,
                           category="year", year=year,
                           pagination=pagination, order=order)



@movies_bp.route("/create", methods=['POST','GET'])
def create():

    if request.method == "POST":

        error = False

        #Even though we have the required attribute for this input text you could
        #enter white spaces
        if request.form['title'].strip() == "":
            flash("Please enter a title for the movie")
            error = True

        movie_id = int(request.form['id'])

        if movie.query.get(movie_id) is not None:
            flash("The primary key has been taken. Please enter another")
            error = True

        if not error:
            year = int(request.form['year'])
            duration = int(request.form['duration'])
            _movie = movie(movie_id, request.form['title'], duration, year)
            db.session.add(_movie)
            db.session.commit()

            return redirect(url_for('movies.movieDetails', Id=movie_id, action='add'))


    return render_template("movies/create.html")

@movies_bp.route("/<int:Id>")
def movieDetails(Id):

    _movie = movie.query.get_or_404(Id)

    if request.args.get("action") == "add":
        flash(f"New movie with {Id} has been sucessfully added")
    elif request.args.get('action') == "edit":
        flash(f"Movie with {Id} has been sucessfully edited")

    return render_template("movies/movie_details.html", movie=_movie)

@movies_bp.route("/edit/<int:Id>", methods=['POST','GET'])
def editMovie(Id):

    _movie = movie.query.get_or_404(Id)

    error = False

    if request.method == "POST":

        #Even though we have the required attribute for this input text you could
        #enter white spaces
        if request.form['title'].strip() == "":
            flash("The title of the movie cannot be blank")
            error = True

        if not error:
            _movie.Movie_Title = request.form['title']
            _movie.Duration = int(request.form['duration'])
            _movie.Year = int(request.form['year'])

            db.session.commit()

            return redirect(url_for('movies.movieDetails', Id=Id, action='edit'))

    return render_template("movies/edit_movie.html", movie = _movie)

@movies_bp.route("/search", methods=['POST'])
def search():
    like_query = "%{}%".format(request.form['keyword'])
    _movies = movie.query.filter(
    movie.Movie_Title.like(like_query)).all()

    return render_template("movies/search.html", movies=_movies,
    keyword=request.form['keyword'])

@movies_bp.route("/<int:movieId>/add_director", methods=['POST','GET'])
def addDiretor(movieId):

    _movie = movie.query.get_or_404(movieId)

    if request.method == "POST":
        selected = request.form.get('Selected')

        if not selected:
            flash("You must select atleast one director from the list")
        else:
            #We need to parse the request data as a list. We cannot
            #use dictionary because the select options cannot be parsed
            #with the same key since it has to be unique. We end up with
            #a dictionary that has a list as the value

            #Refer to stackoverflow for more information about this problem.
            #https://stackoverflow.com/questions/40566757
            #/how-to-get-multiple-selected-items-from-form-in-flask
            _directors = request.form.to_dict(flat=False)

            director_ids = getBulletNumFromBulletString(_directors['Selected'])

            director_names = []

            for Id in director_ids:
                _director = director.query.get(Id)
                _movie.directed_movies.append(_director)
                director_names.append(_director.Director_Name)

            db.session.commit()

            return render_template("movies/add_confirmation.html",
                   to=_movie.Movie_Title, added=director_names)

    availableDirectors = director.query.filter(~director.movie.contains(_movie)).all()

    return render_template("movies/add_director.html",
           movie=_movie, directors=availableDirectors)

@movies_bp.route("/<int:movieId>/add_writer", methods=['POST','GET'])
def addWriter(movieId):

    _movie = movie.query.get_or_404(movieId)

    if request.method == "POST":
        selected = request.form.get('Selected')

        if not selected:
            flash("You must select atleast one writer from the list")
        else:
            _writers = request.form.to_dict(flat=False)

            writer_ids = getBulletNumFromBulletString(_writers['Selected'])

            writer_names = []

            for Id in writer_ids:
                _writer = writer.query.get(Id)
                _movie.moviescripts.append(_writer)
                writer_names.append(_writer.Writer_Name)

            db.session.commit()

            return render_template("movies/add_confirmation.html",
                   to=_movie.Movie_Title, added=writer_names)

    availableWriters = writer.query.filter(~writer.movie.contains(_movie)).all()

    return render_template("movies/add_writer.html",
           movie=_movie, writers=availableWriters)

@movies_bp.route("/<int:movieId>/add_cast", methods=['POST','GET'])
def addCast(movieId):

    _movie = movie.query.get_or_404(movieId)

    if request.method == "POST":
        selected = request.form.get('Selected')

        if not selected:
            flash("You must select atleast one moviestar from the list")
        else:
            _stars = request.form.to_dict(flat=False)

            star_ids = getBulletNumFromBulletString(_stars['Selected'])

            star_names = []

            for Id in star_ids:
                star = moviestar.query.get(Id)
                _movie.cast.append(star)
                star_names.append(star.Star_Name)

            db.session.commit()

            return render_template("movies/add_confirmation.html",
                   to=_movie.Movie_Title, added=star_names)

    availableCast = moviestar.query.filter(~moviestar.movie.contains(_movie)).all()

    return render_template("movies/add_cast.html",
           movie=_movie, moviestars=availableCast)

@movies_bp.route("/<int:movieId>/add_genre", methods=['POST','GET'])
def addGenre(movieId):

    _movie = movie.query.get_or_404(movieId)

    if request.method == "POST":
        selected = request.form.get('Selected')

        if not selected:
            flash("You must select atleast one genre category from the list")
        else:
            _genres = request.form.to_dict(flat=False)

            genre_ids = getBulletNumFromBulletString(_genres['Selected'])

            genre_names = []

            for Id in genre_ids:
                _genre = genre.query.get(Id)
                _movie.categories.append(_genre)
                genre_names.append(_genre.Category_Name)

            db.session.commit()

            return render_template("movies/add_confirmation.html",
                   to=_movie.Movie_Title, added=genre_names)

    availableGenre = genre.query.filter(~genre.movie.contains(_movie)).all()

    return render_template("movies/add_genre.html",
           movie=_movie, genres=availableGenre)

@movies_bp.route("/delete/<int:Id>")
def delete(Id):

    _movie = movie.query.get(Id)

    if _movie is None:
        return f"Movie with Id {Id} could not be found", 404

    db.session.delete(_movie)
    db.session.commit()

    return f"Movie {_movie.Movie_Title} with Id {Id} has been successfully deleted", 200

@movies_bp.route("/<int:Id>/removeGenre/<int:genreId>")
def removeGenre(Id, genreId):
    _movie = movie.query.get(Id)

    if _movie is None:
        return f"Movie with Id {Id} could not be found", 404

    _genre = genre.query.get(genreId)

    if _genre is None:
        return f"Genre with Id {genreId} could not be found", 404

    _movie.categories.remove(_genre)

    db.session.commit()

    return f"Movie with Id {Id} no longer belongs to the genre category with Id {genreId}", 200

@movies_bp.route("/<int:Id>/removeCast/<int:starId>")
def removeCast(Id, starId):
    _movie = movie.query.get(Id)

    if _movie is None:
        return f"Movie with Id {Id} could not be found", 404

    star = moviestar.query.get(starId)

    if star is None:
        return f"Moviestar with Id {starId} could not be found", 404

    _movie.cast.remove(star)
    db.session.commit()

    return f"The moviestar {star.Star_Name} no longer stars in {_movie.Movie_Title}", 200

@movies_bp.route("/<int:Id>/removeDirector/<int:directorId>")
def removeDirector(Id, directorId):
    _movie = movie.query.get(Id)

    if _movie is None:
        return f"Movie with Id {Id} could not be found", 404

    _director = director.query.get(directorId)

    if _director is None:
        return f"Director with Id {directorId} could not be found", 404

    _movie.directed_movies.remove(_director)
    db.session.commit()

    return f"The director {_director.Director_Name} no longer directs {_movie.Movie_Title}", 200

@movies_bp.route("/<int:Id>/removeWriter/<int:writerId>")
def removeWriter(Id, writerId):
    _movie = movie.query.get(Id)

    if _movie is None:
        return f"Movie with Id {Id} could not be found", 404

    _writer = writer.query.get(writerId)

    if _writer is None:
        return f"Writer with Id {writerId} could not be found", 404

    _movie.moviescripts.remove(_writer)
    db.session.commit()

    return f"The Writer {_writer.Writer_Name} no longer wrote the script for movie {_movie.Movie_Title}", 200
