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
class CreateTests(unittest.TestCase):
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
    def test_createValueSet(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        self.dsp.goToValueSet()
        self.sd.pageRefresh()
        self.dsp.clearSearch()
        result_1 = self.dsp.verifyValueSettext()
        assert result_1 == value_set['ExpectedValueSettext']
        self.vs.clickOnNewValueSet()
        time.sleep(3)
        number = self.sd.randomNumber()
        self.vs.enterNewValueSetName(value_set['value_set_name']+number)
        time.sleep(5)
        self.vs.clickOnDropDown()
        time.sleep(2)
        self.vs.enterLabType(value_set['value_set_type'])
        time.sleep(3)
        self.vs.clickOnAddButton()
        time.sleep(4)
        self.vs.clickOnAddDefinition()
        time.sleep(3)
        self.vs.clickOnYearDD()
        time.sleep(3)
        self.vs.enterYear(value_set['Year'])
        time.sleep(5)
        self.vs.addNewDefinitionButton()
        time.sleep(4)
        self.vs.saveNewCreatedValueSet()
        time.sleep(4)
