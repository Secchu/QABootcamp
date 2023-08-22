Running the app
===============

> cd app
			   
> py -3 -m venv .venv

> .venv\scripts\activate

> pip install Flask flask_sqlalchemy

The following command is required for POST requests and if you haven't set the SECRET_KEY

WINDOWS
======
> SET SECRET_KEY=dev

LINUX
=====
> EXPORT SECRET_KEY=dev

STARTING THE DEVELOPMENT SERVER
-------------------------------

WINDOWS OR LINUX
================
> flask run --debug

On a browser browse to localhost:5000

Testing the database
====================
In the backup folder rename any of the sqlite database files to Movies.db and copy it in the instance folder overwriting any existing 
database in the instance folder. empty-movies.db is empty movies database while movies-samples.db contains sample movie records for
testing.

You can also build the Sqlite database using the SQL files in the instance folder. Use the read command contained in the Sqlite command line tools
i.e.

> sqlite3 movies.db

> .read MovieSchema.sql

> .read movie-inserts.sql

ERD Diagram
===========
ERD Diagram is contained in the instance\ERD folder
