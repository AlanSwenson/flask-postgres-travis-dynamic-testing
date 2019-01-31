import pytest
import os

from test.support.configure_test import app
from project.config import (
    get_env_db_url,
    TestingConfig,
    DevelopmentConfig,
    ProductionConfig,
)


@pytest.mark.skipif(
    "TRAVIS" in os.environ and os.environ["TRAVIS"] == "True",
    reason="Skipping this test on Travis CI.",
)
def test_development_config(app):
    app = app(DevelopmentConfig)
    DB_URL = get_env_db_url("development")
    assert app.config["DEBUG"]
    assert not app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == DB_URL


def test_testing_config(app):
    app = app(TestingConfig)
    DB_URL = get_env_db_url("testing")
    assert app.config["DEBUG"]
    assert app.config["TESTING"]
    assert not app.config["PRESERVE_CONTEXT_ON_EXCEPTION"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == DB_URL


def test_production_config(app):
    app = app(ProductionConfig)
    DB_URL = get_env_db_url("production")
    assert not app.config["DEBUG"]
    assert not app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == DB_URL
