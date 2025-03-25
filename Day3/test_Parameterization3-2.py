import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestClass:
    @pytest.mark.parametrize('user,pwd', [('Admin', 'admin123'),('Admi', 'admin123'),('Admin', 'dmin123'),('Admin', 'admin123')])
    def test_Login(self,user,pwd): # This is a data driven testing
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("detach", True)
        opt.add_argument("--start_maximized")
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").send_keys(user)
        driver.find_element(By.NAME, "password").send_keys(pwd)
        driver.find_element(By.TAG_NAME, "button").click()
        try:
            status = driver.find_element(By.XPATH, "//h6[text()='Dashboard']").is_displayed()
            driver.quit()
            assert status == True
        except:
            driver.quit()
            assert False


        # if status==True:
        #     print("Test Method Passed")
        # else:
        #     print("Test Method Failed")


'''
Output after assigning 1 positive and 3 negative tests

.venv/lib/python3.9/site-packages/selenium/webdriver/remote/errorhandler.py:232: NoSuchElementException

During handling of the above exception, another exception occurred:

self = <test_Parameterization3-2.TestClass object at 0x7fb3b2002940>, user = 'Admi', pwd = 'dmin123'

    @pytest.mark.parametrize('user,pwd', [('Admin', 'admin123'),('Admi', 'admin123'),('Admin', 'dmin123'),('Admi', 'dmin123')])
    def test_Login(self,user,pwd): # This is a data driven testing
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("detach", True)
        opt.add_argument("--start_maximized")
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").send_keys(user)
        driver.find_element(By.NAME, "password").send_keys(pwd)
        driver.find_element(By.TAG_NAME, "button").click()
        try:
            status = driver.find_element(By.XPATH, "//h6[text()='Dashboard']").is_displayed()
            driver.quit()
            assert status == True
        except:
            driver.quit()
>           assert False
E           assert False

Day3/test_Parameterization3-2.py:23: AssertionError
======================================================================= short test summary info =======================================================================
FAILED Day3/test_Parameterization3-2.py::TestClass::test_Login[Admi-admin123] - assert False
FAILED Day3/test_Parameterization3-2.py::TestClass::test_Login[Admin-dmin123] - assert False
FAILED Day3/test_Parameterization3-2.py::TestClass::test_Login[Admi-dmin123] - assert False
==================================================================== 3 failed, 1 passed in 51.63s =====================================================================

'''

'''
Output after executing 2 positives and 2 negatives tests
During handling of the above exception, another exception occurred:

self = <test_Parameterization3-2.TestClass object at 0x7fdcc1fd38b0>, user = 'Admin', pwd = 'dmin123'

    @pytest.mark.parametrize('user,pwd', [('Admin', 'admin123'),('Admi', 'admin123'),('Admin', 'dmin123'),('Admin', 'admin123')])
    def test_Login(self,user,pwd): # This is a data driven testing
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("detach", True)
        opt.add_argument("--start_maximized")
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").send_keys(user)
        driver.find_element(By.NAME, "password").send_keys(pwd)
        driver.find_element(By.TAG_NAME, "button").click()
        try:
            status = driver.find_element(By.XPATH, "//h6[text()='Dashboard']").is_displayed()
            driver.quit()
            assert status == True
        except:
            driver.quit()
>           assert False
E           assert False

Day3/test_Parameterization3-2.py:23: AssertionError
======================================================================= short test summary info =======================================================================
FAILED Day3/test_Parameterization3-2.py::TestClass::test_Login[Admi-admin123] - assert False
FAILED Day3/test_Parameterization3-2.py::TestClass::test_Login[Admin-dmin123] - assert False
==================================================================== 2 failed, 2 passed in 44.19s =====================================================================

'''

'''
Output after creating conftest.py file
Day3/test_Parameterization3-2.py:23: AssertionError
========================================================================== warnings summary ===========================================================================
Day3/conftest.py:4
  /Users/olakoya/Desktop/Pytest/Day3/conftest.py:4: PytestDeprecationWarning: The hookimpl pytest_metadata uses old-style configuration options (marks or attributes).
  Please use the pytest.hookimpl(optionalhook=True) decorator instead
   to configure the hooks.
   See https://docs.pytest.org/en/latest/deprecations.html#configuring-hook-specs-impls-using-markers
    @pytest.mark.optionalhook

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================= short test summary info =======================================================================
FAILED Day3/test_Parameterization3-2.py::TestClass::test_Login[Admi-admin123] - assert False
FAILED Day3/test_Parameterization3-2.py::TestClass::test_Login[Admin-dmin123] - assert False
=============================================================== 2 failed, 2 passed, 1 warning in 42.35s ===============================================================
(.venv) olakoya@MacBookPro Pytest % 

'''