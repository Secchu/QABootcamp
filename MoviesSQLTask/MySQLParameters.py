"""
This module defines SQL insert query string parameters and tuple arguments that are
used in the mysql.connector executemany method for the QABootcamp schema.
The schema consists of several tables that describe the required schema for a Movies
database that has several many to many relationships. The database used is MySQL. The
mysql.connector is used to connect to the schema.

The method executemany() is an better option than execute() when there are many inserts to perform
on the mysql database.

For the schema of the QABootcamp database which is the schema used in this demo please refer
to the SQLScripts/MoviesSchema.sql file.

For examples of SQL insert statements please refer to the SQLScripts/MoviesInit.sql file.

To test this demo you have to make sure the schema is empty. This is because of the auto_increment
feature. If we start deleting or adding data then our foreign keys won't match and we will get errors.

You can create an empty schema using the SQL CREATE SCHEMA statement

CREATE SCHEMA QABootcamp

If you have tables in your schema previously you can run DropAllTables.sql to remove all tables. Note that
this SQL Statement will remove all your data and tables without warning. Please make sure you don't require any
data in the table if you use the SQL statement DROP TABLE.
"""

genre_insert_query = "INSERT INTO genre (Category_Name) VALUES (%s)"

#We have already inserted Action and Adventure to demonstrate how to perform inserts using
#the execute() method. We will perform the remaining inserts using executemany()
genres = (("Action",),("Adventure",),("Animation",),("Crime",),("Drama",),("Comedy",),("Fantasy",),("Thriller",)
          ,("Horror",),("Psychological",),("Romance",),("Western",),("Sci-Fi",),("Mystery",))

movies_insert_query = "insert into Movies (Movie_Title, Duration) values (%s, %s)"

movies = (("The flash", 140), ("Man of Steel", 145), ("Justice League", 240), ("Justice League War World", 90)
         , ("Scooby Doo Spooky Games", 25), ("Ambulance", 140), ("Goodfellas", 145), ("Casino", 180), ("Ugram", 145)
         , ("The Out Laws", 95), ("Love Hard", 105), ("One Rangar", 90), ("Hypnotic", 93), ("Happy Death Day", 95)
         , ("Happy Death Day 2U", 95), ("Run Rabbit Run", 95), ("The Black Demon", 100), ("Swallow", 95),("Intrusion", 92)
         , ("Hypnotic", 88), ("Love Again", 105), ("My Fault", 117), ("Chemical Hearts", 93), ("Blood & Gold", 100),("The Old Way", 95)
         , ("True Grit", 110), ("Star Wars IV A New Hope", 105), ("Star Wars V Empire Strikes Back", 124)
         , ("Star Wars VI Return of the Jedi", 131), ("Transformers", 144), ("Transformers: Revenge of the Fallen", 149)
         , ("Missing", 131), ("The Pale Blue Eye", 128), ("Luther: The Fallen Sun", 129))

directors_insert_query = "insert into directors (Director_Name) values (%s)"

directors = (("Andy Muschietti",), ("Zack Snyder",),("Jeremy Adams",),("Ernie Altbacker",),("Josie Campbell",)
             ,("Curt Geda",),("Michael Bay",),("Martin Scorsese",),("Vijay Kanakamedala",),("Tyler Spindel",)
             ,("Hernán Jiménez",),("Jesse V. Johnson",),("Robert Rodriguez",),("Christopher Landon",),("Daina Reid",)
             ,("Adrian Grunberg",),("Carlos Mirabella Davis",),("Adam Salky",),("Matt Angel",),("Suzanne Coote",)
             ,("Jim Strouse",),("Domingo Gonzalez",),("Richard Tanne",),("Peter Thorwarth",),("Brett Donowho",)
             ,("Ethan Coen",),("Joel Coen",),("George Lucas",),("Irwin Kreshner",),("Richard Marquand",),("Nicholas D. Johnson",)
             ,("Will Merrick",),("Scott Cooper",),("Jamie Payne",))

writers_insert_query = "insert into Writers (Writer_Name) values (%s)"

