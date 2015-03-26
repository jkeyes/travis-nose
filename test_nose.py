
def test_add():
    pass


import httpretty
import requests


@httpretty.activate
def test_get():
    httpretty.register_uri(
        httpretty.GET, 'http://example.com', body=None, status=200)
    response = requests.get('http://example.com')
    assert response.status_code == 200
