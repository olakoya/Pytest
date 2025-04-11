'''
Redefined codes by ChatGPT
'''
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

hub_url = "http://192.168.1.166:4444/wd/hub"

# Desired capabilities for Chrome
capabilities = DesiredCapabilities.CHROME.copy()

# Optional: Add Chrome options if needed
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Remote(
    command_executor=hub_url,
    options=options
)

driver.get("https://www.google.com/")
print(driver.title)
time.sleep(5)
driver.quit()

'''
Output after correction and using ChatGPT's code is
Google
'''
