import logging
import time
import unittest

import allure
import pytest

import Utils.Custom_logger as cl
from POM.home.login_page import LoginPage
from Utils.configreader import user_data
from Utils.teststatus import TestStatus
from base.selenium_driver import SeleniumDriver


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.sd = SeleniumDriver(self.driver)

    @allure.testcase("Login with valid set of credentials")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("PTCS-T41056 (1.0)")
    @pytest.mark.run(order=2)
    @pytest.mark.skip
    def test_validLogin(self):
        start_time = time.time()
        tc_desc = "Verify the Newly Created user is able to log in the Application Sucessfully"
        tc_status = "FAIL"
        tc_name = "Login_TC01"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            #self.lp.clickLoginLink()
            self.lp.login(user_data['username'], user_data['password'])
            time.sleep(5)
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time, start_time)


    @allure.testcase("Login with invalid set of credentials")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.MINOR)
    @allure.description("PTCS-T41064 (1.0)")
    #@pytest.mark.skip
    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        start_time = time.time()
        tc_desc = "Verify user account is locked if Wrong password in entered for Six times"
        tc_status = "FAIL"
        tc_name = "Login_TC02"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            self.lp.clickLoginLink()
            self.lp.EnterEmail(user_data['username'])
            self.lp.EnterPassword(user_data['invalid_password'])
            self.lp.clickLoginButton()
            time.sleep(5)
            result = self.lp.verifyLoginFailed()
            assert result == True
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority,tc_time, start_time)
