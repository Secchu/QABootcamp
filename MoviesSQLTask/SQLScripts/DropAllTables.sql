USE QABootcamp;

-- You can run this SQL script before running the Python demo code. It will remove all tables leaving
-- you with an empty schema
-- Drop the junction tables first so we don't run into errors related to foreign key constraints

SET FOREIGN_KEY_CHECKS=0;

drop table MovieStars;
drop table CategorizedMovie;
drop table MovieCast;
drop table MovieScript;
drop table DirectedMovies;
drop table ratings;
drop table movies;
drop table Genre;
drop table directors;
drop table writers;
drop table reviewers;


