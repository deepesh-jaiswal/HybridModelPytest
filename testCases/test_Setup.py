from selenium import webdriver
import pytest
import time

from pageObects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObects.SetupPage import SetupPage


class TestSetup:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_Setup(self,setup):
        self.logger.info("************test_Setup started****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        lp = LoginPage(self.driver)
        lp.clickMyAccountLink()
        lp.clickSignupLink()
        sp = SetupPage(self.driver)
        sp.enterFirstName("Deepesh")
        sp.enterLastName("Kumar")
        sp.enterMobile("9876543210")
        sp.random_emailGenerator()
        sp.enterEmail("abc123@gmail.com")
        sp.enterPassword("abc@123")
        sp.enterConfirmPassword("abc@123")
        sp.clickSignUpButton()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "My Account":
            self.driver.save_screenshot(".\\Screenshots\\"+"test_Setup.png")
            self.logger.info(f"test passed as '{act_title}' equals to 'My Account'")
            lp.clickaccountNameLink()
            lp.clickLogoutLink()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_Setup.png")
            self.logger.error(f"test passed as '{act_title}' not equals to 'My Account'")
            assert False
        self.driver.close()