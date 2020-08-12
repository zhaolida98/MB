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
class NewTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def TestclassSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.mp = MeasurePage(self.driver)
        self.dsp = DataShopPage(self.driver)
        self.ts = TestStatus(self.driver)

    def test_cancelNewMeasure(self):
        tc_desc = "Verify that user is able to click on cancel button of new measure modal"
        tc_status = "FAIL"
        tc_name = "Cancel_New_Measure_creation"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            self.dsp.clickMBLink()
            self.mp.newMeasure()
            result_1 = self.mp.verifyAddNewMeasureText()
            assert result_1 == True
            self.mp.cancelMeasureModal()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)

    @allure.testcase("Validate measure count of all measures")
    @allure.description("")
    @pytest.mark.flaky(reruns=0, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_countAllMeasure(self):
        tc_desc = "Verify that user is able to get the count of all available measure"
        tc_status = "FAIL"
        tc_name = "Measure_Count"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            self.dsp.clickMBLink()
            result_2 = self.dsp.waitForMBLink()
            self.dsp.measureCount()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)

    @allure.testcase("Validate measure count with valid measure")
    @allure.description("")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_countValidMeasure(self):
        tc_desc = "Verify that user is able to get the count of entered measure"
        tc_status = "FAIL"
        tc_name = "Measure_Count of user selection"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            self.dsp.clickMBLink()
            result_2 = self.dsp.waitForMBLink()
            self.dsp.searchMeasure(measure_data['measurename'])
            self.dsp.measureCount()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)


    @allure.testcase("Validate measure count with invalid measure")
    @allure.description("")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_countNoMeasure(self):
        tc_desc = "Verify that user is able to get the count as Zero of incorrect measure"
        tc_status = "FAIL"
        tc_name = "Measure_Count of incorrect measure"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            self.dsp.clickMBLink()
            result_2 = self.dsp.waitForMBLink()
            self.dsp.searchMeasure(measure_data['wrong_measure_name'])
            self.dsp.measureCount()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)



