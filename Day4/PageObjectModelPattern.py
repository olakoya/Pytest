'''
Page Object Model Pattern
-------------------------
Different types of Names for this Modern are:
    1. Page Object Model or 2. Page Object Repository or 3. Page Object Factory
- POM is not a framework but a place where we create reuse able objects
- POM talks about how we can manage/maintain the page objects/elements for multiple Test Cases.
E.g

Web Application
----------------
Inside of this application we have 3 different pages in hierarchy;

1. ==> Login Page
2. ==> Search Page
3. ==> Advanced Search Page

A. Then first we need to automate;
- Automate login Functionality
--------------------------------

B. Secondly we need to automate;
- Automate Search functionality, we need to write;
--------------------------------------------------
	i. Login functionality automation script
	ii. write script for search functionality

 C. Thirdly we need to automate;
- Automate Advanced Search functionality
------------------------------------------------
	i. Login functionality automation script
	ii. write script for search functionality
	iii. write script for Advanced search functionality


Problems without POM (Page Object Model)
-----------------------------------------
1. Duplication is an issue
2. Updating/ Maintenance

With Page Object Model Approach
-------------------------------
1. In the Page object model pattern for every page in application we will create a separate class called Page object classes.
2. Every Page object class contains the elements belonging to a specific page along with action methods.
3. So no need to write page elements only specify test methods.test methods talk to the class and get the elements and will
perform the action.

Note
----
When we enter into a project, first task is to create a page object class by analysing all test cases and nos of pages (lots of functionalities)

class ==> constructors + methods(Actions)

Page Object Class should contain;
-----------------------------------
	1. Locators => Locating element and afterwards perform action
	2. Constructor => Used for initialising an instant variable
	3. Action methods

==> No of Locators = No of action methods


Thumb rules :
------------
1. In the Page object class should have elements belonging to one single page every time i.e, one page object class should
always represent only one single page.
2. Page Object class we should not hard code any data .The data should pass through test case
We should not include any validations and assertions in the page object class


'''