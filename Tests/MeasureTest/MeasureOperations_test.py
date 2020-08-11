import time
import unittest

import allure
import pytest

from POM.Datashop.DataShopPage import DataShopPage
from POM.MeasurePage.MeasurePage import MeasurePage
from POM.home.login_page import LoginPage
from Utils.configreader import user_data, measure_data
from base.selenium_driver import SeleniumDriver


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SMCTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def TestclassSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.mp = MeasurePage(self.driver)
        self.dsp = DataShopPage(self.driver)
        self.sd = SeleniumDriver(self.driver)


    @allure.testcase("Click on searched measure detail as per the search criteria")
    @allure.description("PTCS-T20011 (1.0)")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_clickSearchedMessage(self):
        tc_desc = "Validate user is able to search the desired measure using measure name"
        tc_status = "FAIL"
        tc_name = "SearchMeasure_TC01"
        tc_priority = "Medium"
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            assert result == True
            self.dsp.clickMBLink()
            self.dsp.searchMeasure(measure_data['measurename'])
            time.sleep(2)
            self.mp.clicksearchMeasure()
            time.sleep(2)
            result = self.mp.verifyMeasureCategory()
            assert result == True
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority)

    @allure.testcase("Search non existed measure")
    @allure.description("PTCS-T20202 (1.0)")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_noMeasureMessage(self):
        tc_desc = "Validate that if an invalid name is used for the search than no results should be shown"
        tc_status = "FAIL"
        tc_name = "SearchMeasure_TC02"
        tc_priority = "Medium"
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            assert result == True
            self.dsp.clickMBLink()
            time.sleep(2)
            self.dsp.searchMeasure(measure_data['wrong_measure_name'])
            time.sleep(2)
            self.mp.clicksearchMeasure()
            self.dsp.getNoMeasureText()
            time.sleep(3)
            result = self.dsp.verifyMeasureText()
            assert result == True
            assert result == True
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority)

    @allure.testcase("Click on Edit measure detail as per the search criteria")
    @allure.description("PTCS-T20018 (1.0)")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_editSearchedMessage(self):
        tc_desc = "Validate user is able to update the measure details and definition successfully(Please refer the " \
                  "test data for desired measure name)"
        tc_status = "FAIL"
        tc_name = "EditMeasure_TC03"
        tc_priority = "Medium"
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            assert result == True
            self.dsp.clickMBLink()
            self.dsp.searchMeasure(measure_data['measurename'])
            time.sleep(2)
            self.mp.clicksearchMeasure()
            time.sleep(2)
            self.mp.clickEditMeasureOverview()
            time.sleep(2)
            self.mp.measureNameClearFields()
            self.mp.measureTypeClearFields()
            time.sleep(2)
            result = self.mp.verifyEditMeasureText()
            assert result == True
            self.mp.enterName(measure_data['editMeasureName'])
            time.sleep(2)
            self.mp.enterType(measure_data['editMeasureType'])
            self.mp.clickSaveEditMeasureOverview()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority)

    @allure.testcase("Verify edit measure text Fields")
    @allure.description("PTCS-T20194 (1.0)")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_editMeasureTextFields(self):
        tc_desc = "Validate that following fields are shown in the Edit Measure modal"
        tc_status = "FAIL"
        tc_name = "EditMeasure_TC04"
        tc_priority = "Medium"
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            assert result == True
            self.dsp.clickMBLink()
            self.dsp.searchMeasure(measure_data['measurename'])
            time.sleep(2)
            self.mp.clicksearchMeasure()
            time.sleep(2)
            self.mp.clickEditMeasureOverview()
            result = self.mp.verifymName()
            assert result == True
            result_1 = self.mp.verifymProgram()
            assert result_1 == True
            result_2 = self.mp.verifymProductLine()
            assert result_2 == True
            result_3 = self.mp.verifyPoorMeasureText()
            assert result_3 == True
            time.sleep(2)
            self.mp.verifyEditMeasureText()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority)

    @allure.testcase("Click on cancel duplicate button")
    @allure.description("PTCS-T20013 (1.0)")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cancelDuplicateButton(self):
        tc_desc = "Validate that click on cancel should close the popup window"
        tc_status = "FAIL"
        tc_name = "DuplicateMeasure_TC05"
        tc_priority = "Medium"
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            assert result == True
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


    @allure.testcase("Duplicate measure after clicking on Right side of duplicate Button")
    @allure.description("PTCS-T20011 (1.0)")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_DuplicateMeasure(self):
        tc_desc = "Validate that user is able to duplicate the measure along with all details(Please refer the test data for desired measure name)"
        tc_status = "FAIL"
        tc_name = "DuplicateMeasure_TC06"
        tc_priority = "Medium"
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            assert result == True
            self.dsp.clickMBLink()
            self.dsp.searchMeasure(measure_data['measurename'])
            self.mp.clicksearchMeasure()
            result = self.mp.verifyMeasureCategory()
            assert result == True
            self.mp.clickRDuplicateButton()
            result_1 = self.mp.verifyDuplicateText()
            assert result_1 == True
            self.mp.clickRContinueDuplicateM()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority)

    @allure.testcase("Cancel Duplicate measure after clicking on Right side of duplicate Button")
    @allure.description("PTCS-T20011 (1.0)")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_CancelDuplicateMeasure(self):
        tc_desc = "Validate that click on right side duplicate button should close the popup window"
        tc_status = "FAIL"
        tc_name = "DuplicateMeasure_TC07"
        tc_priority = "Medium"
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            assert result == True
            self.dsp.clickMBLink()
            self.dsp.searchMeasure(measure_data['measurename'])
            self.mp.clicksearchMeasure()
            result = self.mp.verifyMeasureCategory()
            assert result == True
            self.mp.clickRDuplicateButton()
            result_1 = self.mp.verifyDuplicateText()
            assert result_1 == True
            self.mp.cancelRDuplicateM()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority)

    @allure.testcase("Close Duplicate Measure Popup")
    @allure.description("PTCS-T20011 (1.0)")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_closeDuplicateMeasure(self):
        tc_desc = "Validate that click on close icon should close the popup window"
        tc_status = "FAIL"
        tc_name = "DuplicateMeasure_TC08"
        tc_priority = "Medium"
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            assert result == True
            self.dsp.clickMBLink()
            self.dsp.searchMeasure(measure_data['measurename'])
            self.mp.clicksearchMeasure()
            result = self.mp.verifyMeasureCategory()
            assert result == True
            self.mp.clickRDuplicateButton()
            result_1 = self.mp.verifyDuplicateText()
            assert result_1 == True
            self.mp.closeRDuplicateMPopup()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority)


