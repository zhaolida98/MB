import time
import unittest

import allure
import pytest

from POM.Datashop.DataShopPage import DataShopPage
from POM.MeasurePage.MeasurePage import MeasurePage
from POM.home.login_page import LoginPage
from Utils.configreader import user_data, measure_data
from Utils.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SMCTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def TestclassSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.mp = MeasurePage(self.driver)
        self.dsp = DataShopPage(self.driver)
        self.ts = TestStatus(self.driver)

    @allure.testcase("Delete measure detail")
    @pytest.mark.flaky(reruns=1, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.skip
    def test_AcceptDelete(self):
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

    @allure.testcase("Cancel Delete measure detail")
    @pytest.mark.flaky(reruns=1, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cancelDelete(self):
        tc_desc = "Verify that user is able to cancel the delete measure button"
        tc_status = "FAIL"
        tc_name = "Cancel_delete_measure"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            self.dsp.clickMBLink()
            self.sd.pageRefresh()
            self.dsp.searchMeasure(measure_data['measurename'])
            self.mp.clicksearchMeasure()
            result_2 = self.mp.waitForDeleteButton()
            self.mp.clickDeleteMeasureDetail()
            result_1 = self.mp.verifyDeleteMText()
            assert result_1 == True
            self.mp.getDeleteMText()
            self.mp.cancelMeasureDeleteDetails()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)

    @allure.testcase("Close delete Measure Popup")
    @pytest.mark.flaky(reruns=1, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_closeDeletePopup(self):
        tc_desc = "Verify that user is able to close the delete measure popup"
        tc_status = "FAIL"
        tc_name = "Close_delete_measure_popup"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            self.dsp.clickMBLink()
            self.dsp.searchMeasure(measure_data['measurename'])
            self.mp.clicksearchMeasure()
            result_2 = self.mp.waitForDeleteButton()
            self.mp.clickDeleteMeasureDetail()
            result_1 = self.mp.verifyDeleteMText()
            assert result_1 == True
            self.mp.getDeleteMText()
            self.mp.closeRDuplicateMPopup()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)


