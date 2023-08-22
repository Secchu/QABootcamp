USE qabootcamp;

select movies.Movie_Title, movies.Duration from movies left join categorizedmovie on 
categorizedmovie.FKMovie_ID = movies.Movie_ID right join genre on categorizedmovie.FKCategory_ID = genre.Category_ID where 
genre.Category_Name = 'Horror' or genre.Category_Name = 'Thriller';

-- Select all movie titles that begin with Star. This will return all the star wars movies
select Movie_Title from movies where Movie_Title like 'Star%';

-- Show all movies directed by Martin Scorsese. If you used inserts in the MovieInserts.sql file than the query
-- will return the Goodfellas and the Casino
select movies.Movie_Title, directors.Director_Name from movies left join DirectedMovies on 
DirectedMovies.FKMovie_ID = movies.Movie_ID right join directors on 
DirectedMovies.FKDirector_ID = directors.Director_ID where directors.Director_Name = 'Martin Scorsese';

-- Select the writers that help write the comedy Happy Death Day and Happy Death Day 2 U. Note the query will
-- return Scott Lobdell and Christopher Landon. Scott Lobdell help write both movies so we need the distinct keyword
select distinct writers.Writer_Name from writers left join MovieScript on MovieScript.FKWriter_ID = writers.Writer_ID
right join movies on MovieScript.FKMovie_ID = Movies.Movie_ID where Movies.Movie_Title like 'Happy Death Day%'; 

-- Display all the cast in Justice League
select MovieStars.Star_Name from movies left join MovieCast on MovieCast.FKMovie_ID = Movies.Movie_ID
right join MovieStars on MovieCast.FKStar_ID = MovieStars.Star_ID where movies.Movie_Title = 'Justice League';

-- Display all the reviews for the movie Swallow
select reviewers.Reviewer_Name, reviewers.city, ratings.Rating, ratings.review from movies left join ratings 
on ratings.FKMovie_ID = movies.movie_ID right join reviewers on ratings.FKReviewer_ID = reviewers.Reviewer_ID
where movies.Movie_Title = 'Swallow';

-- Display the max rating review for the movie swallow.
select reviewers.Reviewer_Name, reviewers.city, ratings.Rating, ratings.review from movies left join ratings 
on ratings.FKMovie_ID = movies.movie_ID right join reviewers on ratings.FKReviewer_ID = reviewers.Reviewer_ID
where movies.Movie_Title = 'Swallow' order by ratings.Rating desc limit 1;

-- Display all ratings, reviews along with the movie title being reviewed that has a rating of 7.5 or above order by ratings
select movies.Movie_Title, Reviewer_Name, reviewers.city, ratings.Rating, ratings.review from movies left join ratings 
on ratings.FKMovie_ID = movies.movie_ID right join reviewers on ratings.FKReviewer_ID = reviewers.Reviewer_ID
where ratings.Rating > 7.5 order by ratings.Rating desc;

-- This query joins a total of 4 tables and we can go further if we wish ie we haven't used the having and group by clause
-- to sort the movies. The query return all reviews for the action movies. 
select Movie_Title, genre.Category_Name, Reviewer_Name, reviewers.city, ratings.Rating, ratings.review from movies 
left join ratings on ratings.FKMovie_ID = movies.movie_ID right join reviewers on ratings.FKReviewer_ID = reviewers.Reviewer_ID
join CategorizedMovie on CategorizedMovie.FKMovie_ID = movies.Movie_ID join genre 
on CategorizedMovie.FKCategory_ID = genre.Category_ID where genre.Category_Name = 'Action' order by ratings.Rating; 
