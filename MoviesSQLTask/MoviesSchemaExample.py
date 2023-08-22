from MySQLFunctions import getDBConnection, executeScript
from TaskDocumentation import *

def main():
    pass

if __name__ == '__main__':
    main()

#We can read from a SQL Script to create the tables. Note we don't use commit() even though we are making changes to
#the database or we will get an out of synch error. We will have to reconnect to the database.
executeScript(getDBConnection("localhost","chupc","PASSWORD","QABootcamp"), "SQLScripts\MoviesSchema.sql")

print("All the tables have been created successfully")