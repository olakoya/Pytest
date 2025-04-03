from selenium import webdriver
from LoginPageObjects import LoginPage

# Creating Test Login Class
class TestLogin:
    def test_login(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument("--start-maximized")
        opt.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        lp = LoginPage(driver) # Creating object of a class
        lp.setUserName("Admin")
        lp.setPassWord("admin123")
        lp.clickLogin()
        act_title = driver.title # adding a particular instance
        driver.quit()
        assert act_title == "OrangeHRM"

'''
Output is
(.venv) olakoya@MacBookPro Pytest % pytest -s -v Day4/test_Login.py          
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.9.6', 'Platform': 'macOS-10.16-x86_64-i386-64bit', 'Packages': {'pytest': '8.3.5', 'pluggy': '1.5.0'}, 'Plugins': {'html': '4.1.1', 'metadata': '3.1.1', 'dependency': '0.6.0', 'ordering': '0.6', 'xdist': '3.6.1'}}
rootdir: /Users/olakoya/Desktop/Pytest
plugins: html-4.1.1, metadata-3.1.1, dependency-0.6.0, ordering-0.6, xdist-3.6.1
collected 1 item                                                                                                                                                      

Day4/test_Login.py::TestLogin::test_login PASSED

========================================================================== 1 passed in 8.93s ==========================================================================
(.venv) olakoya@MacBookPro Pytest % 

'''