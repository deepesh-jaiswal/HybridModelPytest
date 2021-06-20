from selenium import webdriver
import pytest
import time

from pageObects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtilityFile


class TestLoginDDP:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    dataFilePath = ".//Testdata//DDP.xlsx"

    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("************test_Login started****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        lp = LoginPage(self.driver)
        lp.clickMyAccountLink()
        lp.clickLoginLink()
        loginDetails = ExcelUtilityFile.createDataDictionary(self.dataFilePath,"Sheet1")
        result = []
        for row in range(ExcelUtilityFile.getRowCount(self.dataFilePath,"Sheet1")-1):
            lp.enterUserName(loginDetails["UserName"][row])
            lp.enterPassword(loginDetails["Password"][row])
            lp.clickLoginButton()
            time.sleep(5)
            act_title = self.driver.title
            if act_title == "My Account":
                self.logger.info(f"test passed as '{act_title}' equals to 'My Account'")
                if loginDetails["Status"][row] == "Pass":
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_Login"+str(row)+".png")
                    lp.clickaccountNameLink()
                    lp.clickLogoutLink()
                    result.append("Pass")
                elif loginDetails["Status"][row] == "Fail":
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_Login"+str(row)+".png")
                    lp.clickaccountNameLink()
                    lp.clickLogoutLink()
                    result.append("Fail")
            elif act_title != "My Account":
                self.logger.info(f"test passed as '{act_title}' equals to 'My Account'")
                if loginDetails["Status"][row] == "Pass":
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_Login"+str(row)+".png")
                    result.append("Fail")
                elif loginDetails["Status"][row] == "Fail":
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_Login"+str(row)+".png")
                    if lp.checkInvalidCreds("Invalid Email or Password"):
                        result.append("Pass")

        if "Fail" in result:
            self.logger.info("************test_Login Failed****************")
            assert False
        else:
            self.logger.info("************test_Login Passed****************")
            assert True
        self.driver.close()