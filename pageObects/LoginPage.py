from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    link_myAccount_xpath = "//div[@class='dropdown dropdown-login dropdown-tab']/a[@id='dropdownCurrency']"
    link_login_xpath = "//a[text()='Login']"
    textBox_userNameField_xpath = "//input[@name='username']"
    textBox_passwordField_xpath = "//input[@name='password']"
    button_login_xpath = "//button[text()='Login']"
    link_accountName_xpath = "//div[@class='dropdown dropdown-login dropdown-tab']/a[@id='dropdownCurrency']"
    link_logout_xpath = "//a[text()='Logout']"
    div_alertwrongcreds_xpath = "//div[@class='alert alert-danger']"
    link_signup_xpath = "//a[text()='Sign Up']"

    def __init__(self,driver):
        self.driver=driver

    def clickMyAccountLink(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.link_myAccount_xpath))).click()

    def clickLoginLink(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.link_login_xpath))).click()

    def enterUserName(self,username):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.textBox_userNameField_xpath))).clear()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.textBox_userNameField_xpath))).send_keys(username)

    def enterPassword(self,password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.textBox_passwordField_xpath))).clear()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.textBox_passwordField_xpath))).send_keys(password)

    def clickLoginButton(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))).click()

    def clickaccountNameLink(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.link_accountName_xpath))).click()

    def clickLogoutLink(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.link_logout_xpath))).click()

    def checkInvalidCreds(self,message):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.div_alertwrongcreds_xpath))).text == message

    def clickSignupLink(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.link_signup_xpath))).click()