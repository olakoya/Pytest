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

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver  # Returning some value to a test method
    driver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser', action="store", default="chrome", help="Browser to run tests")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config): # For adding information hook isn't required
    config.stash[metadata_key]['Project Name'] = 'Google'
    config.stash[metadata_key]['Module Name'] = 'Title Module'
    config.stash[metadata_key]['Tester Name'] = 'Ola'

# @pytest.mark.optionalhook
# def pytest_metadata(metadata): # For modifying hook is required above
#     metadata.pop("Python", None)  # pop means remove or delete
#     metadata.pop("Plugins", None)


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Python", None)  # pop means remove or delete # Remove Python version
    metadata.pop("Plugins", None)  # Remove Plugins section
    return metadata # Ensure the updated metadata is returned
    # Your existing code


'''
Specifying some value to option (--browser chrome) in the terminal run code and this is read from the terminal by using 
==> request.config.getoption("--browser")

Output for chrome as you can see from the running/execution code

(.venv) olakoya@MacBookPro Pytest % pytest -s -v --browser chrome Day3/test_commandline4.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
metadata: {'Platform': 'macOS-10.16-x86_64-i386-64bit', 'Packages': {'pytest': '8.3.5', 'pluggy': '1.5.0'}, 'Project Name': 'Google', 'Module Name': 'Title Module', 'Tester Name': 'Ola'}
rootdir: /Users/olakoya/Desktop/Pytest
plugins: html-4.1.1, metadata-3.1.1, dependency-0.6.0, ordering-0.6, xdist-3.6.1
collected 1 item                                                                                                                                                      

Day3/test_commandline4.py::Testsample::test_sample Running tests on chrome
PASSED

========================================================================== 1 passed in 3.04s ==========================================================================



Output for edge as you can see from the running/execution code

(.venv) olakoya@MacBookPro Pytest % pytest -s -v --browser edge Day3/test_commandline4.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
metadata: {'Platform': 'macOS-10.16-x86_64-i386-64bit', 'Packages': {'pytest': '8.3.5', 'pluggy': '1.5.0'}, 'Project Name': 'Google', 'Module Name': 'Title Module', 'Tester Name': 'Ola'}
rootdir: /Users/olakoya/Desktop/Pytest
plugins: html-4.1.1, metadata-3.1.1, dependency-0.6.0, ordering-0.6, xdist-3.6.1
collected 1 item                                                                                                                                                      

Day3/test_commandline4.py::Testsample::test_sample Running tests on edge
PASSED

========================================================================= 1 passed in 19.13s ==========================================================================



Output for firefox as you can see from the running/execution code

(.venv) olakoya@MacBookPro Pytest % pytest -s -v --browser firefox Day3/test_commandline4.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
metadata: {'Platform': 'macOS-10.16-x86_64-i386-64bit', 'Packages': {'pytest': '8.3.5', 'pluggy': '1.5.0'}, 'Project Name': 'Google', 'Module Name': 'Title Module', 'Tester Name': 'Ola'}
rootdir: /Users/olakoya/Desktop/Pytest
plugins: html-4.1.1, metadata-3.1.1, dependency-0.6.0, ordering-0.6, xdist-3.6.1
collected 1 item                                                                                                                                                      

Day3/test_commandline4.py::Testsample::test_sample Running tests on firefox
PASSED

========================================================================= 1 passed in 13.50s ==========================================================================

'''

'''
Below is the code to run to have your code displayed automatically on your browser rather than doing it manually

==> pytest -s -v --browser chrome Day3/test_commandline4.py --html=report.html

Output is
(.venv) olakoya@MacBookPro Pytest % pytest -s -v --browser chrome Day3/test_commandline4.py --html=report.html
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
metadata: {'Platform': 'macOS-10.16-x86_64-i386-64bit', 'Packages': {'pytest': '8.3.5', 'pluggy': '1.5.0'}, 'Project Name': 'Google', 'Module Name': 'Title Module', 'Tester Name': 'Ola'}
rootdir: /Users/olakoya/Desktop/Pytest
plugins: html-4.1.1, metadata-3.1.1, dependency-0.6.0, ordering-0.6, xdist-3.6.1
collected 1 item                                                                                                                                                      

Day3/test_commandline4.py::Testsample::test_sample Running tests on chrome
PASSED

----------------------------------------------- Generated html report: file:///Users/olakoya/Desktop/Pytest/report.html -----------------------------------------------
========================================================================== 1 passed in 4.56s ==========================================================================
(.venv) olakoya@MacBookPro Pytest % 

'''