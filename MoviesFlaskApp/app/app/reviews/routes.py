from flask import render_template, request
from flask import redirect, url_for, flash
from app.reviews import reviews_bp
from app.extensions import db
from app.models.models import review, movie

def validateReviewForm():
    error = False

    if request.form['name'].strip() == "":
        error = True
        flash("Name cannot be blank")
    if request.form['city'].strip() == "":
        error = True
        flash("City cannot be blank")
    if request.form['review'].strip() == "":
        error = True
        flash("Review cannot be blank")

    return error


@reviews_bp.route("add/<int:MovieId>",
methods=['POST','GET'])
def addReview(MovieId):

    _movie = movie.query.get_or_404(MovieId)

    if request.method == "POST":

        error = validateReviewForm()

        reviewId = int(request.form['reviewid'])

        reviewed = review.query.get(reviewId)

        if reviewed is not None:
            error = True
            flash(f"Select another Review ID. {reviewId} has been taken")

        if not error:
            rating = float(request.form['rating'])

            _review = review(MovieId, reviewId, request.form['name'],
                             request.form['city'], request.form['review'],
                             rating)

            db.session.add(_review)
            db.session.commit()

            msg = "Your review has been successfully added."

            return render_template("reviews/confirmation.html",
                                    review=_review, movie=_movie,
                                    msg=msg)

    return render_template("reviews/review.html", movie=_movie)

@reviews_bp.route('edit/<int:reviewId>', methods=['GET','POST'])
def editReview(reviewId):

    print(request.referrer)
    _review = review.query.get_or_404(reviewId)

    _movie = movie.query.get_or_404(_review.Movie_ID)

    if request.method == "POST":
        error = validateReviewForm()

        if not error:
            _review.Reviewer_Name = request.form['name']
            _review.City = request.form['city']
            _review.Rating = float(request.form['rating'])
            _review.Review = request.form['review']

            db.session.commit()

            msg = f"Your review with Id {reviewId} has been successfully edited"

            return render_template("reviews/confirmation.html",
                                   review=_review, movie=_movie,
                                   msg=msg)


    return render_template("reviews/edit_review.html",
                           review=_review, movie=_movie)

@reviews_bp.route('delete/<int:Id>')
def delete(Id):

    _review = review.query.get(Id)

    if _review is None:
        return F"Review with Id {Id} could not be found", 404

    db.session.delete(_review)
    db.session.commit()

    return f"Review by {_review.Reviewer_Name} with Id {Id} has been successfully deleted", 200