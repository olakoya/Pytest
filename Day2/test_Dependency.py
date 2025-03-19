# class TestClass:
#     def test_OpenApp(self): # Sequence of steps from this line to LogOut
#         assert True
#
#     def test_Login(self):
#         assert False
#
#     def test_Search(self):
#         assert True
#
#     def test_AdvanceSearch(self):
#         assert True
#
#     def test_LogOut(self):
#         assert True
'''
Output for line 9 "assert false"
============================= test session starts ==============================
collecting ... collected 5 items

test_Dependency.py::TestClass::test_OpenApp PASSED                       [ 20%]
test_Dependency.py::TestClass::test_Login PASSED                         [ 40%]
test_Dependency.py::TestClass::test_Search FAILED                        [ 60%]
test_Dependency.py:7 (TestClass.test_Search)
self = <test_Dependency.TestClass object at 0x7f936e375370>

    def test_Search(self):
>       assert False
E       assert False

test_Dependency.py:9: AssertionError

test_Dependency.py::TestClass::test_AdvanceSearch PASSED                 [ 80%]
test_Dependency.py::TestClass::test_LogOut PASSED                        [100%]

========================= 1 failed, 4 passed in 0.07s ==========================




Output for line 6 "assert false"
============================= test session starts ==============================
collecting ... collected 5 items

test_Dependency.py::TestClass::test_OpenApp PASSED                       [ 20%]
test_Dependency.py::TestClass::test_Login FAILED                         [ 40%]
test_Dependency.py:4 (TestClass.test_Login)
self = <test_Dependency.TestClass object at 0x7fde13b753a0>

    def test_Login(self):
>       assert False
E       assert False

test_Dependency.py:6: AssertionError

test_Dependency.py::TestClass::test_Search PASSED                        [ 60%]
test_Dependency.py::TestClass::test_AdvanceSearch PASSED                 [ 80%]
test_Dependency.py::TestClass::test_LogOut PASSED                        [100%]

========================= 1 failed, 4 passed in 0.06s ==========================

The reason login Failed and LogOut Passed is because there's a dependency between methods

'''
import pytest


class TestClass:
    @pytest.mark.dependency()
    def test_OpenApp(self): # Sequence of steps from this line to LogOut
        assert True

    @pytest.mark.dependency(depends = ['TestClass::test_OpenApp'])
    def test_Login(self):
        assert False

    @pytest.mark.dependency(depends = ['TestClass::test_Login'])
    def test_Search(self):
        assert True

    @pytest.mark.dependency(depends = ['TestClass::test_Search'])
    def test_AdvanceSearch(self):
        assert True

    @pytest.mark.dependency(depends = ['TestClass::test_Login'])
    def test_LogOut(self):
        assert True
'''
Output is
============================= test session starts ==============================
collecting ... collected 5 items

test_Dependency.py::TestClass::test_OpenApp PASSED                       [ 20%]
test_Dependency.py::TestClass::test_Login FAILED                         [ 40%]
test_Dependency.py:72 (TestClass.test_Login)
self = <test_Dependency.TestClass object at 0x7f814fb60eb0>

    @pytest.mark.dependency(depends = ['TestClass::test_OpenApp'])
    def test_Login(self):
>       assert False
E       assert False

test_Dependency.py:75: AssertionError

test_Dependency.py::TestClass::test_Search SKIPPED (test_Search depends
on TestClass::test_Login)                                                [ 60%]
Skipped: test_Search depends on TestClass::test_Login

test_Dependency.py::TestClass::test_AdvanceSearch SKIPPED                [ 80%]
Skipped: test_AdvanceSearch depends on TestClass::test_Search

test_Dependency.py::TestClass::test_LogOut SKIPPED (test_LogOut depends
on TestClass::test_Login)                                                [100%]
Skipped: test_LogOut depends on TestClass::test_Login


==================== 1 failed, 1 passed, 3 skipped in 0.07s ====================



Output on terminal using code pytest -s -v Day2/test_Dependency.py

========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest/Day2
configfile: pytest.ini
plugins: dependency-0.6.0, ordering-0.6
collected 5 items                                                                                                                                                     

Day2/test_Dependency.py::TestClass::test_OpenApp PASSED
Day2/test_Dependency.py::TestClass::test_Login FAILED
Day2/test_Dependency.py::TestClass::test_Search SKIPPED (test_Search depends on TestClass::test_Login)
Day2/test_Dependency.py::TestClass::test_AdvanceSearch SKIPPED (test_AdvanceSearch depends on TestClass::test_Search)
Day2/test_Dependency.py::TestClass::test_LogOut SKIPPED (test_LogOut depends on TestClass::test_Login)

============================================================================== FAILURES ===============================================================================
________________________________________________________________________ TestClass.test_Login _________________________________________________________________________

self = <test_Dependency.TestClass object at 0x7f78b82a26a0>

    @pytest.mark.dependency(depends = ['TestClass::test_OpenApp'])
    def test_Login(self):
>       assert False
E       assert False

Day2/test_Dependency.py:75: AssertionError
======================================================================= short test summary info =======================================================================
FAILED Day2/test_Dependency.py::TestClass::test_Login - assert False
=============================================================== 1 failed, 1 passed, 3 skipped in 0.09s ================================================================
(.venv) olakoya@MacBookPro Pytest % 

'''