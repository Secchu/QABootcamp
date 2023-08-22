"""
SQLALCHEMY_DATABASE_URI: The database URI specifies the database you want to establish a connection with using SQLAlchemy. In this case, you
either get it from a DATABASE_URI environment variable or you set a default value. The default URI value here follows the format
sqlite:///path/to/app.db. You use the os.path.join() function to join the base directory you constructed and stored in the basedir variable
and the app.db file name. With this, creating a Flask application without setting a DATABASE_URI environment variable will connect to an
app.db database file in your flask_app directory by default. The file will be created when you create your database tables. If you’d like to
set a database URI for a different SQL engine.

SECRET_KEY: A long random string used by Flask as a secret key, or a key used to secure the sessions that remember information from one
request to another. The user can access the information stored in the session but cannot modify it unless they have the secret key, so you
must never allow anyone to access your secret key. you should set the secret key with an environment variable called SECRET_KEY. To get its
value in this config.py file and save it in a class variable called SECRET_KEY, you access the environment variable’s value via the
os.environ object using its get() method. Though you do not need to set the secret key in development but will certainly be something you
do in production.

SQLALCHEMY_TRACK_MODIFICATIONS: A configuration to enable or disable tracking modifications of objects. You set it to False to disable
tracking and use less memory.

Linux Examples
--------------
export SECRET_KEY="your secret key"

export DATABASE_URI="postgresql://username:password@host:port/database_name"

Windows Examples
================
set SECRET_KEY="your secret key"

set DATABASE_URI="postgresql://username:password@host:port/database_name"
"""

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False