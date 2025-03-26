import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key



# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("Python", None) # pop means remove or delete
#     metadata.pop("Plugins", None)

# Importing Fixture Function
@pytest.fixture()
def setup(browser): # defining parameter as browser to the fixture function (Parameter value = browser)
    if browser == 'chrome':
        opt = webdriver.ChromeOptions() # Passing argument in the Chromebrowser
        opt.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opt)
    elif browser == 'edge': # below is using multiple conditional statement
        opt = webdriver.EdgeOptions()  # Passing argument in the Chromebrowser
        opt.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=opt)
    elif browser == 'firefox': # below is using multiple conditional statement
        opt = webdriver.FirefoxOptions()  # Passing argument in the Chromebrowser
        driver = webdriver.Firefox(options=opt)

    yield driver  # Returning some value to a test method
    driver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser')
    # parser.addoption('--os')

def browser(request):
    # browser = request.config.getoption("--browser")
    # os = request.config.getoption("--os")
    return request.config.getoption("--browser")

def pytest_configuration(config): # For adding information hook isn't required
    config.stash[metadata_key]['Project Name'] = 'Parameterization'
    config.stash[metadata_key]['Module Name'] = 'test_Parameterization'
    config.stash[metadata_key]['Tester Name'] = 'Ola'
@pytest.mark.optionalhook
def pytest_metadata(metadata): # For modifying hook is required above
    metadata.pop("Python", None)  # pop means remove or delete
    metadata.pop("Plugins", None)

'''
Specifying some value to option (--browser chrome) in the terminal run code and is read from the terminal by using 
==> request.config.getoption("--browser")

'''