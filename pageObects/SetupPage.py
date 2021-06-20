import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SetupPage:
    textBox_firstName_xpath = "//input[@name='firstname']"
    textBox_lastName_xpath = "//input[@name='lastname']"
    textBox_mobile_xpath = "//input[@name='phone']"
    textBox_email_xpath = "//input[@name='email']"
    textBox_password_xpath = "//input[@name='password']"
    textBox_confirmPassword_xpath = "//input[@name='confirmpassword']"
    button_signUp_xpath = "//button[@class='signupbtn btn_full btn btn-success btn-block btn-lg']"

    def __init__(self,driver):
        self.driver = driver

    def enterFirstName(self,firstname):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.textBox_firstName_xpath))).send_keys(firstname)

    def enterLastName(self,lastname):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.textBox_lastName_xpath))).send_keys(lastname)

    def enterMobile(self,mobile):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.textBox_mobile_xpath))).send_keys(mobile)

    def enterEmail(self,email):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.textBox_email_xpath))).send_keys(email)

    def enterPassword(self,password):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.textBox_password_xpath))).send_keys(password)

    def enterConfirmPassword(self,password):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.textBox_confirmPassword_xpath))).send_keys(password)

    def clickSignUpButton(self):
        #self.driver.execute_script("arguments[0].scrollIntoView(true);",self.button_signUp_xpath)
        button = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.button_signUp_xpath)))
        self.driver.execute_script("arguments[0].click()",button)

    def random_emailGenerator(length = 8,chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(length))