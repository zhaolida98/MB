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
        tc_desc = "Verify that Search functionality should be present on the Agenda screen of the InNote"
        tc_status = "FAIL"
        tc_name = "Patient_Search_TC02"
        tc_priority = "Low"
        try:
            self.sd.createConnection()
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            self.dsp.clickMBLink()
            self.dsp.searchMeasure(measure_data['measurename'])
            time.sleep(2)
            self.mp.clicksearchMeasure()
            time.sleep(3)
            self.mp.clickDuplicateMeasureDetail()
            time.sleep(2)
            result = self.mp.verifyDuplicateText()
            assert result == True
            self.mp.clickCancelDuplicateMeasure()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority)













