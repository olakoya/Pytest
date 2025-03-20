import pytest

class TestClass:
    @pytest.mark.sanity
    def test_LoginByEmail(self):
        print("This is Login by Email.....")
        assert 1 == 1

    @pytest.mark.smoke
    def test_LoginByEmail(self):
        print("This is Login by Email.....")
        assert 1 == 1

    @pytest.mark.sanity
    def test_LoginByFacebook(self):
        print("This is Login by Facebook.....")
        assert 1 == 1

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_LoginByTwitter(self):
        print("This is Login by Twitter.....")
        assert 1 == 1

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_SignUpByEmail(self):
        print("This is Signup by Email Test")
        assert True == True

    @pytest.mark.regression
    def test_SignUpByFacebook(self):
        print("This is Signup by Facebook Test")
        assert True == True

    @pytest.mark.regression
    def test_SignUpByTwitter(self):
        print("This is Signup by Twitter Test")
        assert True == True

    @pytest.mark.smoke
    def test_SignUpByTwitter(self):
        print("This is Signup by Twitter Test")
        assert True == True

'''
Output is
============================= test session starts ==============================
collecting ... collected 6 items

test_Grouping5.py::TestClass::test_LoginByEmail PASSED                   [ 16%]This is Login by Email.....

test_Grouping5.py::TestClass::test_LoginByFacebook PASSED                [ 33%]This is Login by Facebook.....

test_Grouping5.py::TestClass::test_LoginByTwitter PASSED                 [ 50%]This is Login by Twitter.....

test_Grouping5.py::TestClass::test_SignUpByEmail PASSED                  [ 66%]This is Signup by Email Test

test_Grouping5.py::TestClass::test_SignUpByFacebook PASSED               [ 83%]This is Signup by Facebook Test

test_Grouping5.py::TestClass::test_SignUpByTwitter PASSED                [100%]This is Signup by Twitter Test


======================== 6 passed, 10 warnings in 0.04s ========================
'''

'''
Output on terminal using code pytest -s -v Day2/test_Grouping5.py
(.venv) olakoya@MacBookPro Pytest % pytest -s -v Day2/test_Grouping5.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest/Day2
configfile: pytest.ini
plugins: dependency-0.6.0, ordering-0.6
collected 6 items                                                                                                                                                     

Day2/test_Grouping5.py::TestClass::test_LoginByEmail This is Login by Email.....
PASSED
Day2/test_Grouping5.py::TestClass::test_LoginByFacebook This is Login by Facebook.....
PASSED
Day2/test_Grouping5.py::TestClass::test_LoginByTwitter This is Login by Twitter.....
PASSED
Day2/test_Grouping5.py::TestClass::test_SignUpByEmail This is Signup by Email Test
PASSED
Day2/test_Grouping5.py::TestClass::test_SignUpByFacebook This is Signup by Facebook Test
PASSED
Day2/test_Grouping5.py::TestClass::test_SignUpByTwitter This is Signup by Twitter Test
PASSED

========================================================================== warnings summary ===========================================================================
Day2/test_Grouping5.py:4
  /Users/olakoya/Desktop/Pytest/Day2/test_Grouping5.py:4: PytestUnknownMarkWarning: Unknown pytest.mark.sanity - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.sanity

Day2/test_Grouping5.py:9
  /Users/olakoya/Desktop/Pytest/Day2/test_Grouping5.py:9: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.smoke

Day2/test_Grouping5.py:14
  /Users/olakoya/Desktop/Pytest/Day2/test_Grouping5.py:14: PytestUnknownMarkWarning: Unknown pytest.mark.sanity - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.sanity

Day2/test_Grouping5.py:19
  /Users/olakoya/Desktop/Pytest/Day2/test_Grouping5.py:19: PytestUnknownMarkWarning: Unknown pytest.mark.sanity - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.sanity

Day2/test_Grouping5.py:20
  /Users/olakoya/Desktop/Pytest/Day2/test_Grouping5.py:20: PytestUnknownMarkWarning: Unknown pytest.mark.regression - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.regression

Day2/test_Grouping5.py:25
  /Users/olakoya/Desktop/Pytest/Day2/test_Grouping5.py:25: PytestUnknownMarkWarning: Unknown pytest.mark.sanity - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.sanity

Day2/test_Grouping5.py:26
  /Users/olakoya/Desktop/Pytest/Day2/test_Grouping5.py:26: PytestUnknownMarkWarning: Unknown pytest.mark.regression - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.regression

Day2/test_Grouping5.py:31
  /Users/olakoya/Desktop/Pytest/Day2/test_Grouping5.py:31: PytestUnknownMarkWarning: Unknown pytest.mark.regression - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.regression

Day2/test_Grouping5.py:36
  /Users/olakoya/Desktop/Pytest/Day2/test_Grouping5.py:36: PytestUnknownMarkWarning: Unknown pytest.mark.regression - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.regression

Day2/test_Grouping5.py:41
  /Users/olakoya/Desktop/Pytest/Day2/test_Grouping5.py:41: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.smoke

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=================================================================== 6 passed, 10 warnings in 0.08s ====================================================================

Whatever Marker name one is using isn't available by this pytest '@pytest.mark.smoke'
'''

