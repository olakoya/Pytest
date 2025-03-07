'''
Pytest Framework -1
--------------------
- Pytest is a Testing framework
- Pytest can be used to test application for unit, integration and functional

Different Features of Pytest Framework
---------------------------------------
1. Fixtures: Cleaning of code and use in database
2. Parallel Testing: Timeframe
3. Skipping Tests: Unused Test cases
4. Group Test Cases: Selecting of TC
5. Batch Testing: Use for large suits
6. Parameterization: Passing data from Excel sheet to application
7. Detailed Reports: Using HTML to generate reports for TC

- Before running Pytest one needs to install the library and this is the command line to use ==> pip install pytest
- Install selenium ==> pip install selenium
- Then ==> pip install pytest
- Check Pytest library with command ==> pip list

To install other files: PYTHON INTEGRATED TOOLS
-------------------------------------------------
- Click on file
- Click on settings
- Click on Appearance & Behaviour
- Click on Project: pytestFramework
- Click on Python Interpreter
- To install more files you click on "+" on the page to the right
- And type in the search box to search for a specific package
- Click on install package button to install and ok
- And then all the files will be installed
- if a file needs updating it will prompt you in the terminal
- Then follow instructions and afterwards all files will be updated
- Before starting to write the project one needs to ensure PYTHON INTEGRATED TOOLS is installed
- To check
    - Go to file
    - Go to settings
    - Go to Tools
    - Go to Diff & Merge
    - Click on PYTHON INTEGRATED TOOLS
    - Ensure Testing ==> Default Test Runner: Autodetect(pytest) ==> Analyse Python Code in Docstrings is ticked
    - Then click Ok button


Project Structure
------------------
==> Project consists of ==> Test Suite and this is created in form of a (Package/Directory)
==> And Test Suite is a collection of ==> Test Cases and this is created in form of a (Modules(.py))
==> And Test Case is a collection of ==> Test Steps and this is created in form of a (Test Methods)

And the above structure is created in the form of Programming Language Principles

Naming Conventions in pytest framework (One needs to follow this naming conventions to understand each step of the structure)
-----------------------------------------------------------------------------------------------------------------------------
- Modules (means .py files (and python file is nothing but a module)) ==> Modules name must always start with ==> test_ or _test
	E.g ==> test_login.py or login_test.py
- Module consists of Classes. Class name must always start with ==> Test (with a capital letter T)
	E.g ==> TestClass
- Class consists of ==> TestMethods ==> and to specify the name it must start with ==> test (small letter t)
	E.g ==> testMethod(self)

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