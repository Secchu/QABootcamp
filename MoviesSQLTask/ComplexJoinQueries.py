"""
This module contains all the SQL select query strings necessary to query many to
many relationship data from the Movies Schema. The structure of the schema is
defined in the MoviesSchema.sql in the SQLScripts directory. Because these queries
can be long and multilined it was best to include them in separate files as it
can clutter your main code and make it look complex when the truth is the code
is simple but the queries are long.

These queries are also contained in MovieComplexQueries.sql of the SQLScripts
directory. You can use MySQL Workbench or MySQL shell to test the queries
manually before running the code.
"""

moviesInHorrorAndThriller = """select movies.Movie_Title, movies.Duration from movies
left join categorizedmovie on categorizedmovie.FKMovie_ID = movies.Movie_ID right join
genre on categorizedmovie.FKCategory_ID = genre.Category_ID where genre.Category_Name = 'Horror'
or genre.Category_Name = 'Thriller'
"""

moviesBeginWithStar = "select Movie_Title from movies where Movie_Title like 'Star%'"

directedByScorsese = """select movies.Movie_Title, directors.Director_Name from movies left
join DirectedMovies on DirectedMovies.FKMovie_ID = movies.Movie_ID right join directors
on DirectedMovies.FKDirector_ID = directors.Director_ID where
directors.Director_Name = 'Martin Scorsese'
"""

writersOfHappyDeathDay = """select distinct writers.Writer_Name from writers left join
MovieScript on MovieScript.FKWriter_ID = writers.Writer_ID  right join movies on
MovieScript.FKMovie_ID = Movies.Movie_ID where Movies.Movie_Title like 'Happy Death Day%'
"""

justiceLeagueCast = """select MovieStars.Star_Name from movies left join MovieCast on
MovieCast.FKMovie_ID = Movies.Movie_ID right join MovieStars on
MovieCast.FKStar_ID = MovieStars.Star_ID where movies.Movie_Title = 'Justice League'
"""

swallowReviews = """select reviewers.Reviewer_Name, reviewers.city, ratings.Rating, ratings.review
from movies left join ratings on ratings.FKMovie_ID = movies.movie_ID right join reviewers on
ratings.FKReviewer_ID = reviewers.Reviewer_ID where movies.Movie_Title = 'Swallow'
"""

swallowReviewMaxRating = """select reviewers.Reviewer_Name, reviewers.city, ratings.Rating,
ratings.review from movies left join ratings on ratings.FKMovie_ID = movies.movie_ID
right join reviewers on ratings.FKReviewer_ID = reviewers.Reviewer_ID
where movies.Movie_Title = 'Swallow' order by ratings.Rating desc limit 1
"""

highlyRated = """select movies.Movie_Title, Reviewer_Name, reviewers.city, ratings.Rating, ratings.review
from movies left join ratings on ratings.FKMovie_ID = movies.movie_ID right join reviewers on
ratings.FKReviewer_ID = reviewers.Reviewer_ID where ratings.Rating > 7.5 order by ratings.Rating desc
"""

#A query that require joining four tables
actionReviews = """select Movie_Title, genre.Category_Name, Reviewer_Name, reviewers.city, ratings.Rating,
ratings.review from movies left join ratings on ratings.FKMovie_ID = movies.movie_ID right join reviewers on
ratings.FKReviewer_ID = reviewers.Reviewer_ID join CategorizedMovie on CategorizedMovie.FKMovie_ID = movies.Movie_ID
join genre on CategorizedMovie.FKCategory_ID = genre.Category_ID where genre.Category_Name = 'Action'
order by ratings.Rating
"""

joinQueries = (("Horror and tbriller movies", moviesInHorrorAndThriller )
               , ("Movies that begin with 'Star'", moviesBeginWithStar)
               , ("Movies directed by Martin Scorsese", directedByScorsese)
               , ("Writers of the Happy Death Day Franchise", writersOfHappyDeathDay)
               , ("The cast of Justice League", justiceLeagueCast)
               , ("All Reviews of Movie Swallow", swallowReviews)
               , ("Swallow Highest Rated Review", swallowReviewMaxRating)
               , ("Rated Reviews above 7.5", highlyRated)
               , ("All Action Movie Reviews in order", actionReviews))



