import pytest

# 1. UnConditional Skip
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

# 2. Conditional Skip

import sys

# class TestClass:
#     @pytest.mark.skip(reason = "Feature not implemented")
#     def test_unfinished(self): # Defining condition through assertion
#         assert True
#
#     def test_sum(self):
#         print(3+5)
#
#     @pytest.mark.skipif(sys.platform == 'win32', reason="Doesn't run on windows") # This test case is executed on non windows operating system but shouldn't or be highlighted when on windows
#     def test_non_windows(self):
#         assert True # During execution if the system isn't windows it will skip line 105 and execute lines 106 and 107 otherwise it will FAIL

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

# 3. Terminating or Skipping Test Execution

# import sys
#
# class TestClass:
#     @pytest.mark.skip(reason = "Feature not implemented")
#     def test_unfinished(self): # Defining condition through assertion
#         assert True
#
#     def test_sum(self):
#         print(3+5)
#
#     @pytest.mark.skipif(sys.platform == 'win32', reason="Doesn't run on windows")
#     def test_non_windows(self):
#         assert True
#
#     @pytest.fixture()
#     def skip_if_no_network(self):
#         network_available = True
#         if not network_available:
#             pytest.skip("Skipping because no network available")
#
#     # defining a method
#     def test_network_feature(self, skip_if_no_network):
#         assert True

'''
Output is
============================= test session starts ==============================
collecting ... collected 4 items

test_skipping2.py::TestClass::test_unfinished SKIPPED (Feature not
implemented)                                                             [ 25%]
Skipped: Feature not implemented

test_skipping2.py::TestClass::test_sum PASSED                            [ 50%]8

test_skipping2.py::TestClass::test_non_windows PASSED                    [ 75%]
test_skipping2.py::TestClass::test_network_feature SKIPPED (Skipping
because no network available)                                            [100%]
Skipped: Skipping because no network available

========================= 2 passed, 2 skipped in 0.02s =========================




Output after changing method in line 159 from "False" to "True"
============================= test session starts ==============================
collecting ... collected 1 item

test_skipping2.py::TestClass::test_unfinished SKIPPED (Feature not
implemented)                                                             [100%]
Skipped: Feature not implemented


============================== 1 skipped in 0.02s ==============================




Output after changing assert in line 165 from True to False 
============================= test session starts ==============================
collecting ... collected 4 items

test_skipping2.py::TestClass::test_unfinished 
test_skipping2.py::TestClass::test_sum 
test_skipping2.py::TestClass::test_non_windows 
test_skipping2.py::TestClass::test_network_feature 

==================== 1 failed, 2 passed, 1 skipped in 0.08s ====================
SKIPPED (Feature not
implemented)                                                             [ 25%]
Skipped: Feature not implemented
PASSED                            [ 50%]8
PASSED                    [ 75%]FAILED                [100%]
test_skipping2.py:163 (TestClass.test_network_feature)
self = <test_skipping2.TestClass object at 0x7ff527462610>
skip_if_no_network = None

    def test_network_feature(self, skip_if_no_network):
>       assert False
E       assert False

test_skipping2.py:165: AssertionError




Output after changing lines 159 and 165 to True
============================= test session starts ==============================
collecting ... collected 4 items

test_skipping2.py::TestClass::test_unfinished SKIPPED (Feature not
implemented)                                                             [ 25%]
Skipped: Feature not implemented

test_skipping2.py::TestClass::test_sum PASSED                            [ 50%]8

test_skipping2.py::TestClass::test_non_windows PASSED                    [ 75%]
test_skipping2.py::TestClass::test_network_feature PASSED                [100%]

========================= 3 passed, 1 skipped in 0.03s =========================
'''

# 4. Failing Feature
import sys

class TestClass:
    @pytest.mark.skip(reason = "Feature not implemented")
    def test_unfinished(self): # Defining condition through assertion
        assert True

    def test_sum(self):
        print(3+5)

    @pytest.mark.skipif(sys.platform == 'win32', reason="Doesn't run on windows")
    def test_non_windows(self):
        assert True

    @pytest.fixture()
    def skip_if_no_network(self):
        network_available = True
        if not network_available:
            pytest.skip("Skipping because no network available")

    # defining a method
    def test_network_feature(self, skip_if_no_network):
        assert True

    @pytest.mark.xfail(reason="Known bug in this feature")
    def test_failing_feature(self):
        assert False

