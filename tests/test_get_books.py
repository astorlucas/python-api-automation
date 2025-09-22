"""
Test suite for all the GET operations related to the /books enpoint
"""

import pytest
import requests
import logging

# Books schema, needed to validate schema
BOOK_SCHEMA = {
    "id": int,
    "title":str,
    "description":str,
    "pageCount":int,
    "excerpt":str,
    "publishDate":str
}

@pytest.mark.regression
def test_get_all_books_schema(base_url):
    """GET /books test - TC1 - Validating schema"""
    response = requests.get(f"{base_url}/books")
    # Assert status code
    assert response.status_code == 200
    # Assert json response
    assert response.headers['content-type'] == 'application/json; charset=utf-8; v=1.0'
    books = response.json()
    for i, book in enumerate(books):
        for key, expected_type in BOOK_SCHEMA.items():
            assert key in book, f"[{i}] Missing key: {key}"
            assert isinstance(book[key], expected_type), f"[{i}] {key} wrong type"
    # Log response details
    logging.info(f"Response HTTP CODE: {response.status_code}")
    logging.info(f"Response Body Preview: {response.text[:200]}...")
    

@pytest.mark.regression
def test_get_all_books(base_url):
    """GET /books test - TC2"""
    response = requests.get(f"{base_url}/books")
    # Assert status code
    assert response.status_code == 200
    # Assert json response
    assert response.headers['content-type'] == 'application/json; charset=utf-8; v=1.0'

    # Assert that an array of books was returned
    books = response.json()
    assert isinstance(books, list), "Response should be a list/array"
    assert len(books) > 0, "Response should contain at least one book"

    # Log response details
    logging.info(f"Response HTTP CODE: {response.status_code}")
    logging.info(f"Response Body Preview: {response.text[:200]}...")

@pytest.mark.regression
def test_unsupported_method_books(base_url):
    """GET /books test - TC2"""
    response = requests.options(f"{base_url}/books")
    # Assert status code
    assert response.status_code == 405
    # Log response details
    logging.info(f"Response HTTP CODE: {response.status_code}")


@pytest.mark.regression
def test_get_a_book(base_url):
    """GET specific /books test - TC4"""
    response = requests.get(f"{base_url}/books/1")
    # Assert status code
    assert response.status_code == 200
    # Assert json response
    assert response.headers['content-type'] == 'application/json; charset=utf-8; v=1.0'
    # Response to Assert 
    book = response.json()
    # Assert that the book obtained is the correct one 
    # Assert will also fail if not a single object is returned by the API
    assert book['id'] == 1, "Book ID should be 1"
    # Log response details
    logging.info(f"Response HTTP CODE: {response.status_code}")
    logging.info(f"Response Body Preview: {response.text[:200]}...")

@pytest.mark.regression
def test_get_a_non_existing_book(base_url):
    """GET specific non-existing /books test - TC5"""
    response = requests.get(f"{base_url}/books/-1")
    # Assert status code
    assert response.status_code == 404
    # Log response details
    logging.info(f"Response HTTP CODE: {response.status_code}")



