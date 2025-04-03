from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
# Locators
    txtbox_username_name = 'username' # element is username and locator is name
    txtbox_password_name = 'password'
    btn_login_xpath = '//button'

# Constructor
    def __init__(self,driver): # driver is a parameter
        self.driver = driver # declaring instance variable

# Action Methods (declaring custom name)
    def setUserName(self,username): # Locating username txt box from Locators
        self.driver.find_element(By.NAME, self.txtbox_username_name).send_keys(username)
    def setPassWord(self,password):
        self.driver.find_element(By.NAME, self.txtbox_password_name).send_keys(password)
    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click