'''
Output after adding a new method on line 270 and 271
============================= test session starts ==============================
collecting ... collected 5 items

test_skipping2.py::TestClass::test_unfinished 
test_skipping2.py::TestClass::test_sum 
test_skipping2.py::TestClass::test_non_windows 
test_skipping2.py::TestClass::test_network_feature 
test_skipping2.py::TestClass::test_failing_feature 

==================== 1 failed, 3 passed, 1 skipped in 0.05s ====================
SKIPPED (Feature not
implemented)                                                             [ 20%]
Skipped: Feature not implemented
PASSED                            [ 40%]8
PASSED                    [ 60%]PASSED                [ 80%]FAILED                [100%]
test_skipping2.py:269 (TestClass.test_failing_feature)
self = <test_skipping2.TestClass object at 0x7f9495462640>

    def test_failing_feature(self):
>       assert False
E       assert False

test_skipping2.py:271: AssertionError



Output after adding line 270
============================= test session starts ==============================
collecting ... collected 5 items

test_skipping2.py::TestClass::test_unfinished 
test_skipping2.py::TestClass::test_sum 
test_skipping2.py::TestClass::test_non_windows 
test_skipping2.py::TestClass::test_network_feature 
test_skipping2.py::TestClass::test_failing_feature 

=================== 3 passed, 1 skipped, 1 xfailed in 0.08s ====================
SKIPPED (Feature not
implemented)                                                             [ 20%]
Skipped: Feature not implemented
PASSED                            [ 40%]8
PASSED                    [ 60%]PASSED                [ 80%]XFAIL (Known bug in
this feature)                                                            [100%]
self = <test_skipping2.TestClass object at 0x7fbdde462070>

    @pytest.mark.xfail(reason="Known bug in this feature")
    def test_failing_feature(self):
>       assert False
E       assert False

test_skipping2.py:272: AssertionError

'''

# Output when used "pytest -s -v Day2/test_skipping2.py" code in the terminal to run the script
'''
Output is
(.venv) olakoya@MacBookPro Pytest % pytest -s -v Day2/test_skipping2.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest
collected 5 items                                                                                                                                                     

Day2/test_skipping2.py::TestClass::test_unfinished SKIPPED (Feature not implemented)
Day2/test_skipping2.py::TestClass::test_sum 8
PASSED
Day2/test_skipping2.py::TestClass::test_non_windows PASSED
Day2/test_skipping2.py::TestClass::test_network_feature PASSED
Day2/test_skipping2.py::TestClass::test_failing_feature XFAIL (Known bug in this feature)

=============================================================== 3 passed, 1 skipped, 1 xfailed in 0.05s ===============================================================

'''

# To display Test Case Results in the Report Code to use is "pytest -s -v -rs Day2/test_skipping2.py"
'''
Output is
(.venv) olakoya@MacBookPro Pytest % pytest -s -v -rs Day2/test_skipping2.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest
collected 5 items                                                                                                                                                     

Day2/test_skipping2.py::TestClass::test_unfinished SKIPPED (Feature not implemented)
Day2/test_skipping2.py::TestClass::test_sum 8
PASSED
Day2/test_skipping2.py::TestClass::test_non_windows PASSED
Day2/test_skipping2.py::TestClass::test_network_feature PASSED
Day2/test_skipping2.py::TestClass::test_failing_feature XFAIL (Known bug in this feature)

======================================================================= short test summary info =======================================================================
SKIPPED [1] Day2/test_skipping2.py:249: Feature not implemented
=============================================================== 3 passed, 1 skipped, 1 xfailed in 0.05s ===============================================================

'''

# To display expected Failure code to use is "pytest -s -v -rx Day2/test_skipping2.py"
'''
Output is
(.venv) olakoya@MacBookPro Pytest % pytest -s -v -rx Day2/test_skipping2.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest
collected 5 items                                                                                                                                                     

Day2/test_skipping2.py::TestClass::test_unfinished SKIPPED (Feature not implemented)
Day2/test_skipping2.py::TestClass::test_sum 8
PASSED
Day2/test_skipping2.py::TestClass::test_non_windows PASSED
Day2/test_skipping2.py::TestClass::test_network_feature PASSED
Day2/test_skipping2.py::TestClass::test_failing_feature XFAIL (Known bug in this feature)

======================================================================= short test summary info =======================================================================
XFAIL Day2/test_skipping2.py::TestClass::test_failing_feature - Known bug in this feature
=============================================================== 3 passed, 1 skipped, 1 xfailed in 0.05s ===============================================================

'''

# To display both results weather it's PASSED or FAILED code to use is "pytest -s -v -rsx Day2/test_skipping2.py"
'''
Output is
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest
collected 5 items                                                                                                                                                     

Day2/test_skipping2.py::TestClass::test_unfinished SKIPPED (Feature not implemented)
Day2/test_skipping2.py::TestClass::test_sum 8
PASSED
Day2/test_skipping2.py::TestClass::test_non_windows PASSED
Day2/test_skipping2.py::TestClass::test_network_feature PASSED
Day2/test_skipping2.py::TestClass::test_failing_feature XFAIL (Known bug in this feature)

======================================================================= short test summary info =======================================================================
SKIPPED [1] Day2/test_skipping2.py:249: Feature not implemented
XFAIL Day2/test_skipping2.py::TestClass::test_failing_feature - Known bug in this feature
=============================================================== 3 passed, 1 skipped, 1 xfailed in 0.05s ===============================================================

'''