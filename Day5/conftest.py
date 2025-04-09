import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

# Importing Fixture Function

@pytest.fixture()
def setup(browser_platform): # defining parameter as browser to the fixture function (Parameter value = browser)
    browser, platform =  browser_platform
    options = {
        "chrome": webdriver.ChromeOptions,
        "edge": webdriver.EdgeOptions,
        "firefox": webdriver.FirefoxOptions,
        "safari": webdriver.SafariOptions,
    }
    platform_mapping = {"mac": "MAC", "windows": "WIN10", "linux": "LINUX"}

def pytest_addoption(parser):
    parser.addoption('--browser', action="store", default="chrome", help="Browser to run tests")
    parser.addoption("--os")

@pytest.fixture()
def browser_platform(request):
    return request.config.getoption("--browser"),request.config.getoption("--os")

