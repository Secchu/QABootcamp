from flask import render_template, request
from flask import redirect, url_for, flash
from app.writers import writers_bp
from app.extensions import db, getBulletNumFromBulletString
from app.models.models import writer, movie

@writers_bp.route("/", methods=['GET','POST'])
@writers_bp.route("/index", methods=['GET','POST'])
def index():

    order = request.args.get('order')

    #If the page URL is missing than supply default value of 1
    page = request.args.get('page', 1, type=int)

    pagination = None
    title = ""

    if order == "name":
        pagination = writer.query.order_by(writer.Writer_Name).paginate(page=page, per_page=5)
        title = "All Scriptwriters order by Name"
    else:
        pagination = writer.query.paginate(page=page, per_page=5)
        title = "All Scriptwriters"

    return render_template("writers/index.html", title=title,
                           pagination=pagination, order=order)

@writers_bp.route("/create", methods=['POST','GET'])
def create():
    if request.method == "POST":

        error = False

        #Even though we have the required attribute for this input text you could
        #enter white spaces and the form will be validated
        if request.form['name'].strip() == "":
            flash("Please enter the Script Writer's name")
            error = True

        writer_id = int(request.form['id'])

        if writer.query.get(writer_id) is not None:
            flash("The primary key has been taken. Please enter another")
            error = True

        if not error:
            Writer = writer(writer_id, request.form['name'])
            db.session.add(Writer)
            db.session.commit()

            return redirect(url_for('writers.writerDetails', Id=writer_id, action='add'))

    return render_template("writers/create.html")

@writers_bp.route("/<int:Id>")
def writerDetails(Id):

    Writer = writer.query.get_or_404(Id)

    if request.args.get("action") == "add":
        flash(f"New Script Writer with Id {Id} has been added")
    elif request.args.get('action') == "edit":
        flash(f"Script Writer with Id {Id} has been sucessfully edited")

    return render_template("writers/writer_details.html", writer=Writer)

@writers_bp.route("/edit/<int:Id>", methods=['POST','GET'])
def editwriter(Id):

    _writer = writer.query.get_or_404(Id)

    error = False

    if request.method == "POST":

        #Even though we have the required attribute for this input text you could
        #enter white spaces
        if request.form['name'].strip() == "":
            flash("The Writer's name cannot be blank")
            error = True

        if not error:
            _writer.writer_Name = request.form['name']
            db.session.commit()

            return redirect(url_for('writers.writerDetails', Id=Id, action='edit'))

    return render_template("writers/edit_writer.html", writer = _writer)

@writers_bp.route("/search", methods=['POST'])
def search():
    like_query = "%{}%".format(request.form['keyword'])
    _writers = writer.query.filter(
    writer.Writer_Name.like(like_query)).all()

    return render_template("writers/search.html",
               writers=_writers, keyword=request.form['keyword'])

@writers_bp.route("/<int:Id>/add_movie", methods=['GET', 'POST'])
def addMovie(Id):
    _writer = writer.query.get_or_404(Id)

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
                _writer.movie.append(_movie)
                movie_names.append(_movie.Movie_Title)

            db.session.commit()

            return render_template("writers/add_confirmation.html",
                   to=_writer.Writer_Name, added=movie_names)

    availableMovies = movie.query.filter(
    ~movie.moviescripts.contains(_writer)).all()

    return render_template("writers/add_movie.html",
           writer=_writer, movies=availableMovies)

@writers_bp.route("/delete/<int:Id>")
def delete(Id):

    _writer = writer.query.get(Id)

    if _writer is None:
        return f"Could not delete Writer with Id {Id}", 404

    db.session.delete(_writer)
    db.session.commit()

    return f"Successfully deleted Writer {_writer.Writer_Name} with Id {Id}", 200

@writers_bp.route("/<int:Id>/removeMovie/<int:movieId>")
def removeMovie(Id, movieId):

    _writer = writer.query.get(Id)

    if _writer is None:
        return f"Could not delete Writer with Id {Id}", 404

    _movie = movie.query.get(movieId)

    if _movie is None:
        return f"Movie with Id {movieId} could not be found"

    _writer.movie.remove(_movie)
    db.session.commit()

    msg = f"The movie {_movie.Movie_Title} is no longer written by {_writer.Writer_Name}"

    return msg, 200
