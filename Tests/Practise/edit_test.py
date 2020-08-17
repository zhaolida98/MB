import time
import unittest

import allure
import pytest

from POM.Datashop.DataShopPage import DataShopPage
from POM.MeasurePage.MeasurePage import MeasurePage
from POM.MeasurePage.ValueSetPage import ValuePage
from POM.home.login_page import LoginPage
from Utils.configreader import user_data, value_set
from Utils.teststatus import TestStatus
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
        self.sd = SeleniumDriver(self.driver)

    @allure.testcase("Click on cancel duplicate button")
    @allure.description("PTCS-T20013 (1.0)")
    @pytest.mark.flaky(reruns=0, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cancelDuplicateButton(self):
        tc_desc = "Edit the duplicate valueset with new name"
        tc_status = "FAIL"
        tc_name = "Edit_TC01"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            self.dsp.goToValueSet()
            result_1 = self.dsp.verifyValueSettext()
            assert result_1 == value_set['ExpectedValueSettext']
            result = self.vs.waitForSearchedValueSet()
            self.vs.enterValueSetName(value_set['valuesetname'])
            time.sleep(4)
            self.sd.duplicateClick()
            time.sleep(3)
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
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"

        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)
