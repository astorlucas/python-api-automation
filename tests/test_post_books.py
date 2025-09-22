"""
Test suite for all the POST operations related to the /books enpoint
"""
import pytest
import requests
import logging
import os
import json

def load_book_data(filename):
    """Load book data from specified file"""
    # I moved it from conftest.py for simplicity and ease of use
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', filename)
    with open(data_path, 'r') as f:
        return json.load(f)

@pytest.mark.regression
def test_post_a_book(base_url):
    """POST a /books test - TC6 - A book is returned"""
    book_data = load_book_data('book_data.json')
    response = requests.post(f"{base_url}/books", json=book_data)
    # Assert status code
    assert response.status_code == 200 # It should be 201, but for the service uses 200 for creation
    # Assert json response
    assert response.headers['content-type'] == 'application/json; charset=utf-8; v=1.0'
    # Assert that an array of books was returned
    book = response.json()

    # Assert all sent fields match the obtained response
    for field in ['title', 'description', 'pageCount', 'excerpt', 'publishDate']:
        assert book[field] == book_data[field], f"{field} should match"
    # Log response details
    logging.info(f"Response HTTP CODE: {response.status_code}")
    logging.info(f"Created book with ID: {book['id']}")

@pytest.mark.regression
def test_post_a_book_no_nullable(base_url):
    """POST a /books test - TC7 - No nullable fields"""
    book_data = load_book_data('book_data_nullable.json')
    response = requests.post(f"{base_url}/books", json=book_data)
    # Assert status code
    assert response.status_code == 200 # It should be 201, but for the service uses 200 for creation
    # Assert json response
    assert response.headers['content-type'] == 'application/json; charset=utf-8; v=1.0'
    # Log response details
    logging.info(f"Response HTTP CODE: {response.status_code}")

@pytest.mark.regression
def test_post_a_book_no_body(base_url):
    """POST a /books test - TC8 - No request body"""
    response = requests.post(f"{base_url}/books", json=[])
    # Assert status code
    assert response.status_code == 400
    # Log response details
    logging.info(f"Response HTTP CODE: {response.status_code}")

@pytest.mark.regression
def test_post_a_book_invalid_date(base_url):
    """POST a /books test - TC9 - Invalid date format"""
    book_data = load_book_data('book_data_invalid_date.json')
    response = requests.post(f"{base_url}/books", json=book_data)
    # Assert status code
    assert response.status_code == 400
    # Assert json response
    logging.info(f"Response HTTP CODE: {response.status_code}")

@pytest.mark.regression
def test_post_a_book_extra_property(base_url):
    """POST a /books test - TC10 - Extra property included"""
    book_data = load_book_data('book_data_extra_property.json')
    response = requests.post(f"{base_url}/books", json=book_data)
    # Assert status code
    assert response.status_code == 400, f"Expected 400 for an extra property but got {response.status_code}"
    # Assert json response
    logging.info(f"Response HTTP CODE: {response.status_code}")







