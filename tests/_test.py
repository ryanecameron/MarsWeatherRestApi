import json


def test_rout(app, client):
    res = client.get("/mars_weather_data/832")
    assert res.status_code == 200