writers = (("Christina Hodson",),("John Francis Daley",),("Jonathan Goldstein",),("David Goye",),("Christopher Nolan",),("Jerry Siegel",)
           ,("Joe Shuster",),("Abburi Ravi",),("Zack Snyder",),("Jeremy Adams",),("Ernie Altbacker",),("Josie Campbell",)
           ,("Mark Banker",),("Chris Fedak",),("Laurits Punch-Petersen",),("Lars Andreas Pedersen",),("Martin Scorsese",)
           ,("Nicholas Pileggi",),("Vijay Kanakamedala",),("Ben Zazove",),("Evan Turner",),("Danny Mackey",),("Rebecca Ewing",)
           ,("Jesse V. Johnson",),("Robert Rodriguez",), ("Max Borenstein",),("Scott Lobdell",),("Christopher Landon",),("Hannah Kent",)
           ,("Carlos Cisco",),("Boise Esquerra",),("Carlos Mirabella Davis",),("Chris Sparling",),("Richard D'Ovidio",),("Jim Strouse",)
           ,("Sofie Kramer",),("Andrea Wilson",),("Domingo Gonzalez",),("Mercedes Ron",),("Richard Tanne",)
           ,("Krystal Sutherland",),("Peter Thorwarth",),("Stefan Barth",),("Carl W Lucas",),("Ethan Coen",),("Joel Coen",)
           ,("Charles Portis",),("George Lucas",),("Leigh Brackett",),("Lawrance Kasdan",),("Roberto Orci",),("Alex Kurtzman",)
           ,("John Rogers",),("Ehren Kruger",),("Sev Ohanian",),("Nicholas D. Johnson",), ("Will Merrick",),("Scott Cooper",)
           ,("Louis Bayard",),("Neil Cross",),("Joseph Barbera",),("William Hanna",),("Toom Venkat",))

movieStar_query_insert = "insert into MovieStars (Star_Name) values (%s)"

movieStars = (("Ezra Miller",),("Sasha Calle",),("Ben Affleck",),("Jeremy Irons",),("Henry Cavill",),("Amy Adams",),("Diane Lane",)
             ,("Gal Galdot",),("Jensen Ackles",),("Stana Katic",),("Matt Bomer",),("Frank Welker",),("Grey Griffin",),("Matthew Lillard",)
             ,("Mindy Cohn",),("Jake Gyllenhaal",),("Yahya Abdul-Mateen",),("Eiza Gonzalez",),("Robert De Niro",),("Ray Liotta",)
             ,("Joe Pesci",),("Sharon Stone",),("Allari Naresh",),("Mirnaa",),("Adam Devine",),("Pierce Brosnan",),("Ellen Barkin",)
             ,("Nina Dobrev",),("Darren Barnett",),("Jimmy O Yang",),("Mikaela Hoover",),("Thomas Jane",),("Dean Jaggar",)
             ,("Dominique Tipper",),("Alice Braga",),("JD Pardo",),("Jessica Rothe",),("Israel Broussard",),("Ruby Modine",),("Sarah Snook",)
             ,("Lilly LaTorre",),("Neil Melville",),("Omar Chaparro",),("Bolivar Sanchez",),("Carlos Solorzano",),("Haley Bennett",)
             ,("Austin Stowell",),("Denis O'Hare",),("Freida Pinto",),("Logan Marshall Green",),("Robert John Burke",),("Kate Siegel",)
             ,("Jason O'Mara",),("Dule Hill",),("Priyanka Chopra Jonas",),("Sam Heughan",),("Celine Dion",),("Nicola Wallace",)
             ,("Gabriel Guevara",),("Marta Hazas",),("Lili Reinhart",),("Austin Abrams",),("Sarah Jones",),("Robert Maaser",)
             ,("Jordis Triebel",),("Marie Hacke",),("Phillip Aguirre",),("Ryan Kiera Armstrong",),("Clint Howard",),("Nicholas Cage",)
             ,("Jeff Bridges",),("Matt Damon",),("Hailee Steinfield",),("Mark Hamil",),("Harrison Ford",),("Carrie Fisher",)
             ,("Shia LeBeouf",),("Megan Fox",),("Josh Duhamel",),("Tim Griffin",),("Ava Zaria Lee",),("Nia Long",),("Christian Bale",)
             ,("Harry Melling",),("Simon McBurney",),("Idris Elba",),("Cynthia Erivo",),("Andy Serkis",),("Darren Barnett",))

