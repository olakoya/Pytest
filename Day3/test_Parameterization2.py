# class Test:
#     def test_calculation(self,num1,num2):
#         assert num1==num2 # This line is asserting if the numbers are equal or not
#
# # Creating an object
# t = Test()
# t.test_calculation(1, 2)
# t.test_calculation(1, 1)

'''
Output is 

pytest -s -v Day3/test_Parameterization2.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest
plugins: dependency-0.6.0, ordering-0.6, xdist-3.6.1
collected 0 items / 1 error                                                                                                                                           

=============================================================================== ERRORS ================================================================================
___________________________________________________________ ERROR collecting Day3/test_Parameterization2.py ___________________________________________________________
Day3/test_Parameterization2.py:7: in <module>
    t.test_calculation(1, 2)
Day3/test_Parameterization2.py:3: in test_calculation
    assert num1==num2 # This line is asserting if the numbers are equal or not
E   assert 1 == 2
======================================================================= short test summary info =======================================================================
ERROR Day3/test_Parameterization2.py - assert 1 == 2
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
========================================================================== 1 error in 0.19s ===========================================================================

The above execution has an output of one error based on the facts that in the object num 1 doesn't equal num 2
'''

import pytest
class Test:
    @pytest.mark.parametrize('num1,num2',[(1,2),(1,1)]) # Test data is 1, 2
    def test_calculation(self, num1, num2):
        assert num1==num2
'''
Output for [(1,2), (1,2)] is
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest
plugins: dependency-0.6.0, ordering-0.6, xdist-3.6.1
collected 2 items                                                                                                                                                     

Day3/test_Parameterization2.py::Test::test_calculation[1-2_0] FAILED
Day3/test_Parameterization2.py::Test::test_calculation[1-2_1] FAILED

============================================================================== FAILURES ===============================================================================
____________________________________________________________________ Test.test_calculation[1-2_0] _____________________________________________________________________

self = <test_Parameterization2.Test object at 0x7fb66432aee0>, num1 = 1, num2 = 2

    @pytest.mark.parametrize('num1,num2',[(1,2),(1,2)]) # Test data is 1, 2
    def test_calculation(self, num1, num2):
>       assert num1==num2
E       assert 1 == 2

Day3/test_Parameterization2.py:40: AssertionError
____________________________________________________________________ Test.test_calculation[1-2_1] _____________________________________________________________________

self = <test_Parameterization2.Test object at 0x7fb6643409a0>, num1 = 1, num2 = 2

    @pytest.mark.parametrize('num1,num2',[(1,2),(1,2)]) # Test data is 1, 2
    def test_calculation(self, num1, num2):
>       assert num1==num2
E       assert 1 == 2

Day3/test_Parameterization2.py:40: AssertionError
======================================================================= short test summary info =======================================================================
FAILED Day3/test_Parameterization2.py::Test::test_calculation[1-2_0] - assert 1 == 2
FAILED Day3/test_Parameterization2.py::Test::test_calculation[1-2_1] - assert 1 == 2
========================================================================== 2 failed in 0.07s ==========================================================================
(.venv) olakoya@MacBookPro Pytest % pyt
'''

'''
Output for [(1,2), (1,1)] is
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest
plugins: dependency-0.6.0, ordering-0.6, xdist-3.6.1
collected 2 items                                                                                                                                                     

Day3/test_Parameterization2.py::Test::test_calculation[1-2] FAILED
Day3/test_Parameterization2.py::Test::test_calculation[1-1] PASSED

============================================================================== FAILURES ===============================================================================
_____________________________________________________________________ Test.test_calculation[1-2] ______________________________________________________________________

self = <test_Parameterization2.Test object at 0x7fc365c511f0>, num1 = 1, num2 = 2

    @pytest.mark.parametrize('num1,num2',[(1,2),(1,1)]) # Test data is 1, 2
    def test_calculation(self, num1, num2):
>       assert num1==num2
E       assert 1 == 2

Day3/test_Parameterization2.py:40: AssertionError
======================================================================= short test summary info =======================================================================
FAILED Day3/test_Parameterization2.py::Test::test_calculation[1-2] - assert 1 == 2
===================================================================== 1 failed, 1 passed in 0.10s =====================================================================
(.venv) olakoya@MacBookPro Pytest % 

'''