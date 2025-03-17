'''
Pytest Framework - 2
--------------------
Skipping
---------
1. @pytest.mark(are used to call other TestCases).skip(Mark is for skipping TCs) ==> Skips unconditionally
2. @pytest.mark.skipif ==> Skips based on condition it skips some Test Cases
3. pytest.skip() ==> Skip TCs inside test execution
4. @pytest.mark.xfail ==> Mark test as expected to fail but still run it

The above method from number 1 to 4 are all features

Multiples options to manually Execute the above Skipping Methods and generates accurate results
------------------------------------------------------------------------------------------------
1. Code to run the entire script "pytest -s -v Day2/test_skipping2.py"
2. Code to use to display Test Case Results in the Report "pytest -s -v -rs Day2/test_skipping2.py"
3. Code to use to display expected Failure "pytest -s -v -rx Day2/test_skipping2.py"
4. Code to use to display both results weather it's PASSED or FAILED "pytest -s -v -rsx Day2/test_skipping2.py"


Ordering
--------
1. install pytest-ordering
2. @pytest.mark.run(order=num)
3. @pytest.mark.first

pytest.ini ==> Markers
conftest.py ==> fixtures


Dependency
-----------
1. pip install pytest-dependency
2. @pytest.mark.dependency(depends=[])



grouping
----------
smoke
sanity
regresion

@pytest.mark.groupingname

@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.regression


parallel execution
-------------------
100TC ==> 100 min

Time is saved
Results are very quick

Pytest parallel testing can significantly speed up the test execution process by running tests in parallel across multiple CPU cores. This is useful for large test suites and can reduce the time taken for test execution.

The pytest-xdist plugin enables parallel test execution in pytest. It allows tests to be distributed across multiple processors, threads, or machines.

pip install pytest-xdist

'''