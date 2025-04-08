import time
from selenium import webdriver

hub_url = "http://192.168.1.166:4444/wd/hub"

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)

opt.platform_name = "MacBook Pro"
opt.browser_version = "chrome"

driver = webdriver.Remote(command_executor=hub_url, options=opt)

driver.get("https://www.google.com/")
print(driver.title)
time.sleep(5)
driver.close()

'''
Output from the teacher's code is
Error
'''