from selenium import webdriver
import pytest
from utilities.read_json import get_config

# Initializes, maximizes, and navigates the Chrome WebDriver before each test, then closes it after the test finishes
@pytest.fixture(scope="function")
def driver(test_data):
    driver = webdriver.Chrome()
    driver.explicit_wait = test_data["explicit_wait"]
    driver.maximize_window()
    driver.get(test_data["base_url"])
    yield driver
    driver.quit()

# Loads the global configuration details from the JSON file once per test execution session
@pytest.fixture(scope="session")
def test_data():
    return get_config()