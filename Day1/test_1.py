import pytest # firstly, import pytest

# Creating a Class
# class TestClass: # Secondly, create a class
#     def testMethod1(self): # Thirdly, inside of the class create a Module (Method)
#         print("This is test Method1") # Fourthly, inside of module create a Test Case
#
#     def testMethod2(self): # 2nd Module (Method) created inside the same Class
#         print("This is test Method2")

'''
Output from the above 2 Test Cases
Testing started at 21:22 ...
Launching pytest with arguments test_1.py::TestClass --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day1

============================= test session starts ==============================
collecting ... collected 2 items

test_1.py::TestClass::testMethod1 PASSED                                 [ 50%]This is test Method1

test_1.py::TestClass::testMethod2 PASSED                                 [100%]This is test Method2


============================== 2 passed in 0.04s ===============================

The above percentage only displays 100% when all the Test Cases inside the Class have finished executing
'''

# Fixtures (Fixture is a decorator)
@pytest.fixture() # Calling fixture in pytest

def setup (): # Creating a function and with it self parameter isn't required and passing it as an arguement
    print("Launching Browser") # Having simple statement inside the function (prerequisite)
    yield # Teardown
    print("Closing Browser")



# Creating a Class and inside we will have 2 Methods
class TestClass:
    def testLogin(self,setup): # Method 1
        print("This is Login Test")
    def testLogout(self, setup): # Method 2
        print("This is Logout Test")

'''
Output when execute line 38
Testing started at 18:03 ...
Launching pytest with arguments test_1.py::TestClass --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day1

============================= test session starts ==============================
collecting ... collected 2 items

test_1.py::TestClass::testLogin PASSED                                   [ 50%]This is Login Test

test_1.py::TestClass::testLogout PASSED                                  [100%]This is Logout Test


============================== 2 passed in 0.02s ===============================

'''

'''
Output for line 39 after adding line 30 and "setup" to line 41 and 43
Testing started at 18:09 ...
Launching pytest with arguments test_1.py::TestClass::testLogin --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day1

============================= test session starts ==============================
collecting ... collected 1 item

test_1.py::TestClass::testLogin Launching Browser
PASSED                                   [100%]This is Login Test


============================== 1 passed in 0.02s ===============================

'''

'''
Output for line 39 after adding line 34 and line 35
Testing started at 18:15 ...
Launching pytest with arguments test_1.py::TestClass::testLogin --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day1

============================= test session starts ==============================
collecting ... collected 1 item

test_1.py::TestClass::testLogin Launching Browser
PASSED                                   [100%]This is Login Test
Closing Browser


============================== 1 passed in 0.02s ===============================

'''

'''
Output for line 43
Testing started at 18:16 ...
Launching pytest with arguments test_1.py::TestClass::testLogout --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day1

============================= test session starts ==============================
collecting ... collected 1 item

test_1.py::TestClass::testLogout Launching Browser
PASSED                                  [100%]This is Logout Test
Closing Browser


============================== 1 passed in 0.01s ===============================

'''