import pytest

# 1. Function Scope:
# @pytest.fixture() # Decorated Function specifying the scope here i.e scope = class
#
# def setup (): # Fixture Function
#     print("Launching Browser") # Having simple statement inside the function (prerequisite)
#     yield # Teardown
#     print("Closing Browser")
# class TestClass: # Creating a Class
#     def testLogin(self,setup): # Method 1 - Passing as an arguement before execution
#         print("This is Login Test") # Passing as an arguement after execution
#     def testLogout(self, setup): # Method 2
#         print("This is Logout Test")

'''
Output is
Testing started at 18:09 ...
Launching pytest with arguments test_1.py::TestClass::testLogin --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day1

============================= test session starts ==============================
collecting ... collected 1 item

test_1.py::TestClass::testLogin Launching Browser
PASSED                                   [100%]This is Login Test


============================== 1 passed in 0.02s ===============================
'''

# 2. Class Scope
# @pytest.fixture(scope = "class") # Class
# def setup (): # Fixture Function
#     print("Launching Browser") # Having simple statement inside the function (prerequisite)
#     yield # Teardown
#     print("Closing Browser")

# class TestClass: # Creating a Class
#     def testLogin(self): # Method 1 - Passing as an arguement before execution
#         print("This is Login Test") # Passing as an arguement after execution
#     def testLogout(self): # Method 2
#         print("This is Logout Test")
'''
Line 39 Output is
Testing started at 18:41 ...
Launching pytest with arguments test_function_scope.py::TestClass::testLogin --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day1

============================= test session starts ==============================
collecting ... collected 1 item

test_function_scope.py::TestClass::testLogin PASSED                      [100%]This is Login Test


============================== 1 passed in 0.02s ===============================

Line 41 Output is
Testing started at 18:43 ...
Launching pytest with arguments test_function_scope.py::TestClass::testLogout --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day1

============================= test session starts ==============================
collecting ... collected 1 item

test_function_scope.py::TestClass::testLogout PASSED                     [100%]This is Logout Test


============================== 1 passed in 0.01s ===============================

Line 38 Output is
Testing started at 18:44 ...
Launching pytest with arguments test_function_scope.py::TestClass --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day1

============================= test session starts ==============================
collecting ... collected 2 items

test_function_scope.py::TestClass::testLogin PASSED                      [ 50%]This is Login Test

test_function_scope.py::TestClass::testLogout PASSED                     [100%]This is Logout Test


============================== 2 passed in 0.02s ===============================

'''
# @pytest.fixture(scope = "class") # Class
# def setup (): # Fixture Function
#     print("Launching Browser") # Having simple statement inside the function (prerequisite)
#     yield # Teardown
#     print("Closing Browser")
# class TestClass: # Creating a Class
#     def testLogin(self, setup): # Method 1 - Passing as an arguement before execution
#         print("This is Login Test") # Passing as an arguement after execution
#     def testLogout(self, setup): # Method 2
#         print("This is Logout Test")
'''
Output is
Testing started at 18:47 ...
Launching pytest with arguments test_function_scope.py::TestClass --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day1

============================= test session starts ==============================
collecting ... collected 2 items

test_function_scope.py::TestClass::testLogin Launching Browser
PASSED                      [ 50%]This is Login Test

test_function_scope.py::TestClass::testLogout PASSED                     [100%]This is Logout Test
Closing Browser


============================== 2 passed in 0.02s ===============================

'''

# @pytest.fixture() # Class without scope
# def setup (): # Fixture Function
#     print("Launching Browser") # Having simple statement inside the function (prerequisite)
#     yield # Teardown
#     print("Closing Browser")
# class TestClass: # Creating a Class
#     def testLogin(self, setup): # Method 1 - Passing as an arguement before execution
#         print("This is Login Test") # Passing as an arguement after execution
#     def testLogout(self, setup): # Method 2
#         print("This is Logout Test")
'''
Output is
Testing started at 18:51 ...
Launching pytest with arguments test_function_scope.py::TestClass --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day1

============================= test session starts ==============================
collecting ... collected 2 items

test_function_scope.py::TestClass::testLogin Launching Browser
PASSED                      [ 50%]This is Login Test
Closing Browser

test_function_scope.py::TestClass::testLogout Launching Browser
PASSED                     [100%]This is Logout Test
Closing Browser


============================== 2 passed in 0.02s ===============================
'''

# # Module Scope
# @pytest.fixture(scope = 'module') # Class
# def setup (): # Fixture Function
#     print("Launching Browser")
#     yield # Teardown
#     print("Closing Browser")
#
# class TestClass: # Creating a Class
#     def testLogin(self, setup): # Method 1 - Passing as an arguement before execution
#         print("This is Login Test") # Passing as an arguement after execution
#     def testLogout(self, setup): # Method 2
#         print("This is Logout Test")
'''
Output is
Testing started at 18:58 ...
Launching pytest with arguments test_function_scope.py::TestClass --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day1

============================= test session starts ==============================
collecting ... collected 2 items

test_function_scope.py::TestClass::testLogin Launching Browser
PASSED                      [ 50%]This is Login Test

test_function_scope.py::TestClass::testLogout PASSED                     [100%]This is Logout Test
Closing Browser


============================== 2 passed in 0.02s ===============================

'''

# Session Scope
@pytest.fixture(scope = 'module') # Class
def setup (): # Fixture Function
    print("Launching Browser")
    yield # Teardown
    print("Closing Browser")

class TestClass: # Creating a Class
    def testLogin(self, setup): # Method 1 - Passing as an argument before execution
        print("This is Login Test") # Passing as an argument after execution
    def testLogout(self, setup): # Method 2
        print("This is Logout Test")