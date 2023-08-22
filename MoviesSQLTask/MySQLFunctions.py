"""
This module contains basic utility functions for querying, inserting records in a MySQL database. These untility functions
are used by

It makes use of the mysql.connector package
"""

import mysql.connector

def getDBConnection(host, user, password, database):

    """
    This function uses the mysql connector to connect to a MySQL database. Please note you should not
    hardcode your credentials in code. It is recommended to get the credentials from a secure store such
    as Secrets Manager in the AWS Cloud. This is just a demo only and even though it is obvious you should
    be aware of this security vulnerability. For our purposes this is just a demo and our main focus won't
    be on security.

    Parameters
    ==========
    host: The host of the database as a string ie 'localhost'

    user: The username that has the necessary privileges to perform the necessary actions
    on the database specified in the database parameter. The expected type is string ie
    'admin'

    password: The password of the username specified in the user parameter. The expected type
    is string.

    database: The name of the database or the schema. The expected type is string.

    Return
    ======
    The function returns a mysql.connector object representing the MySQL connection if the connection was
    successful. Otherwise an error will be raised.
    """

    db = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database= database)

    return db

def executeSQLStmt(db, cursor, sql, commit=True):

    """
    This function executes a single sql statement specified as a string.

    Parameters
    ==========

    db: This is the mysql connector object representing the MySQL connection. This object
    should be connected to the database. You can use the is_connected() method to check if
    the object is connected to the MySQL database.

    Either call mysql.connector.connect method to obtain a mysql connection object or
    alternatively you can use the getDBConnection() function contained in this module.

    cursor: The existing cursor object of the mysql.connector class. You can either call
    cursor() method on the mysql.connector object to obtain a new cursor object or you
    can simply pass the cursor object to the cursor argument if you need to preserve the
    current state of the position of the cursor.

    sql: The sql statement in SQL as a string. ie 'Select * from movies'

    commit: This is a boolean variable that specifies whether a commit needs to be
    applied on the database object for changes to take effect. If there are NO changes
    to the database schema then this variable should be set to False. For example,
    SQL select statement only query the database table and do not make any changes or
    modifications to the table so this variable needs to be set to False. However, for
    statements such as Insert or Alter then there will be changes to the database therefore
    you should commit pending changes for it to take effect. In this case the variable should
    be set to True. Note that the variable has a default value of True so if omitted changes
    will be committed to the database.

    Return
    ======
    No value is explicitly returned. However as we all know all functions return a value
    in Python. If no return value is explicitly returned then the function returns None
    by default.

    """

    cursor.execute(sql)

    #Commit only required if changes are made to the db. If no changes are made ie select
    #then we don't commit
    if commit:
        db.commit()

def selectQuery(cursor, sqlSelect, fetchall=True):

    cursor.execute(sqlSelect)

    if fetchall:
        return cursor.fetchall()
    else:
        return cursor.fetchone()

def printRecords(rows):

    print("THE FUNCTION RETURNED {} rows\n\n".format(len(rows)))

    for row in rows:
        print(row)



def executeScript(db, path):

    """
    This function reads SQL statements from a SQL Script and executes the statements. Note that
    with very short and simple SQL scripts you should call commit() after executing the SQL
    statements in the script.

    However in our case because we are creating several tables and some with foreign key constraints
    we run into an error 'Database not sync error'. In this case we should not call commit() as when
    the error is raised changes won't take effect. You should overcome this problem by simply closing
    the cursor object. It does mean that you need to reconnect to the database if you need to perform
    additional operations. Believe me it took me hours to debug this kind of problem.

    Parameters
    ==========

    db: This is the mysql connector object representing the MySQL connection. This object
    should be connected to the database. You can use the is_connected() method to check if
    the object is connected to the MySQL database.

    path: This is a string that contains the relative or absolute path to the SQL file.

    Return
    ======
    No value is explicitly returned. However as we all know all functions return a value
    in Python. If no return value is explicitly returned then the function returns None
    by default.

    """

    cursor = db.cursor()
    with open(path, 'r') as f:
        cursor.execute(f.read(), multi=True)

    cursor.close()

def insertMany(db, cursor, sql, records):

    """
    This function is used to insert many records in a MySQL database that in turn calls executemany() of
    the mysql.connector class. The executemany() function is optimized to perform many insert operations
    as a batch. Behind the scenes it optimizes batch inserts by using prepared statements.

    Parameters
    ==========

    db: This is the mysql connector object representing the MySQL connection. This object
    should be connected to the database. You can use the is_connected() method to check if
    the object is connected to the MySQL database.

    cursor: The existing cursor object of the mysql.connector class. You can either call
    cursor() method on the mysql.connector object to obtain a new cursor object or you
    can simply pass the cursor object to the cursor argument if you need to preserve the
    current state of the position of the cursor.

    sql: The SQL insertion statement that contains the place holder variables and SQL the insert
    statement as a string.
    i.e

    'insert into Movies (Movie_Title, Duration) values (%s, %s)'

    With the SQL statement above it contains the SQL insert statement for the movies database
    and the two place holder values for Movie_Title and Duration signified the %s notation.
    The syntax is similar to SQL prepared statements.

    records: A sequence of values for the place holders contained in the SQL insert statement
    specified by the argument sql. Note that the number of elements within a sequence item should
    match the number of values for the place holders in the sql insert statement or an error will
    be raised.

    Return
    ======
    No value is explicitly returned. However as we all know all functions return a value
    in Python. If no return value is explicitly returned then the function returns None
    by default.
    """

    cursor.executemany(sql, records)
    db.commit()

