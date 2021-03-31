import pytest
from get_mars_data import get_data
import rest_api

def connect_to_server():
    rest_api.main()

def test_get_mars_data():
    result = get_data()

    assert result == 201
    assert result != 404
