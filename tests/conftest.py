import pytest
import os
import json
from datetime import datetime

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

def pytest_configure(config):
    # Date for test file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    config.option.htmlpath = f"reports/report-{timestamp}.html"