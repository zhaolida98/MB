import logging
import time
import unittest

import allure
import pytest

from POM.Datashop.DataShopPage import DataShopPage
from POM.MeasurePage.ValueSetPage import ValuePage
from POM.home.login_page import LoginPage
from Utils.configreader import user_data, value_set
from Utils.teststatus import TestStatus
import Utils.Custom_logger as cl
from base.selenium_driver import SeleniumDriver


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.vs = ValuePage(self.driver)
        self.dsp = DataShopPage(self.driver)
        self.sd = SeleniumDriver(self.driver)

    @allure.testcase("Search Valueset")
    @pytest.mark.flaky(reruns=0, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_clickSearchedValueSet(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        self.dsp.goToValueSet()
        self.dsp.clearSearch()
        self.sd.pageRefresh()
        result_1 = self.dsp.verifyValueSettext()
        assert result_1 == value_set['ExpectedValueSettext']
        result = self.vs.waitForSearchedValueSet()
        self.vs.searchAndClickValueSet(value_set['Edit_valueSetName'])
        time.sleep(3)
        result_2 = self.vs.verifyIndexText()
        assert result_2 == value_set['index_text']
        time.sleep(2)
        self.vs.editButton()
        time.sleep(2)
        self.vs.cancelButton()
        time.sleep(4)
        self.vs.closeEditCancelPopup()
        result_3 = self.vs.verifyIndexText()
        assert result_3 == value_set['index_text']

