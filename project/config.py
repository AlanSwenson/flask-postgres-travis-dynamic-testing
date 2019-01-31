import os


def get_env_variable(name):
    try:
        return os.environ.get(name)
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


def create_db_url(user, pw, url, db):
    return f"postgresql://{user}:{pw}@{url}/{db}"


# import .env variables for DB connection
# TODO: Unify these ENV variables by pulling from different dot files
def get_env_db_url(env_setting):
    if env_setting == "development":
        POSTGRES_USER = get_env_variable("DEV_POSTGRES_USER")
        POSTGRES_PW = get_env_variable("DEV_POSTGRES_PW")
        POSTGRES_URL = get_env_variable("DEV_POSTGRES_URL")
        POSTGRES_DB = get_env_variable("DEV_POSTGRES_DB")
    elif env_setting == "testing":
        POSTGRES_USER = get_env_variable("TESTING_POSTGRES_USER")
        POSTGRES_PW = get_env_variable("TESTING_POSTGRES_PW")
        POSTGRES_URL = get_env_variable("TESTING_POSTGRES_URL")
        POSTGRES_DB = get_env_variable("TESTING_POSTGRES_DB")
    elif env_setting == "production":
        POSTGRES_USER = get_env_variable("PROD_POSTGRES_USER")
        POSTGRES_PW = get_env_variable("PROD_POSTGRES_PW")
        POSTGRES_URL = get_env_variable("PROD_POSTGRES_URL")
        POSTGRES_DB = get_env_variable("PROD_POSTGRES_DB")

    return create_db_url(POSTGRES_USER, POSTGRES_PW, POSTGRES_URL, POSTGRES_DB)


# DB URLS for each Environment
DEV_DB_URL = get_env_db_url("development")
TESTING_DB_URL = get_env_db_url("testing")
PROD_DB_URL = get_env_db_url("production")


class Config(object):
    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = DEV_DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Settings
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = TESTING_DB_URL
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = PROD_DB_URL
    DEBUG = False
    TESTING = False
