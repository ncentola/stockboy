import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = "postgres://{}:{}@db:5432/{}".format(
        os.environ['POSTGRES_USER'],
        os.environ['POSTGRES_PASSWORD'],
        os.environ['POSTGRES_DB']
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
