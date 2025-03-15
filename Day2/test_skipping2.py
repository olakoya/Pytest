import pytest

# UnConditional Skip
# class TestClass:
#     @pytest.mark.skip(reason = "Feature not implemented")
#     def test_unfinished(self): # Defining condition through assertion
#         assert True
#
#     def test_sum(self):
#         print(3+5)

'''
Output for line 3 before adding lines 7 and 8

Testing started at 21:10 ...
Launching pytest with arguments test_skipping2.py::TestClass --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day2

============================= test session starts ==============================
collecting ... collected 1 item

test_skipping2.py::TestClass::test_unfinished PASSED                     [100%]

============================== 1 passed in 0.01s ===============================



Output for line 7

Testing started at 21:11 ...
Launching pytest with arguments test_skipping2.py::TestClass::test_sum --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day2

============================= test session starts ==============================
collecting ... collected 1 item

test_skipping2.py::TestClass::test_sum PASSED                            [100%]8


============================== 1 passed in 0.01s ===============================



Output from line 3

============================= test session starts ==============================
collecting ... collected 2 items

test_skipping2.py::TestClass::test_unfinished PASSED                     [ 50%]
test_skipping2.py::TestClass::test_sum PASSED                            [100%]8


============================== 2 passed in 0.02s ===============================



Output after adding @pytest.mark.skip

Testing started at 21:14 ...
Launching pytest with arguments test_skipping2.py::TestClass --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day2

============================= test session starts ==============================
collecting ... collected 2 items

test_skipping2.py::TestClass::test_unfinished SKIPPED (unconditional
skip)                                                                    [ 50%]
Skipped: unconditional skip

test_skipping2.py::TestClass::test_sum PASSED                            [100%]8


========================= 1 passed, 1 skipped in 0.02s =========================



Output after adding @pytest.mark.skip(reason = "Feature not implemented")

Testing started at 21:16 ...
Launching pytest with arguments test_skipping2.py::TestClass --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day2

============================= test session starts ==============================
collecting ... collected 2 items

test_skipping2.py::TestClass::test_unfinished SKIPPED (Feature not
implemented)                                                             [ 50%]
Skipped: Feature not implemented

test_skipping2.py::TestClass::test_sum PASSED                            [100%]8


========================= 1 passed, 1 skipped in 0.02s =========================

'''

# Conditional Skip

import sys

class TestClass:
    @pytest.mark.skip(reason = "Feature not implemented")
    def test_unfinished(self): # Defining condition through assertion
        assert True

    def test_sum(self):
        print(3+5)

    @pytest.mark.skipif(sys.platform == 'win32', reason="Doesn't run on windows") # This test case is executed on non windows operating system but shouldn't or be highlighted when on windows
    def test_non_windows(self):
        assert True # During execution if the system isn't windows it will skip line 105 and execute lines 106 and 107 otherwise it will FAIL

'''
Output is
============================= test session starts ==============================
collecting ... collected 3 items

test_skipping2.py::TestClass::test_unfinished SKIPPED (Feature not
implemented)                                                             [ 33%]
Skipped: Feature not implemented

test_skipping2.py::TestClass::test_sum PASSED                            [ 66%]8

test_skipping2.py::TestClass::test_non_windows PASSED                    [100%]

========================= 2 passed, 1 skipped in 0.02s =========================


Output after adding lines 95 and 105

============================= test session starts ==============================
collecting ... collected 3 items

test_skipping2.py::TestClass::test_unfinished SKIPPED (Feature not
implemented)                                                             [ 33%]
Skipped: Feature not implemented

test_skipping2.py::TestClass::test_sum PASSED                            [ 66%]8

test_skipping2.py::TestClass::test_non_windows PASSED                    [100%]

========================= 2 passed, 1 skipped in 0.03s =========================
'''