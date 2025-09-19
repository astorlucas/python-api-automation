import pytest
import os
import json

@pytest.fixture(scope="session")
def environment_config():
    """Load env config from env file"""
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'environment.json'), 'r') as json_env:
        return json.load(json_env)

@pytest.fixture(scope="session")
def base_url(environment_config):
    """Getting base_url"""
    return environment_config['base_url']

@pytest.fixture(autouse=True)
def test_message():
    """Message at start and end of each test"""
    print("\n---Starting test---")
    yield
    print("\n---Test complete---")