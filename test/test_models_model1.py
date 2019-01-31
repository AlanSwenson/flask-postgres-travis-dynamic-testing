import pytest

from test.support.configure_test import app
from project import db

import project.models.model1 as model1
from project.config import TestingConfig


def test_db_create(app):
    app = app(TestingConfig)

    test_model_to_insert = model1.Model1(
        cool_field="test name", cooler_field="Cooler String"
    )
    test_model_to_insert.save()
    db.session.commit()

    assert db.session.query(model1.Model1).one()
