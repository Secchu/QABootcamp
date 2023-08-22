from flask import Flask, render_template, request, flash
from app.genres import genres_bp
from app.extensions import db
from app.models.models import genre

def validateForm():
        error = False

        #Even though we have the required attribute for this input text you could
        #enter white spaces
        if request.form['category'].strip() == "":
            flash("Category cannot be empty")
            error = True

        _genre = genre.query.filter(
                 genre.Category_Name == request.form['category']).first()

        if _genre is not None:
            flash(f"category name has to be unique")
            error = True

        return error

@genres_bp.route("/")
def index():

    _genres = genre.query.all()

    return render_template("genres/index.html", genres=_genres)

@genres_bp.route("/edit/<int:Id>", methods=['GET','POST'])
def editGenre(Id):

    _genre = genre.query.get_or_404(Id)

    if request.method == "POST":
        error = validateForm()

        if not error:
            _genre.Category_Name = request.form['category']
            db.session.commit()

            return render_template("genres/editConfirmation.html",
                                   genre=_genre)

    return render_template("genres/editGenre.html", genre=_genre)

@genres_bp.route("/create", methods=['GET','POST'])
def create():

    if request.method == "POST":

        error = validateForm()

        genre_id = int(request.form['id'])

        if genre.query.get(genre_id) is not None:
            flash("The primary key has been taken. Please enter another")
            error = True

        if not error:
            new_genre = genre(genre_id, request.form['category'])
            db.session.add(new_genre)
            db.session.commit()

            return render_template("genres/add_confirmation.html", genre=new_genre)


    return render_template("genres/create.html")

@genres_bp.route("/delete/<int:Id>")
def delete(Id):

    _genre = genre.query.get(Id)

    if _genre is None:
        return f"Genre with Id {Id} could not be deleted", 404

    db.session.delete(_genre)
    db.session.commit()

    return f"Category {_genre.Category_Name} with Id {Id} has been successfully deleted", 200