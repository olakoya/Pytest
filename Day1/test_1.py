import pytest # firstly, import pytest

# Creating a Class
class TestClass: # Secondly, create a class
    def testMethod1(self): # Thirdly, inside of the class create a Module (Method)
        print("This is test Method1") # Fourthly, inside of module create a Test Case

    def testMethod2(self): # 2nd Module (Method) created inside the same Class
        print("This is test Method2")

'''
Output from the above 2 Test Cases
Testing started at 21:22 ...
Launching pytest with arguments test_1.py::TestClass --no-header --no-summary -q in /Users/olakoya/Desktop/Pytest/Day1

============================= test session starts ==============================
collecting ... collected 2 items

test_1.py::TestClass::testMethod1 PASSED                                 [ 50%]This is test Method1

test_1.py::TestClass::testMethod2 PASSED                                 [100%]This is test Method2


============================== 2 passed in 0.04s ===============================

The above percentage only displays 100% when all the Test Cases in the Class have finished executing
'''