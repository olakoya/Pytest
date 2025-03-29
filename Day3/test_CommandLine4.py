from selenium import webdriver

class Testsample:
    def test_sample(self, setup, browser):
        self.driver = setup
        self.driver.get("https://www.google.co.uk/")

        act_title = self.driver.title
        exp_title = "Google"

        print(f"Running tests on {browser}")
        assert act_title == exp_title, f"Expected {exp_title}, but got {act_title}"

        self.driver.quit()
# Passing Method from Commandline