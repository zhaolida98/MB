import logging
import time
import unittest

import allure
import pytest

from pages.home.login_page import LoginPage
from utilities.configreader import user_data
from utilities.teststatus import TestStatus
import utilities.Custom_logger as cl


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @allure.testcase("Login with valid set of credentials")
    @pytest.mark.flaky(reruns=0, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_validLogin(self):
        self.lp.login(user_data['username'], user_data['password'])
        time.sleep(5)
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")

    @allure.testcase("Login with invalid set of credentials")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.skip
    def test_invalidLogin(self):
        self.lp.login(user_data['username'], user_data['invalid_password'])
        time.sleep(5)
        result = self.lp.verifyLoginFailed()
        assert result == True
