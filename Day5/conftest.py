from email.policy import default

import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

hub_url = "http://192.168.1.166:4444/wd/hub"

# Importing Fixture Function (Correction: Second Attempt from ChatGPT)

# Command-line arguments
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests with")
    parser.addoption("--os", action="store", default="mac", help="Operating system for test run")

# Fixture that provides the browser and OS
@pytest.fixture()
def browser_platform(request):
    return request.config.getoption("--browser"), request.config.getoption("--os")

# Selenium driver setup fixture
@pytest.fixture(scope="function")
def setup(request):
    browser = request.config.getoption("--browser")
    os_name = request.config.getoption("--os")

    # Map browser to its respective options
    browser_options = {
        "chrome": webdriver.ChromeOptions(),
        "firefox": webdriver.FirefoxOptions(),
        "edge": webdriver.EdgeOptions(),
        "safari": webdriver.SafariOptions()
    }

    if browser not in browser_options:
        raise ValueError(f"Unsupported browser: {browser}")

    option = browser_options[browser]
    option.set_capability("platformName", os_name)

    # Connect to Selenium Grid
    driver = webdriver.Remote(command_executor=hub_url, options=option)
    driver.get("https://www.google.com")  # Optional: Initial page load

    # option = options[browser]
    # option.set_capability("platformName", os_name)
    # driver = webdriver.Remote(command_executor=hub_url, options=option)
    # driver.get("https://www.google.com")

    yield driver

    driver.quit()

@pytest.fixture()
def browser_platform(request):
    return request.config.getoption("--browser"), request.config.getoption("--os")

