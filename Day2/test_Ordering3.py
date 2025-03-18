import pytest

# class TestClass:
#     def testMethodC(self):
#         print("Running Method C...")
#
#     def testMethodD(self):
#             print("Running Method D...")
#
#     def testMethodE(self):
#         print("Running Method E...")
#
#     def testMethodA(self):
#         print("Running Method A...")
#
#     def testMethodB(self):
#         print("Running Method B...")
# Python is an interpreted language
'''
Output is
============================= test session starts ==============================
collecting ... collected 5 items

test_Ordering3.py::TestClass::testMethodC PASSED                         [ 20%]Running Method C...

test_Ordering3.py::TestClass::testMethodD PASSED                         [ 40%]Running Method D...

test_Ordering3.py::TestClass::testMethodE PASSED                         [ 60%]Running Method E...

test_Ordering3.py::TestClass::testMethodA PASSED                         [ 80%]Running Method A...

test_Ordering3.py::TestClass::testMethodB PASSED                         [100%]Running Method B...


============================== 5 passed in 0.03s ===============================
'''

# # Ordering i.e executing in orderliness
# class TestClass:
#     @pytest.mark.third
#     def testMethodC(self):
#         print("Running Method C...")
#
#     @pytest.mark.fifth
#     def testMethodD(self):
#             print("Running Method D...")
#
#     @pytest.mark.sixth
#     def testMethodE(self):
#         print("Running Method E...")
#
#     @pytest.mark.first
#     def testMethodA(self):
#         print("Running Method A...")
#
#     @pytest.mark.second
#     def testMethodB(self):
#         print("Running Method B...")
'''
Output is
============================= test session starts ==============================
collecting ... collected 5 items

test_Ordering3.py::TestClass::testMethodA PASSED                         [ 20%]Running Method A...

test_Ordering3.py::TestClass::testMethodB PASSED                         [ 40%]Running Method B...

test_Ordering3.py::TestClass::testMethodC PASSED                         [ 60%]Running Method C...

test_Ordering3.py::TestClass::testMethodD PASSED                         [ 80%]Running Method D...

test_Ordering3.py::TestClass::testMethodE PASSED                         [100%]Running Method E...


======================== 5 passed, 5 warnings in 0.03s =========================
'''

'''
Output using code "pytest -s -v Day2/test_Ordering3.py' in terminal
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest
plugins: ordering-0.6
collected 5 items                                                                                                                                                     

Day2/test_Ordering3.py::TestClass::testMethodA Running Method A...
PASSED
Day2/test_Ordering3.py::TestClass::testMethodB Running Method B...
PASSED
Day2/test_Ordering3.py::TestClass::testMethodC Running Method C...
PASSED
Day2/test_Ordering3.py::TestClass::testMethodD Running Method D...
PASSED
Day2/test_Ordering3.py::TestClass::testMethodE Running Method E...
PASSED

========================================================================== warnings summary ===========================================================================
Day2/test_Ordering3.py:40
  /Users/olakoya/Desktop/Pytest/Day2/test_Ordering3.py:40: PytestUnknownMarkWarning: Unknown pytest.mark.third - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.third

Day2/test_Ordering3.py:44
  /Users/olakoya/Desktop/Pytest/Day2/test_Ordering3.py:44: PytestUnknownMarkWarning: Unknown pytest.mark.fifth - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.fifth

Day2/test_Ordering3.py:48
  /Users/olakoya/Desktop/Pytest/Day2/test_Ordering3.py:48: PytestUnknownMarkWarning: Unknown pytest.mark.sixth - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.sixth

Day2/test_Ordering3.py:52
  /Users/olakoya/Desktop/Pytest/Day2/test_Ordering3.py:52: PytestUnknownMarkWarning: Unknown pytest.mark.first - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.first

Day2/test_Ordering3.py:56
  /Users/olakoya/Desktop/Pytest/Day2/test_Ordering3.py:56: PytestUnknownMarkWarning: Unknown pytest.mark.second - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.second

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
==================================================================== 5 passed, 5 warnings in 0.04s ====================================================================


With this "warnings summary" and "PytestUnknownMarkWarning: Unknown pytest.mark.third - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.third" in the output shows pytest doesn't understand the first, second, third, forth, and fifth in @pytest.mark, first etc
    
So, solution is best to use "pytest.ini ==> Markers"
'''

'''
Output after creating the "pytest.ini" file
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest/Day2
configfile: pytest.ini
plugins: ordering-0.6
collected 5 items                                                                                                                                                     

Day2/test_Ordering3.py::TestClass::testMethodA Running Method A...
PASSED
Day2/test_Ordering3.py::TestClass::testMethodB Running Method B...
PASSED
Day2/test_Ordering3.py::TestClass::testMethodC Running Method C...
PASSED
Day2/test_Ordering3.py::TestClass::testMethodD Running Method D...
PASSED
Day2/test_Ordering3.py::TestClass::testMethodE Running Method E...
PASSED

========================================================================== 5 passed in 0.04s ==========================================================================

The created text file is used to inform pytest of any new word you want to use in your code
'''

# Ordering in "ini and conftest"
class TestClass:
    @pytest.mark.run(order=3)
    def testMethodC(self):
        print("Running Method C...")

    @pytest.mark.run(order=5)
    def testMethodD(self):
            print("Running Method D...")

    @pytest.mark.run(order=6)
    def testMethodE(self):
        print("Running Method E...")

    @pytest.mark.run(order=1)
    def testMethodA(self):
        print("Running Method A...")

    @pytest.mark.run(order=2)
    def testMethodB(self):
        print("Running Method B...")
'''
Output is
============================= test session starts ==============================
collecting ... collected 5 items

test_Ordering3.py::TestClass::testMethodA PASSED                         [ 20%]Running Method A...

test_Ordering3.py::TestClass::testMethodB PASSED                         [ 40%]Running Method B...

test_Ordering3.py::TestClass::testMethodC PASSED                         [ 60%]Running Method C...

test_Ordering3.py::TestClass::testMethodD PASSED                         [ 80%]Running Method D...

test_Ordering3.py::TestClass::testMethodE PASSED                         [100%]Running Method E...


============================== 5 passed in 0.03s ===============================



Output In terminal
(.venv) olakoya@MacBookPro Pytest % pytest -s -v Day2/test_Ordering3.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest/Day2
configfile: pytest.ini
plugins: ordering-0.6
collected 5 items                                                                                                                                                     

Day2/test_Ordering3.py::TestClass::testMethodA Running Method A...
PASSED
Day2/test_Ordering3.py::TestClass::testMethodB Running Method B...
PASSED
Day2/test_Ordering3.py::TestClass::testMethodC Running Method C...
PASSED
Day2/test_Ordering3.py::TestClass::testMethodD Running Method D...
PASSED
Day2/test_Ordering3.py::TestClass::testMethodE Running Method E...
PASSED

========================================================================== 5 passed in 0.04s ==========================================================================

'''