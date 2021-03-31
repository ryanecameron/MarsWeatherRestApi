import pytest
import get_mars_data
import rest_api


def test_get_mars_data():
    result = get_mars_data.get_data()

    assert result == 201
    assert result != 404
