"""
This module is a basic demo that demostrates how to query a movies database that has many
to many relationships.

It was an optional task during my study at QA Bootcamp Python Development Level 3
"""

from MySQLFunctions import selectQuery, printRecords, getDBConnection
from TaskDocumentation import *

def main():
    pass

if __name__ == '__main__':
    main()

def underline(string):
    """
    A basic function that underlines the a string

    Parameter
    =========
    string: A string argument. Should not be None.

    Return
    ======
    Returns a underline that underline the string parameter as if it is a header.
    The underline matches the length of the string and it does this by using
    simple concatenation.
    """
    length = len(string)

    line = ""

    for x in range(length):
        line += "="

    return line

def printQuery(sqlqueries, cursor):

    """
    A function that executes a SQL statement specified as a tuple in the
    in the sqlqueries parameter.

    Format of output
    ----------------

    header (explaination of query
    =============================
    Query results with a row on a single line.

    Note: Function will simply print the tuple contents as a string.

    Parameter
    =========
    sqlqueries: sqlqueries is a sequence with each item with two elements.

    (element1, element2)

    element1 is a string that explains the purpose of the
    sql query in the demo. This is underlined.

    element2 is a string that contains SQL select statement.
    The select statement can be join queries that query multiple
    tables.

    cursor: A cursor object of the mysql.connector class. You can call
    the cursor() method of the mysql.connector class to obtain an instance
    of the required cursor.

    Return
    ======
    No explicit return specified so None is returned by default.



    """

    for heading, query in sqlqueries:
        print("\n" + heading)
        print(underline(heading), "\n")
        rows = selectQuery(cursor, query)
        printRecords(rows)

#You should put your db connection within a context manager so the db will automatically be closed
db = getDBConnection("localhost","chupc","PASSWORD","QABootcamp")

queries = (("Movies","Select * from movies"), ("Genre","Select * from Genre"), ("Directors", "Select * from directors")
           , ("Writers","Select * from writers"), ("Movie Stars", "Select * from moviestars")
           , ("Reviewers", "Select * from reviewers"))

with db.cursor() as cursor:
    print("First of all printing all records for the main tables\n")

    printQuery(queries, cursor)

    print("Below are query examples that involve joins\n")

    from ComplexJoinQueries import joinQueries

    printQuery(joinQueries, cursor)


db.close()

print("End of demo")