reviewers_query_insert = "insert into reviewers (Reviewer_Name, City) values (%s, %s)"

reviewers = (("Joe Stevens","London"),("Jo Ferry","London"),("Jane Daley","Sheffied"),("Paul Cross","Norwich"),("Simon Tate","Sheffied")
            ,("Peter Simmons","Scotland"),("Mike Smith","Scotland"),("Paul Trust", "Brighton"),("Samantha Taylor","Brighton")
            ,("Jason Reeds","London"),("Anne Tate", "Newmarket"),("Peter Hancock","Newmarket"),("Jessie Youth","Leeds")
            ,("Bob Missile","Manchester"),("Jennifer Aymes","Manchester"),("Simon Ridley","Leeds"),("Charlie Simms","Leeds")
            ,("Charlene","Ripon"),("Mike Howorth","Ripon"),("Jason Richards","Manchester"),("Jermaine Roberts","York"),("Mike Chalk","York")
            ,("Pat Colt","York"),("Nicola Holmes","Sheffield"),("Joseph Pine","London"),("Craig Peters","Barnsley")
            ,("Kelly Bowchurch","London"),("Daniel Taylor","Barnsley"),("Jess Best","London"),("Joseph Holiday","Barnsley")
            ,("Jane Doe","Oxford"))

#Below are query strings for many to many relationship inserts and the sequences that can be used by Python to insert the data
#via the executemany() method. If you examine the SQL file you notice that for the primary key it makes use of composite keys
#rather than the auto_increment feature

#We can categorize a movie with many categories ie thriller, drama, action etc. A category can categorize many movies
CategorizedMovie_query_insert = "insert into CategorizedMovie (FKMovie_ID, FKCategory_ID) values (%s, %s)"

CategorizedMovies = ((1, 1),(1, 2),(1, 6),(1, 7),(2, 1),(2, 2),(2, 7),(2, 13),(3, 1),(3, 2),(3, 7),(4, 1),(4, 2),(4, 3),(4, 7),(4, 13)
                    ,(5, 3),(5, 13),(6, 1),(6, 4),(6, 5),(6, 8),(7, 4),(7, 5),(8, 4),(8, 5),(9, 1),(9, 5),(9, 11),(10, 1),(10, 4),(10, 6)
                    ,(11, 11),(11, 6),(12, 1),(12, 8),(13, 14),(13, 1),(13, 8),(13, 10),(14, 14),(14, 6),(14, 9),(15, 14),(15, 6),(15, 9)
                    ,(16, 8),(16, 9),(17, 9),(17, 8),(17, 13),(18, 9),(18, 8),(18, 5),(19, 8),(19, 14),(19, 10),(19, 1),(19, 5),(20, 8)
                    ,(20, 10),(20, 14),(21, 5),(21, 6),(21, 11),(22, 5),(22, 11),(23, 5),(23, 11),(24, 1),(24, 5),(24, 12),(25, 1),(25, 5)
                    ,(25, 12),(26, 5),(26, 12),(27, 1),(27, 2),(27, 7),(27, 13),(28, 1),(28, 2),(28, 7),(28, 13),(29, 1),(29, 2),(29, 7)
                    ,(29, 13),(30, 1),(30, 2),(30, 13),(31, 1),(31, 2),(31, 13),(32, 5),(32, 8),(32, 14),(33, 8),(33, 14),(34, 4),(34, 5)
                    ,(34, 13))

#A movie can have many movie stars and a movie star can star in many movies
moviecast_query_insert = "insert into MovieCast (FKMovie_ID, FKStar_ID) values (%s, %s)"

