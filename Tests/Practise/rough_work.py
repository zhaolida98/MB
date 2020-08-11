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

    @allure.testcase("Edit Valueset with cancel")
    @pytest.mark.flaky(reruns=0, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.skip
    def test_CancelValueSet(self):
        tc_desc = "Save Changes"
        tc_status = "FAIL"
        tc_name = "Edit_TC08"
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
            time.sleep(2)
            self.vs.editButton()
            time.sleep(10)
            self.vs.verifyEnableSaveButton()
            self.vs.clickSaveButton()
            self.vs.verifyEnableSaveButton()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)

    def test_cancelWithSaveAndClose(self):
        tc_desc = "Delete with close popup  icon"
        tc_status = "FAIL"
        tc_name = "Delete_valueset_01"
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
            self.vs.confirmDelete()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)