'''
Pytest Framework-3
--------------------
Parametarisation (This is also a marker)
-----------------
- Parameterisation enables the Test Method to run multiple times with different data sets without the need for loops.
- Instead of writing looping statements, we can pass parameters to the test method, simplifying the process of repeating it
    with varying data.

@pytest.mark.parameterize() (its like a data driven testing and if the data is huge DDT is what to use)




Generating HTML Reports
-----------------------
pip install pytest-html

Hooks
-------
Customizing Test Metadata and Environment Information in Pytest HTML Reports
Hooks are functions provided by the pytest framework used to Add/Delete/Modify Environment info in the HTML Report - @pytest.mark.optionalhook


Commandline options
--------------------
parser.addoption('--browser')
request.config.getoption("--browser")

'''