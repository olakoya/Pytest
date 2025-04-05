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
1. pip install pytest-html
    - After installing the above
2. To generate reports needed, code to use is below;
==> pytest -s -v --html=Day3\report.html Day3/test_Parameterization3-2.py
3. After execution, report can be displayed in a plain browser by
    - Right clicking on the automatic created html file report in the folder
    - Click on Open in
    - Browser (select one)
    - Safari or Chrome or Firefox or Edge ( I selected Safari for this report)
    - Reports generated onto selected browser, Safari

After generating the report, user decided to edit and delete some unnecessary info on the report, software to use is below;

Hooks
-------
Customizing Test Metadata and Environment Information in Pytest HTML Reports
Hooks are functions provided by the pytest framework used to Add/Delete/Modify Environment info in the HTML Report
==> @pytest.mark.optionalhook


Commandline options
--------------------
- parser.addoption('--browser') (describing method and using option '--browser' dynamically by specifying)

- request.config.getoption("--browser") (this is capturing the value and passing it to fixture function)

'''