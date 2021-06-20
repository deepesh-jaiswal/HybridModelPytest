from selenium import webdriver
import pytest
import time

from pageObects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestLogin:
    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_HomePage(self,setup):
        self.logger.info("************test_HomePage started****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title
        if act_title == "PHPTRAVELS | Travel Technology Partner":
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePage.png")
            self.logger.info(f"test passed as '{act_title}' equals to 'PHPTRAVELS | Travel Technology Partner'")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePage.png")
            self.logger.error(f"test failed as title as '{act_title}' not equals to 'PHPTRAVELS | Travel Technology Partner'")
            assert False
        self.driver.close()

    @pytest.mark.regression
    def test_LoginPage(self,setup):
        self.logger.info("************test_LoginPage started****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        lp = LoginPage(self.driver)
        lp.clickMyAccountLink()
        lp.clickLoginLink()
        act_title = self.driver.title
        if act_title == "Login":
            self.driver.save_screenshot(".\\Screenshots\\"+"test_LoginPage.png")
            self.logger.info(f"test passed as '{act_title}' equals to 'Login'")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_LoginPage.png")
            self.logger.error(f"test passed as '{act_title}' not equals to 'Login'")
            assert False
        self.driver.close()

    @pytest.mark.sanity
    def test_Login(self, setup):
        self.logger.info("************test_Login started****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        lp = LoginPage(self.driver)
        lp.clickMyAccountLink()
        lp.clickLoginLink()
        lp.enterUserName(self.userName)
        lp.enterPassword(self.password)
        lp.clickLoginButton()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "My Account":
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.logger.info(f"test passed as '{act_title}' equals to 'My Account'")
            lp.clickaccountNameLink()
            lp.clickLogoutLink()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.logger.error(f"test passed as '{act_title}' not equals to 'My Account'")
            print(f"test passed as '{act_title}' not equals to 'My Account'")
            assert False
        self.driver.close()