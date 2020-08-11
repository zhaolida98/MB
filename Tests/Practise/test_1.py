import time
import unittest

import allure
import pytest

from POM.Datashop.DataShopPage import DataShopPage
from POM.MeasurePage.MeasurePage import MeasurePage
from POM.MeasurePage.ValueSetPage import ValuePage
from POM.home.login_page import LoginPage
from Utils.configreader import user_data, measure_data, value_set
from Utils.teststatus import TestStatus
from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SMCTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def TestclassSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.mp = MeasurePage(self.driver)
        self.dsp = DataShopPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.vs = ValuePage(self.driver)
        self.bp = BasePage(self.driver)
        self.sd = SeleniumDriver(self.driver)

    @allure.testcase("Create duplicate valuesetDetail")
    @pytest.mark.flaky(reruns=0, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_createDuplicate(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        self.dsp.goToValueSet()
        result_1 = self.dsp.verifyValueSettext()
        assert result_1 == value_set['ExpectedValueSettext']
        result = self.vs.waitForSearchedValueSet()
        self.vs.enterValueSetName(value_set['valuesetname'])
        time.sleep(4)
        #cc=self.vs.clickSearchedFValueSet()
        dd = self.sd.duplicateClick()
        result_2 = self.vs.verifyIndexText()
        assert result_2 == value_set['index_text']
        time.sleep(2)
        self.vs.clickDuplicateDetail()
        time.sleep(2)
        result_3 = self.vs.verifyDuplicateDetailButtonText()
        assert result_3 == value_set['Duplicate_Button_Text']
        self.vs.clickDuplicateDetailButton()
        time.sleep(5)
        self.sd.screenShot(resultMessage="Screenshot Captured")

