'''
Automation Framework - Introduction
-----------------------------------
Automation Framework
----------------------
It provides a systematic approach to writing, executing, and maintaining test scripts,
promoting reusability, scalability, and efficiency.
We organize automation project files and folders in structured manner.

Objectives
----------
Reusability
Scalability
Maintainability
Efficiency
Reporting

Types of Automation Frameworks
------------------------------
Built-in Frameworks
-------------------
Ready-to-use frameworks
TestNG,Junit,Pytest,Unittest,cucumber,Behave,etc


User-Defined/Customized Frameworks
----------------------------------
Customized frameworks meet specific project or organization requirements by
integrating tools and libraries.

Hybrid-Driven framework combine pom
Keyword-driven framework
Data Driven Approaches

Phases in Developing Automation Framework
------------------------------------------
1. Requirement Analysis: Identify testing needs, tools, and project requirements.
2. Tool Selection: Choose appropriate tools and libraries based on application type and
   project needs.
3. Framework Design: Decide on the structure, architecture, and approach (e.g., modular,
   hybrid, etc.).
4. Implementation: Develop reusable components, utilities, and test scripts.
5. Integration: Configure CI/CD pipelines for automated execution and reporting.
6. Testing: Validate the framework by executing sample test cases.
7. Maintenance: Continuously improve the framework to accommodate application
   changes.



configurations - directory
logs - dierctory
pageObjects - package
reports - directory
screenshorts - directory
testCases - package
testData - directory
utilities - package
requirements.txt

https://tutorialsninja.com/demo/

How to Select an Automation Testing Tool
------------------------------------------
1.Know your Requirements
	identify application type (Static,Dynamic,Responsive)
	understand technology stack (HTML,Angular,React)
	Ensure tool supports all target browsers and platforms
2.Check Tool Features
	Cross-browser compatability
	Ease of Integration
	Dynamic content handling
3.Evaluate usabilty
4.Consider costs
5.Test the Tool
6.Feature Readiness
7.Make a Decision



How to choose Test Cases for Automation
----------------------------------------
• High Priority Tests: Test cases for critical functionalities of the application.
• Repetitive Tests: Regression and smoke tests that are run frequently.
• Data-Driven Tests: Scenarios requiring multiple input combinations.
• Time-Consuming Tests: Tests that take significant time to execute manually.
• Stable Tests: Scenarios with a stable application feature.

Avoid Automation
----------------
• Exploratory or ad-hoc tests.
• Tests for features still under development.
• Low-priority or rarely used functionalities.

100% automation is not at all possible practically.

'''