moviecast = ((1, 1),(1, 2),(1, 3),(1, 4),(2, 5),(2, 6),(2, 7),(3, 1),(3, 2),(3, 3),(3, 4),(3, 5),(3, 8),(3, 6),(3, 7),(4, 9),(4, 10)
             ,(4, 11),(5, 12),(5, 13),(5, 14),(5, 15),(6, 16),(6, 17),(6, 18),(7, 19),(7, 20),(7, 21),(8, 19),(8, 22),(8, 21),(9, 23)
             ,(9, 24),(10, 25),(10, 26),(10, 27),(11, 28),(11, 29),(11, 30),(11, 31),(11, 89),(12, 32),(12, 33),(12, 34),(13, 35),(13, 36)
             ,(13, 3),(14, 37),(14, 38),(14, 39),(15, 37),(15, 38),(15, 39),(16, 40),(16, 41),(16, 42),(17, 43),(17, 44),(17, 45),(18, 46)
             ,(18, 47),(18, 48),(19, 49),(19, 50),(19, 51),(20, 52),(20, 53),(20, 54),(21, 55),(21, 56),(21, 57),(22, 58),(22, 59),(22, 60)
             ,(23, 61),(23, 62),(23, 63),(24, 64),(24, 65),(24, 66),(25, 67),(25, 68),(25, 69),(25, 70),(26, 71),(26, 72),(26, 73),(27, 74)
             ,(27, 75),(27, 76),(28, 74),(28, 75),(28, 76),(29, 74),(29, 75),(29, 76),(30, 77),(30, 78),(30, 79),(31, 77),(31, 78),(31, 79)
             ,(32, 80),(32, 81),(32, 82),(33, 83),(33, 84),(33, 85),(34, 86),(34, 87),(34, 88))

moviescript_query_insert = "insert into MovieScript (FKMovie_ID, FKWriter_ID) values (%s, %s)"

moviescripts = ((1, 1),(1, 2),(1, 3),(2, 4),(2, 5),(2, 6),(3, 7),(3, 8),(3, 9),(4, 10),(4, 11),(4, 12),(5, 13),(6, 14),(6, 15),(6, 16)
                ,(7, 17),(7, 18),(8, 17),(8, 18),(9, 19),(9, 8),(9, 63),(10, 20),(10, 21),(11, 23),(11, 22),(12, 24),(13, 25),(14, 27)
                ,(13, 26),(15, 28),(15, 27),(16, 29),(17, 30),(17, 31),(18, 32),(19, 33),(20, 34),(21, 35),(21, 36),(21, 37),(22, 38)
                ,(22, 39),(23, 40),(23, 41),(24, 42),(24, 43),(25, 44),(26, 45),(26, 46),(26, 47),(27, 48),(28, 48),(28, 49),(28, 50)
                ,(29, 48),(29, 50),(30, 51),(30, 52),(30, 53),(31, 51),(31, 52),(31, 54),(32, 55),(32, 56),(32, 57),(33, 58),(33, 59)
                ,(34, 60),(5, 61),(5, 62))

directedMovies_insert_query = "insert into DirectedMovies (FKMovie_ID, FKDirector_ID) values (%s, %s)"

directedMovies = ((1, 1),(2, 2),(3, 2),(4, 3),(5, 6),(6, 7),(7, 8),(8, 8),(9, 9),(10, 10),(11, 11),(12, 12),(13, 13),(14, 14)
                 ,(15, 14),(16, 15),(17, 16),(18, 17),(19, 18),(20, 19),(20, 20),(21, 21),(22, 22),(23, 23),(24, 24),(25, 25),(26, 26)
                 ,(26, 27),(27, 28),(28, 29),(29, 30),(30, 7),(31, 7),(32, 31),(32, 32),(33, 33),(34, 34))

ratings_insert_query = "insert into ratings (FKMovie_ID, FKReviewer_ID, Rating, Review) values (%s, %s, %s, %s)"

