import os

# folder where script runs
basedir = os.path.abspath(os.path.dirname(__file__))
FLASK_DEBUG = True
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/fyyur"
