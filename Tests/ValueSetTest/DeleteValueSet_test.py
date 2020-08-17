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
class ValueSetTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def TestclassSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.mp = MeasurePage(self.driver)
        self.dsp = DataShopPage(self.driver)
        self.vs = ValuePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.sd = SeleniumDriver(self.driver)

    @allure.testcase("Delete Valueset")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=3)
    @pytest.mark.skip
    def test_deleteValueSet(self):
        start_time = time.time()
        tc_desc = "Delete with close popup  icon"
        tc_status = "FAIL"
        tc_name = "Delete_valueset_01"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            # self.lp.login(user_data['username'], user_data['password'])
            # result = self.lp.verifyLoginSuccessful()
            # self.ts.markFinal("test_validLogin", result, "Login was successful")
            # self.dsp.goToValueSet()
            self.dsp.clearSearch()
            self.sd.pageRefresh()
            result_1 = self.dsp.verifyValueSettext()
            assert result_1 == value_set['ExpectedValueSettext']
            result = self.vs.waitForSearchedValueSet()
            self.vs.searchAndClickValueSet(value_set['Edit_valueSetName'])
            time.sleep(3)
            result_2 = self.vs.verifyIndexText()
            assert result_2 == value_set['index_text']
            self.vs.deleteValueSet()
            self.vs.confirmDelete()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time, start_time)

    @allure.testcase("Cancel delete Valueset")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.skip
    @pytest.mark.run(order=1)
    def test_cancelDeleteValueSet(self):
        start_time = time.time()
        tc_desc = "Delete with cancel"
        tc_status = "FAIL"
        tc_name = "Delete_valueset_02"
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
            self.vs.searchAndClickValueSet(value_set['Edit_valueSetName'])
            time.sleep(3)
            result_2 = self.vs.verifyIndexText()
            assert result_2 == value_set['index_text']
            self.vs.deleteValueSet()
            self.vs.cancelDelete()
            result_3 = self.vs.verifyIndexText()
            assert result_3 == value_set['index_text']
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time, start_time)

    @allure.testcase("Close Delete popup")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.skip
    @pytest.mark.run(order=2)
    def test_closeDeleteValueSet(self):
        start_time = time.time()
        tc_desc = "Delete with close popup  icon"
        tc_status = "FAIL"
        tc_name = "Delete_valueset_03"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            # self.lp.login(user_data['username'], user_data['password'])
            # result = self.lp.verifyLoginSuccessful()
            # self.ts.markFinal("test_validLogin", result, "Login was successful")
            # self.dsp.goToValueSet()
            self.dsp.clearSearch()
            self.vs.pageRefresh()
            time.sleep(2)
            result_1 = self.dsp.verifyValueSettext()
            assert result_1 == value_set['ExpectedValueSettext']
            result = self.vs.waitForSearchedValueSet()
            self.vs.searchAndClickValueSet(value_set['Edit_valueSetName'])
            time.sleep(3)
            result_2 = self.vs.verifyIndexText()
            assert result_2 == value_set['index_text']
            self.vs.deleteValueSet()
            self.vs.closeDeletePopup()
            result_3 = self.vs.verifyIndexText()
            assert result_3 == value_set['index_text']
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time, start_time)

