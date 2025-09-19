import pytest
import requests


def test_get_all_books_schema(base_url):
    pass

def test_get_all_books(base_url):
    """Basic GET /books test - TC2"""
    response = requests.get(f"{base_url}/books")
    # Assert status code
    assert response.status_code == 200
    # Assert json response
    assert response.headers['content-type'] == 'application/json; charset=utf-8; v=1.0'


