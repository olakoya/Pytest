import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day4.pom_login import driver

# Mine is below this code but trying ChatGPT Code below
class TestTitle:

    def test_title_chrome(self, setup):
        assert "Google" in setup.title

    def test_title_firefox(self, setup):
        assert "Google" in setup.title

    def test_title_edge(self, setup):
        assert "Google" in setup.title

    def test_title_safari(self, setup):
        assert "Google" in setup.title

# My Code: It Works
# class TestTitle:
#     def test_title_chrome(self,setup):
#         driver = setup
#         driver.get("https://www.google.com/")
#         assert driver.title == "Google"
#
#     def test_title_edge(self, setup):
#         driver = setup
#         driver.get("https://www.google.com/")
#         assert driver.title == "Google"
#
#     def test_title_firefox(self,setup):
#         driver = setup
#         driver.get("https://www.google.com/")
#         assert driver.title == "Google"
#
#     def test_title_safari(self,setup):
#         driver = setup
#         driver.get("https://www.google.com/")
#         assert driver.title == "Google"