"""from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage():

    #lnk_myaccount_xpath = "//a[@title='My Account']"
    lnk_register_linktext = "Register"
    lnk_login_linktext = "Login"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    #def clickMyAccount(self):
     #   self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath).click()

    def clickRegister(self):
        self.wait.until(EC.element_to_be_clickable(self.lnk_register_linktext)).click()
        self.driver.find_element(By.LINK_TEXT,self.lnk_register_linktext).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    lnk_myaccount = (By.LINK_TEXT, "My Account")
    lnkRegister = (By.LINK_TEXT, "Register")
    lnkLogin = (By.LINK_TEXT, "Login")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def clickMyAccount(self):
        self.wait.until(EC.element_to_be_clickable(self.lnk_myaccount)).click()

    def clickRegister(self):
        self.wait.until(EC.element_to_be_clickable(self.lnkRegister)).click()

    def clickLogin(self):
        self.wait.until(EC.element_to_be_clickable(self.lnkLogin)).click()
