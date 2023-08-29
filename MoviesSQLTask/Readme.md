Project
=======
This was a portfolio task that I completed during my studies at QA Bootcamp. The relation database used is MySQL. The schema is called
QABootcamp.

1. Design a movies schema with the necessary relationships for movies, genre, directors, writers, and moviestars.
2. Develop the necessary SQL files. Solution will require relating tables. Write SQL file for inserting data.
3. Write python code to build the schema.
4. Write python to insert data. 
5. Write python code to query the tables to get common information from the tables. Some queries will require joining tables.

SQL files
=========
The SQL files are contained in the SQLScripts directory. The ERD diagram is contained in this directory called Movies-MySql-ERD.jpg.

MoviesSchema.sql: SQL instructions for building the tables and the foreign relationships between the tables.

MoviesInit.sql: SQL statements for inserting data into the tables.

MovieComplexQueries.sql: SQL join queries

DropAllTables.sql: When testing the MoviesSchema.sql you can run this file to drop all tables.

Running the Python code
=======================
You will neesd to install the MySQL Connector. Examples assume that database is at localhost. User with rights is called chupc and passwod is PASSWORD.
You may need to change this to your credentials.

python -m pip install mysql-connector-python 

You don't have to but it is recommended to use virtual environments

> cd MoviesSQLTask
> py -3 -m venv .venv
> .venv\Scripts\activate

Building the schema. QABootcamp schema needs to be empty or you will get errors. MoviesSchemaExample.py reads the SQL file MoviesSchema.sql to build 
the schema.

> cd MoviesSQLTask
> python MoviesSchemaExample.py

To insert sample data in the tables using Python

> cd MoviesSQLTask
> python MovieInsertExample.py

To perform common queries using Python

> cd MoviesSQLTask
> python MovieQueryExamples.py