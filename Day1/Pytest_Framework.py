'''
Pytest Framework -1
--------------------
Testing framework
unit,Integration and functional

Features of Pytest Framework
-----------------------------
Fixtures
Parallel Testing
Skipping Tests
Group Test Cases
Batch Testing
Parameterization
Detailed Reports

pip install pytest

Project Stucture
----------------
Project ==> Test Suite(Package/Directory)  ==> Test Cases(Modules(.py)) ==> Test Steps(Test Methods)

Naming Conventions in pytest framework
-----------------------------------------
Modules ==> test_ or _test
	test_login.py or login_test.py
Class ==> Test
	TestClass
TestMethods ==> test
	testMethod(self)



Pytest Fixtures
---------------
fixtures are functions that manage the setup and teardown process for test environments. Fixtures allow you to define code that needs to run before a test (setup) and after a test (teardown), ensuring a controlled and repeatable test environment. They help in avoiding code duplication, keeping test logic clear, and sharing reusable setup logic across multiple tests.


Setup
------
This is the preparation phase that occurs before the test runs. It involves allocating resources, setting initial conditions, or configuring external dependencies like databases, files, or networks.

Teardown
--------
This is the cleanup phase that occurs after the test completes, regardless of whether the test passes or fails. It ensures that any resources used during the test are released, cleaned, or reset, such as closing database connections or deleting temporary files.


Fixture functions are passed as an argument to testMethod.
fixtures functions also returns value when called which is optional


Scope of fixtures
------------------
Function Scope: Fixture is called once per test function.
Class Scope: Fixture is called once per class, shared by all test methods in that class.
Module Scope: Fixture is called once per module, shared by all test functions in that file.
Session Scope: Fixture is called once per session, shared by all tests in the test run.


Session Scope is useful when you need to set up something that should last for the entire test run, like a database connection.


Autouse Fixtures
----------------
gobal setup and Teardowns

Conftest file
---------------
For better code maintenance we will specify Configurations and fixtures in conftest.py and pass as argument in testMethods in modules



In Pytest by default all the testMethods will be passed unless we put assertions (validation point).
Pytest automatically discovers and loads the `conftest.py` file for configurations and fixtures if it's in the same directory as the test modules. If it's outside the directory, Pytest won't recognize it.



'''