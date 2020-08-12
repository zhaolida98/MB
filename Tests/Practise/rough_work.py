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
    pytestmark = pytest.mark.random_order(disabled=True)

    @pytest.fixture(autouse=True)
    def TestclassSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.mp = MeasurePage(self.driver)
        self.dsp = DataShopPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.vs = ValuePage(self.driver)
        self.bp = BasePage(self.driver)
        self.sd = SeleniumDriver(self.driver)

    @allure.testcase("Click on cancel new measure modal")
    @allure.description("PTCS-T20193 (1.0)")
    @pytest.mark.flaky(reruns=0, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_countAllMeasure(self):
        tc_desc = "Verify that user is able to delete the measure of his choice"
        tc_status = "FAIL"
        tc_name = "Delete_measure"
        tc_priority = "Medium"
        tc_time = self.sd.getTime()
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            self.dsp.clickMBLink()
            self.sd.pageRefresh()
            self.dsp.searchMeasure(measure_data['measurename'])
            self.mp.deleteMeasure()
            result_2 = self.mp.waitForDeleteButton()
            self.mp.clickDeleteMeasureDetail()
            result_1 = self.mp.verifyDeleteMText()
            assert result_1 == True
            self.mp.getDeleteMText()
            self.mp.deleteMeasureDetail()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)

