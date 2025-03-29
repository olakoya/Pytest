import pytest
from selenium import webdriver

from Day3.conftest import browser


@pytest.fixture()
def setup():

    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opt)

    yield driver # Returning some value to a test method
    driver.quit() # Ensuring browser is closed after test execution
