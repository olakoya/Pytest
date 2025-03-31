'''
Page Object Model Pattern
-------------------------
Different types of Names for this Modern are:
    1. Page Object Model or 2. Page Object Repository or 3. Page Object Factory
- POM is not a framework
- POM talks about how we can manage/maintain the page objects/elements for multiple Test Cases.
E.g

Web Application
----------------
Inside of this application we have 3 different pages in hierarchy;

1. ==> Login
2. ==> Search
3. ==> Advanced Search

A. Then first we need to automate;
- Automate login Functionality

B. Secondly we need to automate;
- Automate Search functionality, we need to write;
	i. Login functionality automation script
	ii. write script for search functionality

 C. Thirdly we need to automate;
- Automate Advanced Search functionality
	i. Login functionality automation script
	ii. write script for search functionality
	iii. write script for Advanced search functionality


Problems without POM
---------------------
Duplication
Updation/Maintainance

With Page Object Model Approach
-------------------------------
In the Page object model pattern for every page in application we will create a separate class called Page object classes.
Page object class contains the elements belonging to a specific page along with action methods.
so no need to write page elements only specify test methods.test methods talk to the class and get the elements and will perform the action.

Note
----
when we enter into a project first task is to create a page object class by analysing all test cases,no of pages

class ==> constructors + methods(Actions)

page object class should contain
	Locators
	constructor
	action methods

No of Locators = No of action methods


Thumb rules :
------------
In the Page object class should have elements belonging to one single page every time i.e, one page object class should always represent only one single page.
Page Object class we should not hard code any data .The data should pass through test case
We should not include any validations and assertions in the page object class


'''