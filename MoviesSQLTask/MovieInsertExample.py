"""
MySQL demo as part a task during my study at QA Bootcamp. We will need to design a Movies Schema using SQL.
We would then need to connect to a MySQL database and using Python insert some movies records.

We should then be able to connect to the MySQL database and perform various SQL queries.

You will need to install a Python Connector for Python to be able to connect to the database. You can either
download the Python connector from Oracle or you can use Pip to install the Python Connector.

pip install mysql-connector-python

For this demo you will need a empty schema called QABootcamp. For demonstrations purposes just delete all tables
in the schema making sure the schema is completely empty. The demo will build and insert data into all the required
tables.
"""


from MySQLParameters import genre_insert_query, genres, movies, movies_insert_query
from MySQLParameters import directors_insert_query, directors, writers_insert_query, writers
from MySQLParameters import movieStar_query_insert, movieStars, reviewers_query_insert, reviewers
from MySQLParameters import CategorizedMovie_query_insert, CategorizedMovies
from MySQLParameters import moviecast_query_insert, moviecast, moviescript_query_insert
from MySQLParameters import moviescripts, directedMovies_insert_query, directedMovies
from MySQLParameters import ratings_insert_query, ratings
from MySQLFunctions import executeSQLStmt, insertMany, getDBConnection
from TaskDocumentation import *

def main():
    pass

if __name__ == '__main__':
    main()



#You should put your db connection within a context manager so the db will automatically be closed
db = getDBConnection("localhost","chupc","PASSWORD","QABootcamp")

with db.cursor() as cursor:
    #You can use execute method alone to insert into the database but this is only good if you have a few inserts.
    #We should be using executeMany. We are going to use executeMany from now on. These two inserts are only included
    #for completeness.
    executeSQLStmt(db, cursor, 'insert into Genre (Category_Name) values ("Action")', True)
    executeSQLStmt(db, cursor, 'insert into Genre (Category_Name) values ("Adventure")', True)

    sqlParameters = (("Inserting records in the Genre table using executemany()"
                     , genre_insert_query, genres)
                     ,("Now inserting records in the movies table using executemany()"
                     , movies_insert_query, movies)
                     ,("Now inserting records in the directors table"
                     , directors_insert_query, directors)
                     ,("Now inserting records in the writers table"
                     , writers_insert_query, writers)
                     ,("Now inserting records in the movies stars table"
                     , movieStar_query_insert, movieStars)
                     ,("Now inserting records in the reviewers table"
                     , reviewers_query_insert, reviewers)
                     , ("Finally come to the junction table inserts starting with the categorized movies"
                     , CategorizedMovie_query_insert, CategorizedMovies)
                     , ("Next junction table is the MovieCast table"
                     , moviecast_query_insert, moviecast)
                     , ("Now inserting records for the MovieScript table"
                     , moviescript_query_insert, moviescripts)
                     , ("Inserting records for the DirectedMovies table"
                     , directedMovies_insert_query, directedMovies)
                     , ("Finally inserting records in the ratings table"
                     , ratings_insert_query, ratings))

    for myIntent, sql, records in sqlParameters:
        print(myIntent)
        insertMany(db, cursor, sql, records)

print("All records have successfully been inserted in the table")

print("Next run MovieQueryExamples.py for MySQL query examples")

db.close()









