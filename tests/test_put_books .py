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
def test_put_a_book(base_url):
    """PUT (update) a /books test - TC11 - Book 1 info is updated"""
    book_data = load_book_data('book_data_update.json')
    response = requests.put(f"{base_url}/books/1", json=book_data)
    # Assert status code
    assert response.status_code == 200
    # Assert json response
    assert response.headers['content-type'] == 'application/json; charset=utf-8; v=1.0'
    # Assert that an array of books was returned
    book = response.json()

    # Assert all sent fields match the obtained response
    for field in ['title', 'description', 'pageCount', 'excerpt', 'publishDate']:
        assert book[field] == book_data[field], f"{field} should match"
    # Log response details
    logging.info(f"Response HTTP CODE: {response.status_code}")
    logging.info(f"Updated the book with ID: {book['id']}")

@pytest.mark.regression
def test_put_a_book_invalid_date(base_url):
    """PUT a /books test - TC12 - Using invalid date property"""
    book_data = load_book_data('book_data_invalid_date.json')
    response = requests.put(f"{base_url}/books/1", json=book_data)
    # Assert status code
    assert response.status_code == 400
    # Log response details
    logging.info(f"Response HTTP CODE: {response.status_code}")






