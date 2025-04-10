from Day4.pom_login import driver


class TestTitle:
    def test_title_chrome(self,setup):
        driver = setup
        driver.get("https://www.google.com/")
        assert driver.title == "Google"

    def test_title_edge(self, setup):
        driver = setup
        driver.get("https://www.google.com/")
        assert driver.title == "Google"

    def test_title_firefox(self,setup):
        driver = setup
        driver.get("https://www.google.com/")
        assert driver.title == "Google"

    def test_title_safari(self,setup):
        driver = setup
        driver.get("https://www.google.com/")
        assert driver.title == "Google"