ratings = ((1,1,7.2,"Erza is great. Contains jaw dropping action scenes"),(1,2,5.1,"Seen too many of these movies. They are all the same")
          ,(1,3,8.0,"Funny. Pleasure to watch"),(1,4,7.3,"Great movie. Definitely recommend"),(2,5,7.2,"Great Watch")
          ,(2,6,6.8,"Prefer Christopher Reeves. Superman isn't trusted in movie"),(2,3,8.0,"Definitely recommend")
          ,(3,5,8.9,"Great Watch but too long"),(3,6,8.1,"My favourite superhero movie"),(3,7,8.2,"Definitely recommend")
          ,(3,4,8.0,"Recommend"),(4,2,5.1,"Slow and boring"),(4,4,4.1,"Don't waste your time"),(5,7,7.2,"I loved it")
          ,(5,4,8.2,"Definitely recommend"),(5,8,4.3,"No Thank you"),(5,9,3.1,"Worst Animation I have seen so far")
          ,(6,10,7.2,"Definitely recommend"),(6,8,7.3,"Must see"),(6,9,8.1,"Loved it"),(7,10,9.1, "Classic. Even for today")
          ,(7,4,9.8,"Never get bored watching this"),(8,11,7.1,"Even now it is still good"),(8,10,7.1,"Good Crime movie")
          ,(9,12,4.2,"Don't bother"),(8,13,3.1,"Didn't watch all of it because it was a drag"),(10,6,6.1,"OK"),(10,8,5.0,"Don't bother")
          ,(10,13,6.8,"Funny"),(11,14,6.4,"Worth a watch"),(11,12,6.1,"I love romantic Comedies"),(11,9,6.2,"Better than I thought")
          ,(13,15,5.1,"Even with Ben Affleck movie is dull"),(13,9,4.29,"Wierd movie"),(15,5,6.3,"Sequel even better")
          ,(15,2,6.0,"Prefer the original"),(15,3,6.6,"Could have been better"),(15,8,7.39,"Always like these kind of movies")
          ,(16,16,5.0,"Dissapointing"),(16,10,4.9,"Better horror movies out there"),(16,7,5.1,"Not scary at all")
          ,(17,17,3.31,"Absolute lame movie"),(17,18,3.3,"Cannot recommend"),(17,6,4.2,"Low budget scenes and dissapointing plot")
          ,(17,5,4.1,"Scary but boring as well"),(18,19,6.31,"Watchable"),(18,20,5.7,"Cannot recommend")
          ,(18,18,5.9,"Pyschological movie with a difference"),(18,3,4.7,"This is not my cup of tea"),(19,21,3.3,"Seen too many movies")
          ,(19,22,2.2,"One of the worst movies I have seen"),(20,22,5.0,"Movie plays with your mind"),(22,22,5.2,"It is not bad")
          ,(22,11,4.3,"Waste of time"),(23,23,6.2,"I like it"),(23,24,6.3,"I don't usually watch Romantic movies but this was OK")
          ,(25,25,6.3,"Cage is always good Actor. He stars in this exciting Western Drama"),(26,26,4.3,"I didn't like it")
          ,(26,27,3.3, "Slow and for a Western it is very badly written"),(27,3,8.8,"Best Sci-Fi Franchise")
          ,(27,2,8.7,"Never forget this. I will always be a fan"),(27,1,8.9,"Brilliant")
          ,(27,23,7.7,"This is the best movie in the whole franchise")
          ,(27,21,8.3,"Imagine they use the special effects available now then this would be even better"),(28,9,9.2,"Classic Sci-Fi")
          ,(28,11,9.0,"Great Plot and movie"),(28,12,9.2,"Old classic. I even watch even today")
          ,(28,19,8.3,"Watched when I was a kid and I am still a big fan"),(29,13,8.2,"I like it"),(29,14,8.3,"Lovely")
          ,(29,19,9.3,"Great. But the sequel franchise is not as good and the ideas were copied. They can never match Lucas")
          ,(29,12,8.43,"Star wars and may the force be with us"),(29,17,9.3,"Excellent"),(30,28,8.3,"Was never a Transformer fan until now")
          ,(30,29,7.0,"Give it a 7 because too much violence but overall good movie"),(30,8,8.0,"Amazing fight scenes and special effects")
          ,(30,9,8.2,"Must watch"),(31,10,7.8,"Best Transformers movie so far"),(31,12,8.4,"I loved it"),(31,11,8.2,"Great movie")
          ,(31,4,9.0,"Great. I am a fan of the whole franchise so far"),(31,2,8.73,"Great sequel to an excellent franchise so far")
          ,(31,5,7.9,"Excellent"),(33,30,5.8,"Watchable"),(33,29,4.9,"Started well then plot drifted"),(33,11,6.1,"Was surprised"))




