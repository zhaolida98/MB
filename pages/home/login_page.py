import logging
import time

import allure
from allure_commons.types import AttachmentType

import utilities.Custom_logger as cl
from base.basepage import BasePage
from utilities.configreader import title


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _login_link = "//body//div[@class='login-wrapper login-wrapper-modal']//div[@class='login-wrapper " \
                  "login-wrapper-modal']//div[1]//div[2]"
    _email_field = "//form[@id='datashop-login-form']//input[@name='email']"
    _password_field = "//form[@id='datashop-login-form']//input[@name='password']"
    _submit_link = "//form[@id='datashop-login-form']//button[contains(text(),'Sign in to continue')]"
    _successful_login = "//p[@class='email']"
    _failed_login = "//div[@class='login-error-alert alert callout']"

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
