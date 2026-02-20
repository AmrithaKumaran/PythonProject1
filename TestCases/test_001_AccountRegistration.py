"""from PageObject.HomePage import HomePage
from PageObject.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomstring


class Test_001_AccountReg:
    baseURL = "https://www.opencart.com/"

    def test_account_reg(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.regpage=AccountRegistrationPage(self.driver)

        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
	self.email=randomstring.random_string_generator()+'@gmail.com'
        self.regpage.setEmail(self.email)
        self.regpage.setTelephone("65656565")
        self.regpage.setPassword("abcxyz")
        self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg=self.regpage.getconfirmationmsg()
        self.driver.close()

        if self.confmsg=="Your Account Has Been Created!":
            assert True
        else:
            assert False"""

from PageObject.HomePage import HomePage
from PageObject.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomstring
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest


class TestAccountRegistration:
    baseURL = ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_account_reg(self, setup):
        self.logger.info("test_001_AccountRegistration_test_Case")
        self.driver = setup
        self.logger.debug("WebDriver instance assigned")
        self.driver.get(self.baseURL)
        self.logger.info(f"Application launched with URL: {self.baseURL}")
        self.hp = HomePage(self.driver)
        self.logger.debug("HomePage object created")
        self.hp.clickMyAccount()
        self.logger.info("Clicked on My Account link")
        self.hp.clickRegister()
        self.logger.info("Clicked on Register page")
        self.regpage = AccountRegistrationPage(self.driver)
        self.logger.debug("AccountRegistrationPage object created")
        #self.regpage.setUsername("johncanedyhb")
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")

        self.email = randomstring.random_string_generator() + "@gmail.com"
        self.regpage.setEmail(self.email)

        self.regpage.setTelephone("65656565")
        self.regpage.setPassword("abcxyz")
        self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()
        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("Account Registration is passed")
            assert True
            self.driver.close()
        else:
            self.logger.warning("Expected confirmation message did not match")
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\Screenshots\\"+"test_account_reg.png") # will give project directory
            #first give project directory and then give the screenshot folder name+ name of the method for which screenshot is taken.
            self.logger.error("Account Registration Failed")
            self.driver.close()
            assert False

        #assert self.confmsg == "Your Account Has Been Created!"









