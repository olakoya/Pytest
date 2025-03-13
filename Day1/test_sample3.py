# from selenium import webdriver

# class Testsample:
#     def test_sample(self):

        # opt = webdriver.ChromeOptions() # Lines 6 to 10 are prerequisites
        # opt.add_experimental_option("detach", True)
        #
        # driver = webdriver.Chrome(options=opt)
        # driver.get("https://www.google.co.uk/")

        # act_title = driver.title # Lines 11 to 17 are execution for test phase
        # exp_title = "Google"
        #
        # if act_title == exp_title:
        #     print("Test Passed")
        # else:
        #     print("Test Failed")

        # driver.quit() # This is also prerequisite
'''
Output is
Testing started at 17:36 ...
Launching pytest with arguments /Users/olakoya/Desktop/Pytest/Day1/test_sample3.py --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day1

============================= test session starts ==============================
collecting ... collected 1 item

test_sample3.py::Testsample::test_sample

============================== 1 passed in 3.01s ===============================
PASSED                           [100%]Test Passed

'''

# Defining Sets of Features
# import pytest
# from selenium import webdriver
#
# @pytest.fixture()
# def setup():
#     opt = webdriver.ChromeOptions()
#     opt.add_experimental_option("detach", True)
#
#     driver = webdriver.Chrome(options=opt)
#     yield driver # Returning some value to a test method
#     driver.quit() # Ensuring browser is closed after test execution
#
# class Testsample:
#     def test_sample(self, setup): # Passing fixture "setup" as an argument
#         self.driver = setup # instoring as class method variable
#         self.driver.get("https://www.google.co.uk/")
#         act_title = self.driver.title  # Lines 11 to 17 are execution for test phase
#         exp_title = "Google"
#
#         if act_title == exp_title:
#             print("Test Passed")
#         else:
#             print("Test Failed")
'''
Output is
Testing started at 17:48 ...
Launching pytest with arguments test_sample3.py::Testsample --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day1

============================= test session starts ==============================
collecting ... collected 1 item

test_sample3.py::Testsample::test_sample 

============================== 1 passed in 3.28s ===============================
PASSED                           [100%]Test Passed

'''

# Importing from File contest3.py
# class Testsample:
#     def test_sample(self, setup): # Passing fixture "setup" as an argument
#         self.driver = setup # instoring as class method variable
#         self.driver.get("https://www.google.co.uk/")
#         act_title = self.driver.title  # Lines 11 to 17 are execution for test phase
#         exp_title = "Googleeee"
#
#         if act_title == exp_title:
#             print("Test Passed")
#         else:
#             print("Test Failed")
'''
Output is

Testing started at 17:56 ...
Launching pytest with arguments test_sample3.py::Testsample --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day1

============================= test session starts ==============================
collecting ... collected 1 item

test_sample3.py::Testsample::test_sample 

============================== 1 passed in 3.29s ===============================
PASSED                           [100%]Test Passed

'''

'''
Executing from terminal using "-s -v Day1/test_sample3.py"

(.venv) olakoya@MacBookPro Pytest % pytest -s -v Day1/test_sample3.py 
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest
collected 1 item                                                                                                                                                      

Day1/test_sample3.py::Testsample::test_sample Test Passed
PASSED

========================================================================== 1 passed in 2.20s ==========================================================================
(.venv) olakoya@MacBookPro Pytest % 

'''

'''
Output to check if FAILED works i.e Negative testing by changing the name in line 81 from "Google" to 'Googleee'

(.venv) olakoya@MacBookPro Pytest % pytest -s -v Day1/test_sample3.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest
collected 1 item                                                                                                                                                      

Day1/test_sample3.py::Testsample::test_sample Test Failed
PASSED

========================================================================== 1 passed in 2.41s ==========================================================================
(.venv) olakoya@MacBookPro Pytest % 

'''

# Using Assertion for FAILED purpose (Assertion is a powerful tool used in performing some validations)
class Testsample:
    def test_sample(self, setup): # Passing fixture "setup" as an argument
        self.driver = setup # instoring as class method variable
        self.driver.get("https://www.google.co.uk/")
        act_title = self.driver.title  # Lines 11 to 17 are execution for test phase
        exp_title = "Googleeee"

        assert act_title==exp_title # This is performing a validation
'''
Output is 
Testing started at 18:05 ...
Launching pytest with arguments test_sample3.py::Testsample --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day1

============================= test session starts ==============================
collecting ... collected 1 item

test_sample3.py::Testsample::test_sample 

============================== 1 failed in 2.89s ===============================
FAILED                           [100%]


test_sample3.py:140 (Testsample.test_sample)
'Google' != 'Googleeee'

Expected :'Googleeee'
Actual   :'Google'
<Click to see difference>

self = <test_sample.Testsample object at 0x7ff5272eb2b0>
setup = <selenium.webdriver.chrome.webdriver.WebDriver (session="045af78479a92ac27dff5d53dd22d858")>

    def test_sample(self, setup): # Passing fixture "setup" as an argument
        self.driver = setup # instoring as class method variable
        self.driver.get("https://www.google.co.uk/")
        act_title = self.driver.title  # Lines 11 to 17 are execution for test phase
        exp_title = "Googleeee"
    
>       assert act_title==exp_title
E       AssertionError: assert 'Google' == 'Googleeee'
E         
E         - Googleeee
E         ?       ---
E         + Google

test_sample3.py:147: AssertionError

Process finished with exit code 1
'''