'''
Output is
2nd Execution

(.venv) olakoya@MacBookPro Pytest % pytest -s -v -n=3 --os=mac --browser=chrome Day5/test_Parallel.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.9.6', 'Platform': 'macOS-10.16-x86_64-i386-64bit', 'Packages': {'pytest': '8.3.5', 'pluggy': '1.5.0'}, 'Plugins': {'html': '4.1.1', 'metadata': '3.1.1', 'dependency': '0.6.0', 'ordering': '0.6', 'xdist': '3.6.1'}}
rootdir: /Users/olakoya/Desktop/Pytest
plugins: html-4.1.1, metadata-3.1.1, dependency-0.6.0, ordering-0.6, xdist-3.6.1
3 workers [4 items]     
scheduling tests via LoadScheduling

Day5/test_Parallel.py::TestTitle::test_title_chrome 
Day5/test_Parallel.py::TestTitle::test_title_edge 
Day5/test_Parallel.py::TestTitle::test_title_firefox 
[gw1] PASSED Day5/test_Parallel.py::TestTitle::test_title_firefox 
[gw0] PASSED Day5/test_Parallel.py::TestTitle::test_title_chrome 
[gw2] PASSED Day5/test_Parallel.py::TestTitle::test_title_edge 
Day5/test_Parallel.py::TestTitle::test_title_safari 
[gw0] PASSED Day5/test_Parallel.py::TestTitle::test_title_safari 

========================================================================= 4 passed in 14.56s ==========================================================================
(.venv) olakoya@MacBookPro Pytest % pytest -s -v -n=3 --os=mac --browser=chrome Day5/test_Parallel.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.9.6', 'Platform': 'macOS-10.16-x86_64-i386-64bit', 'Packages': {'pytest': '8.3.5', 'pluggy': '1.5.0'}, 'Plugins': {'html': '4.1.1', 'metadata': '3.1.1', 'dependency': '0.6.0', 'ordering': '0.6', 'xdist': '3.6.1'}}
rootdir: /Users/olakoya/Desktop/Pytest
plugins: html-4.1.1, metadata-3.1.1, dependency-0.6.0, ordering-0.6, xdist-3.6.1
3 workers [4 items]     
scheduling tests via LoadScheduling

Day5/test_Parallel.py::TestTitle::test_title_chrome 
Day5/test_Parallel.py::TestTitle::test_title_firefox 
Day5/test_Parallel.py::TestTitle::test_title_edge 
[gw0] PASSED Day5/test_Parallel.py::TestTitle::test_title_chrome 
[gw2] PASSED Day5/test_Parallel.py::TestTitle::test_title_edge 
Day5/test_Parallel.py::TestTitle::test_title_safari 
[gw1] PASSED Day5/test_Parallel.py::TestTitle::test_title_firefox 
[gw0] PASSED Day5/test_Parallel.py::TestTitle::test_title_safari 

========================================================================= 4 passed in 17.94s ==========================================================================
(.venv) olakoya@MacBookPro Pytest % pytest -s -v -n=3 --os=mac --browser=chrome Day5/test_Parallel.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.9.6', 'Platform': 'macOS-10.16-x86_64-i386-64bit', 'Packages': {'pytest': '8.3.5', 'pluggy': '1.5.0'}, 'Plugins': {'html': '4.1.1', 'metadata': '3.1.1', 'dependency': '0.6.0', 'ordering': '0.6', 'xdist': '3.6.1'}}
rootdir: /Users/olakoya/Desktop/Pytest
plugins: html-4.1.1, metadata-3.1.1, dependency-0.6.0, ordering-0.6, xdist-3.6.1
3 workers [4 items]     
scheduling tests via LoadScheduling

Day5/test_Parallel.py::TestTitle::test_title_edge 
Day5/test_Parallel.py::TestTitle::test_title_chrome 
Day5/test_Parallel.py::TestTitle::test_title_firefox 
[gw2] PASSED Day5/test_Parallel.py::TestTitle::test_title_edge 
[gw0] PASSED Day5/test_Parallel.py::TestTitle::test_title_chrome 
[gw1] PASSED Day5/test_Parallel.py::TestTitle::test_title_firefox 
Day5/test_Parallel.py::TestTitle::test_title_safari 
[gw0] PASSED Day5/test_Parallel.py::TestTitle::test_title_safari 

========================================================================= 4 passed in 16.15s ==========================================================================
(.venv) olakoya@MacBookPro Pytest % pytest -s -v -n=3 --os=mac --browser=chrome Day5/test_Parallel.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.9.6', 'Platform': 'macOS-10.16-x86_64-i386-64bit', 'Packages': {'pytest': '8.3.5', 'pluggy': '1.5.0'}, 'Plugins': {'html': '4.1.1', 'metadata': '3.1.1', 'dependency': '0.6.0', 'ordering': '0.6', 'xdist': '3.6.1'}}
rootdir: /Users/olakoya/Desktop/Pytest
plugins: html-4.1.1, metadata-3.1.1, dependency-0.6.0, ordering-0.6, xdist-3.6.1
3 workers [4 items]     
scheduling tests via LoadScheduling

Day5/test_Parallel.py::TestTitle::test_title_firefox 
Day5/test_Parallel.py::TestTitle::test_title_chrome 
Day5/test_Parallel.py::TestTitle::test_title_edge 
[gw2] PASSED Day5/test_Parallel.py::TestTitle::test_title_edge 
[gw1] PASSED Day5/test_Parallel.py::TestTitle::test_title_firefox 
[gw0] PASSED Day5/test_Parallel.py::TestTitle::test_title_chrome 
Day5/test_Parallel.py::TestTitle::test_title_safari 
[gw0] PASSED Day5/test_Parallel.py::TestTitle::test_title_safari 

========================================================================= 4 passed in 13.75s ==========================================================================
(.venv) olakoya@MacBookPro Pytest % 


1st Execution

========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.9.6', 'Platform': 'macOS-10.16-x86_64-i386-64bit', 'Packages': {'pytest': '8.3.5', 'pluggy': '1.5.0'}, 'Plugins': {'html': '4.1.1', 'metadata': '3.1.1', 'dependency': '0.6.0', 'ordering': '0.6', 'xdist': '3.6.1'}}
rootdir: /Users/olakoya/Desktop/Pytest
plugins: html-4.1.1, metadata-3.1.1, dependency-0.6.0, ordering-0.6, xdist-3.6.1
3 workers [4 items]     
scheduling tests via LoadScheduling

Day5/test_Parallel.py::TestTitle::test_title_edge 
Day5/test_Parallel.py::TestTitle::test_title_chrome 
Day5/test_Parallel.py::TestTitle::test_title_firefox 
[gw0] PASSED Day5/test_Parallel.py::TestTitle::test_title_chrome 
Day5/test_Parallel.py::TestTitle::test_title_safari 
[gw0] PASSED Day5/test_Parallel.py::TestTitle::test_title_safari 
[gw2] PASSED Day5/test_Parallel.py::TestTitle::test_title_firefox 
[gw1] PASSED Day5/test_Parallel.py::TestTitle::test_title_edge 

========================================================================= 4 passed in 52.59s ==========================================================================
(.venv) olakoya@MacBookPro Pytest % 

'''

# Importing Fixture Function (first Attempt of My Code)

# @pytest.fixture()
# def setup(browser_platform): # defining parameter as browser to the fixture function (Parameter value = browser)
#     browser, platform =  browser_platform
#     options = {
#         "chrome": webdriver.ChromeOptions(),
#         "edge": webdriver.EdgeOptions(),
#         "firefox": webdriver.FirefoxOptions(),
#         "safari": webdriver.SafariOptions(),
#     }
#
#     platform_mapping = {"mac": "MAC", "windows": "WIN10", "linux": "LINUX"}
#     platform_name = platform_mapping[platform]
#     opt = options[browser]
#     opt.add_experimental_option("detach", True) if browser in ['chrome','edge','firefox','safari'] else None
#     opt.platform_name = platform_name
#     driver = webdriver.Remote(command_executor=hub_url, options=opt)
#     yield driver
#     driver.quit()
#
# def pytest_addoption(parser):
#     parser.addoption('--browser', action="store", default="chrome", help="Browser to run tests")
#     parser.addoption("--os", default='windows')
#
# @pytest.fixture()
# def browser_platform(request):
#     return request.config.getoption("--browser"),request.config.getoption("--os")
#
