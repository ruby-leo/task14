from selenium import webdriver
import pytest
from utilities.read_json import get_config


@pytest.fixture
def driver(test_data):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(test_data["base_url"])
    yield driver
    driver.quit()


@pytest.fixture
def test_data():
    return get_config()