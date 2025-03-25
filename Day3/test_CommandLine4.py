from selenium import webdriver

class Testsample:
    def test_sample(self, setup):
        self.driver = setup
        self.driver.get("https://www.google.co.uk/")
        act_title = self.driver.title
        exp_title = "Google"