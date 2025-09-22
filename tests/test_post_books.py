"""
Test suite for all the POST operations related to the /books enpoint
"""
import pytest
import requests
import logging

@pytest.mark.regression
def test_get_all_books_schema(base_url, book_data):
    """POST a /books test - TC6 - A book is returned"""
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




