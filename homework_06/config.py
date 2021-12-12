import os

SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI",
    'postgresql://user:password@localhost/otus',
)

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "-XNe9mz'v$\$FGnSw4z.bbuP",
)


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    ENV = "development"
    SECRET_KEY = SECRET_KEY


class ProductionConfig(Config):
    DEBUG = False
    ENV = "production"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
