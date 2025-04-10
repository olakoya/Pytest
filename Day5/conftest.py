from email.policy import default

import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

hub_url = "http://192.168.1.166:4444/wd/hub"

# Importing Fixture Function

@pytest.fixture()
def setup(browser_platform): # defining parameter as browser to the fixture function (Parameter value = browser)
    browser, platform =  browser_platform
    options = {
        "chrome": webdriver.ChromeOptions(),
        "edge": webdriver.EdgeOptions(),
        "firefox": webdriver.FirefoxOptions(),
        "safari": webdriver.SafariOptions(),
    }
    platform_mapping = {"mac": "MAC", "windows": "WIN10", "linux": "LINUX"}
    platform_name = platform_mapping[platform]
    opt = options[browser]
    opt.add_experimental_option("detach", True) if browser in ['chrome','edge','firefox','safari'] else None
    opt.platform_name = platform_name
    driver = webdriver.Remote(command_executor=hub_url, options=opt)
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser', action="store", default="chrome", help="Browser to run tests")
    parser.addoption("--os", default='windows')

@pytest.fixture()
def browser_platform(request):
    return request.config.getoption("--browser"),request.config.getoption("--os")

