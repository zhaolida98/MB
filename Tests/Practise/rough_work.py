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

    @allure.testcase("Edit Valueset with save")
    @pytest.mark.flaky(reruns=0, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=1)
    def test_EditValueSet(self):
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
            self.sd.pageRefresh()
            result_1 = self.dsp.verifyValueSettext()
            assert result_1 == value_set['ExpectedValueSettext']
            result = self.vs.waitForSearchedValueSet()
            self.vs.searchAndClickValueSet(value_set['Edit_valueSetName'])
            time.sleep(3)
            result_2 = self.vs.verifyIndexText()
            assert result_2 == value_set['index_text']
            time.sleep(2)
            self.vs.clickEditValueSetDetail()
            time.sleep(2)
            self.vs.clearValueSetName()
            time.sleep(2)
            self.vs.entereditvaluesetName(value_set['editValueSetName'])
            time.sleep(2)
            self.vs.saveValueSetName()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)
