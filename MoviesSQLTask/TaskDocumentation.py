"""
This module is for documentation purposes only. It contains information
about the purpose of the code as well as general information about the
Author.
"""

__author__ = "Sec Chu"

__author_email__ = "duongchu@hotmail.com"

__comments__ = "Developed during my study at QA Bootcamp as part of my portfolio"

__database__ = """The code uses MySQL database and a schema called QABootcamp. The schema represents a
movie database with many to many relationships."""

__RequiredModules__ = """The code uses mysql.connector to connect to the MySQL database and this needs to be
installed using pip"""

__basicTask__ = "Design a Movies relational database and insert the records using Python."

__additionalTaskNotes__ = "Has many to many relationships and uses tables"

__Files__ = """Refer to MoviesSchemaExample.py for schema creation using Python.
Refers to MovieInsertExample.py for SQL insert examples. Refer to MovieQueryExamples.py for SQL
query examples. You can run each file separately in no particular order though the recommended order
is MovieSchemaExample.py, MovieInsertExample.py and MovieQueryExamples.py but this is not necessary.
There are requirements running the code. Please refer to __requirements__
"""

__requirements__ = """To run MoviesSchemaExample.py you need a schema called QABootcamp. It is recommended that this
schema is empty but this is only for simplicity. What is necessary is that the tables do not exist in the schema or
you will run into errors. The tables are created in the QABootcamp schema.

Also because most of the tables use auto increment as primary keys and in turn the junction table use two primary keys
from different tables as a composite key you must run MovieInsertExample.py when the tables are empty and all of them
exist in the schema. Otherwise you will run into errors especially when inserting records in a junction table that link
two tables together with foreign keys. The linked tables will be incorrect.

As well as the tables being empty it is very important that there are no records inserted in any of the tabkes with auto
increment because when records are inserted into tables that link records from separate tables with foreign keys that will
be incorrect and the side effect is the incorrect records from different tables are linked together with the incorrect
foreign key. The concept is very simple but because I was new to the concept I had to learn the difficult way spending
hours debugging a problem that was very straight forward. If you need more control over the foreign keys
then you will need to modify the code to use manual primary keys with no auto increment.
"""

__SQLFiles__ = """
MoviesSchema.sql: This file contain SQL statements to create the tables in the QABootcamp schema. This file is used by
MoviesSchemaExample.py to create the tables. This file is also useful for for running MovieInsertExample.py in which
you will need newly created tables to run the Python code.

MoviesInit.sql: This file contains SQL statements to insert records in each table in the QABootcamp schema. It can be run
separately. It is not related to any of the Python modules.

DropAllTables.sql: This SQL file drops all tables in the QABootcamp schema. Be warned once the table is dropped it cannot
be retrieved. This file is useful for running MovieInsertExample.py that requires an empty schema to run correctly.

MoviesComplexQueries.sql: The MovieQueryExamples.py file uses the same join queries contained in MovieComplexQueries.sql
file of the SQLScripts folder. You can use MySQL Workbench or MySQL shell to test the queries manually before running the
code contained in MovieQueryExamples.py. Since it uses the same SQL join queries you will get the same column results whether
your using the Python code to query the database or the SQL file.
"""

__license__ = "No Licensing restrictions in place. Feel free to use code as you wish"


