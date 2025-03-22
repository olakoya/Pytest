class Test:
    def test_calculation(self,num1,num2):
        assert num1==num2 # This line is asserting if the numbers are equal or not

# Creating an object
t = Test()
t.test_calculation(1, 2)
t.test_calculation(1, 1)

'''
Output is 

pytest -s -v Day3/test_Parameterisation2.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.5, pluggy-1.5.0 -- /Users/olakoya/Desktop/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/olakoya/Desktop/Pytest
plugins: dependency-0.6.0, ordering-0.6, xdist-3.6.1
collected 0 items / 1 error                                                                                                                                           

=============================================================================== ERRORS ================================================================================
___________________________________________________________ ERROR collecting Day3/test_Parameterisation2.py ___________________________________________________________
Day3/test_Parameterisation2.py:7: in <module>
    t.test_calculation(1, 2)
Day3/test_Parameterisation2.py:3: in test_calculation
    assert num1==num2 # This line is asserting if the numbers are equal or not
E   assert 1 == 2
======================================================================= short test summary info =======================================================================
ERROR Day3/test_Parameterisation2.py - assert 1 == 2
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
========================================================================== 1 error in 0.19s ===========================================================================

The above execution has an output of one error based on the facts that in the object num 1 doesn't equal num 2
'''