# Warning comes as a result of regression, smoke and sanity not installed on the pytest library.
# However, after adding them to the pytest.ini test file the warnings disappeared after execution

'''
Output after adding regression, smoke and sanity to the pytest.ini
============================= test session starts ==============================
collecting ... collected 6 items

test_Grouping5.py::TestClass::test_LoginByEmail PASSED                   [ 16%]This is Login by Email.....

test_Grouping5.py::TestClass::test_LoginByFacebook PASSED                [ 33%]This is Login by Facebook.....

test_Grouping5.py::TestClass::test_LoginByTwitter PASSED                 [ 50%]This is Login by Twitter.....

test_Grouping5.py::TestClass::test_SignUpByEmail PASSED                  [ 66%]This is Signup by Email Test

test_Grouping5.py::TestClass::test_SignUpByFacebook PASSED               [ 83%]This is Signup by Facebook Test

test_Grouping5.py::TestClass::test_SignUpByTwitter PASSED                [100%]This is Signup by Twitter Test


============================== 6 passed in 0.03s ===============================




(.venv) olakoya@MacBookPro Pytest % pytest -s -v Day2/test_Grouping5.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest/Day2
configfile: pytest.ini
plugins: dependency-0.6.0, ordering-0.6
collected 6 items                                                                                                                                                     

Day2/test_Grouping5.py::TestClass::test_LoginByEmail This is Login by Email.....
PASSED
Day2/test_Grouping5.py::TestClass::test_LoginByFacebook This is Login by Facebook.....
PASSED
Day2/test_Grouping5.py::TestClass::test_LoginByTwitter This is Login by Twitter.....
PASSED
Day2/test_Grouping5.py::TestClass::test_SignUpByEmail This is Signup by Email Test
PASSED
Day2/test_Grouping5.py::TestClass::test_SignUpByFacebook This is Signup by Facebook Test
PASSED
Day2/test_Grouping5.py::TestClass::test_SignUpByTwitter This is Signup by Twitter Test
PASSED

========================================================================== 6 passed in 0.05s ==========================================================================

'''

# To execute a specific test -m "sanity" is added to the terminal code

'''
Output after adding -m "sanity" ==> pytest -s -v -m "sanity" Day2/test_Grouping5.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest/Day2
configfile: pytest.ini
plugins: dependency-0.6.0, ordering-0.6
collected 6 items / 3 deselected / 3 selected                                                                                                                         

Day2/test_Grouping5.py::TestClass::test_LoginByFacebook This is Login by Facebook.....
PASSED
Day2/test_Grouping5.py::TestClass::test_LoginByTwitter This is Login by Twitter.....
PASSED
Day2/test_Grouping5.py::TestClass::test_SignUpByEmail This is Signup by Email Test
PASSED

=================================================================== 3 passed, 3 deselected in 0.05s ===================================================================

Smoke and Regression deselected because they are not grouped under sanity
'''

'''
Output for Smoke ==> pytest -s -v -m "smoke" Day2/test_Grouping5.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest/Day2
configfile: pytest.ini
plugins: dependency-0.6.0, ordering-0.6
collected 6 items / 4 deselected / 2 selected                                                                                                                         

Day2/test_Grouping5.py::TestClass::test_LoginByEmail This is Login by Email.....
PASSED
Day2/test_Grouping5.py::TestClass::test_SignUpByTwitter This is Signup by Twitter Test
PASSED

=================================================================== 2 passed, 4 deselected in 0.05s ===================================================================

'''

'''
Output for Regression ==> Pytest % pytest -s -v -m "regression" Day2/test_Grouping5.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest/Day2
configfile: pytest.ini
plugins: dependency-0.6.0, ordering-0.6
collected 6 items / 3 deselected / 3 selected                                                                                                                         

Day2/test_Grouping5.py::TestClass::test_LoginByTwitter This is Login by Twitter.....
PASSED
Day2/test_Grouping5.py::TestClass::test_SignUpByEmail This is Signup by Email Test
PASSED
Day2/test_Grouping5.py::TestClass::test_SignUpByFacebook This is Signup by Facebook Test
PASSED

=================================================================== 3 passed, 3 deselected in 0.04s ===================================================================

'''