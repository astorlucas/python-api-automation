"""
Test suite for all the POST operations related to the /books enpoint
"""
import pytest
import requests
import logging

@pytest.mark.regression
def test_delete_a_book(base_url):
    """DELETE a /books test - TC13 - Book 1 is deleted"""
    response = requests.delete(f"{base_url}/books/1")
    # Assert status code
    assert response.status_code == 200
    # Log response details
    logging.info(f"Response HTTP CODE: {response.status_code}")

@pytest.mark.regression
def test_delete_an_invalid_book(base_url):
    """DELETE a /books test - TC14 - 400 when deleting an invalid id"""
    response = requests.delete(f"{base_url}/books/-1")
    # Assert status code
    assert response.status_code == 400, f"Expected 400 for an invalid id but got {response.status_code}"
    # Log response details
    logging.info(f"Response HTTP CODE: {response.status_code}")

@pytest.mark.regression
def test_delete_a_long_id_book(base_url):
    """DELETE a /books test - TC15 - 400 when deleting a >10 digits id"""
    response = requests.delete(f"{base_url}/books/99999999999")
    # Assert status code
    assert response.status_code == 400, f"Expected 400 for a long id but got {response.status_code}"
    # Log response details
    logging.info(f"Response HTTP CODE: {response.status_code}")






