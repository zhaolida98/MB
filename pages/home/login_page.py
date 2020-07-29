import logging
import time

import utilities.Custom_logger as cl
from base.basepage import BasePage
from utilities.configreader import login
from utilities.configreader import title


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _login_link = login['loginLink_xpath']
    _email_field = login['emailField_xpath']
    _password_field = login['passwordField_xpath']
    _submit_link =  login['loginButton_xpath']
    _successful_login = login['successfulLogin_xpath']
    _failed_login = login['failedLogin_xpath']

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    # Actions performed on the Element.

    def EnterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType='xpath')

    def EnterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._submit_link, locatorType="xpath")

    ### This is the functionality.

    def login(self, email="", password=""):
        self.clickLoginLink()
        time.sleep(2)
        self.EnterEmail(email)
        time.sleep(2)
        self.EnterPassword(password)
        self.clickLoginButton()
        time.sleep(2)
        self.verifyLoginSuccessful()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._successful_login, locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._failed_login, locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle(title['home_page_title'])

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()
