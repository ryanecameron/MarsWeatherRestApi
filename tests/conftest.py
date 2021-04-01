import pytest
from get_mars_data import get_data
from rest_api import app as flask_app


@pytest.fixture()
def app():
    yield flask_app

@pytest.fixture()
def client(app):
    return app.test_client()