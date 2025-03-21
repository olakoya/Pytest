import pytest
from selenium import webdriver

class TestTitle:

    # Method Chrome
    def test_title_chrome(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opt)
        driver.get("https://www.google.co.uk/")
        act_title = driver.title  # Lines 11 to 17 are execution for test phase
        exp_title = "Google"

        if act_title == exp_title:
                print("Test Passed")
        else:
                print("Test Failed")
        assert act_title == exp_title # Validation
        driver.quit()

    # Method Edge
    def test_title_edge(self):
        opt = webdriver.EdgeOptions()
        opt.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=opt)
        driver.get("https://www.google.co.uk/")
        act_title = driver.title  # Lines 11 to 17 are execution for test phase
        exp_title = "Google"

        if act_title == exp_title:
                print("Test Passed")
        else:
                print("Test Failed")
        assert act_title == exp_title # Validation
        driver.quit()

    # Method Firefox
    # def test_title_firefox(self):
    #     opt = webdriver.FirefoxOptions()
    #     driver = webdriver.Firefox(options=opt)
    #     driver.get("https://www.google.co.uk/")
    #     act_title = driver.title  # Lines 11 to 17 are execution for test phase
    #     exp_title = "Google"
    #
    #     if act_title == exp_title:
    #             print("Test Passed")
    #     else:
    #             print("Test Failed")
    #     assert act_title == exp_title # Validation
    #     driver.quit()

'''
Output is
============================= test session starts ==============================
collecting ... collected 3 items

test_Parallel6.py::TestTitle::test_title_chrome 
test_Parallel6.py::TestTitle::test_title_edge 
test_Parallel6.py::TestTitle::test_title_firefox 

============================== 3 passed in 51.75s ==============================
PASSED                   [ 33%]Test Passed
PASSED                     [ 66%]Test Passed
PASSED                  [100%]Test Passed

Process finished with exit code 0

'''

# Using Parallel Execution

# Code to use is  pytest -s -v -n=3 (3 means executing the 3 methods and if there are 10 methods that will be n=10 )

# Accurate code with file name is pytest -s -v -n=3 Day2/test_Parallel6.py

'''
Output after using a complete code pytest -s -v -n=3 Day2/test_Parallel6.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest/Day2
configfile: pytest.ini
plugins: dependency-0.6.0, ordering-0.6, xdist-3.6.1
3 workers [3 items]     
scheduling tests via LoadScheduling

Day2/test_Parallel6.py::TestTitle::test_title_firefox 
Day2/test_Parallel6.py::TestTitle::test_title_chrome 
Day2/test_Parallel6.py::TestTitle::test_title_edge 
[gw0] PASSED Day2/test_Parallel6.py::TestTitle::test_title_chrome 
[gw2] PASSED Day2/test_Parallel6.py::TestTitle::test_title_firefox 
[gw1] PASSED Day2/test_Parallel6.py::TestTitle::test_title_edge 

========================================================================= 3 passed in 17.47s ==========================================================================

Time is quite much as seen from the above output but after adding driver.quit to the codes output is


pytest -s -v -n=3 Day2/test_Parallel6.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest/Day2
configfile: pytest.ini
plugins: dependency-0.6.0, ordering-0.6, xdist-3.6.1
3 workers [3 items]     
scheduling tests via LoadScheduling

Day2/test_Parallel6.py::TestTitle::test_title_firefox 
Day2/test_Parallel6.py::TestTitle::test_title_chrome 
Day2/test_Parallel6.py::TestTitle::test_title_edge 
[gw0] PASSED Day2/test_Parallel6.py::TestTitle::test_title_chrome 
[gw2] PASSED Day2/test_Parallel6.py::TestTitle::test_title_firefox 
[gw1] PASSED Day2/test_Parallel6.py::TestTitle::test_title_edge 

========================================================================= 3 passed in 17.47s ==========================================================================
(.venv) olakoya@MacBookPro Pytest % pytest -s -v -n=3 Day2/test_Parallel6.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest/Day2
configfile: pytest.ini
plugins: dependency-0.6.0, ordering-0.6, xdist-3.6.1
3 workers [3 items]     
scheduling tests via LoadScheduling

Day2/test_Parallel6.py::TestTitle::test_title_firefox 
Day2/test_Parallel6.py::TestTitle::test_title_edge 
Day2/test_Parallel6.py::TestTitle::test_title_chrome 
[gw0] PASSED Day2/test_Parallel6.py::TestTitle::test_title_chrome 
[gw2] PASSED Day2/test_Parallel6.py::TestTitle::test_title_firefox 
[gw1] PASSED Day2/test_Parallel6.py::TestTitle::test_title_edge 

========================================================================= 3 passed in 11.06s ==========================================================================

Time is 11.06s



Output after commenting Firefox out 

========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest/Day2
configfile: pytest.ini
plugins: dependency-0.6.0, ordering-0.6, xdist-3.6.1
3 workers [2 items]     
scheduling tests via LoadScheduling

Day2/test_Parallel6.py::TestTitle::test_title_edge 
Day2/test_Parallel6.py::TestTitle::test_title_chrome 
[gw1] PASSED Day2/test_Parallel6.py::TestTitle::test_title_edge 
[gw0] PASSED Day2/test_Parallel6.py::TestTitle::test_title_chrome 

========================================================================== 2 passed in 5.37s ==========================================================================

Time is 5.37s on terminal


Output using run
============================= test session starts ==============================
collecting ... collected 2 items

test_Parallel6.py::TestTitle::test_title_chrome 
test_Parallel6.py::TestTitle::test_title_edge 

============================== 2 passed in 6.81s ===============================
PASSED                   [ 50%]Test Passed
PASSED                     [100%]Test Passed

Time is 6.81s for both Chrome and Edge compare to the terminal execution.
'''