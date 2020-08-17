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

    @allure.testcase("Search Valueset")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_clickSearchedValueSet(self):
        start_time = time.time()
        tc_desc = "Verify that user is able to search the valueset"
        tc_status = "FAIL"
        tc_name = "Search_Duplicate_Valueset_TC01"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            self.dsp.goToValueSet()
            self.vs.pageRefresh()
            result_1 = self.dsp.verifyValueSettext()
            assert result_1 == value_set['ExpectedValueSettext']
            result = self.vs.waitForSearchedValueSet()
            self.vs.enterValueSetName(value_set['valuesetname'])
            time.sleep(2)
            self.vs.clickSearchedFValueSet()
            time.sleep(3)
            result_2 = self.vs.verifyIndexText()
            assert result_2 == value_set['index_text']
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time, start_time)

    @allure.testcase("Create duplicate valuesetDetail")
    @pytest.mark.flaky(reruns=0, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_createDuplicate(self):
        start_time = time.time()
        tc_desc = "Verify that user is able to create a duplicate valueset of same type"
        tc_status = "FAIL"
        tc_name = "Create_Duplicate_Valueset_TC01"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            self.dsp.goToValueSet()
            self.vs.pageRefresh()
            result_1 = self.dsp.verifyValueSettext()
            assert result_1 == value_set['ExpectedValueSettext']
            result = self.vs.waitForSearchedValueSet()
            self.vs.enterValueSetName(value_set['valuesetname'])
            time.sleep(4)
            self.vs.clickSearchedFValueSet()
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
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time, start_time)


    @allure.testcase("Cancel duplicate valuesetDetail")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cancelDuplicate(self):
        start_time = time.time()
        tc_desc = "Verify that user is able to cancel the button on duplicate valueset popup"
        tc_status = "FAIL"
        tc_name = "Cancel_Duplicate_Valueset_TC01"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            self.dsp.goToValueSet()
            self.vs.pageRefresh()
            result_1 = self.dsp.verifyValueSettext()
            assert result_1 == value_set['ExpectedValueSettext']
            result = self.vs.waitForSearchedValueSet()
            self.vs.enterValueSetName(value_set['valuesetname'])
            time.sleep(2)
            self.vs.clickSearchedFValueSet()
            result_2 = self.vs.verifyIndexText()
            assert result_2 == value_set['index_text']
            time.sleep(2)
            self.vs.clickDuplicateDetail()
            time.sleep(2)
            result_3 = self.vs.verifyDuplicateDetailButtonText()
            assert result_3 == value_set['Duplicate_Button_Text']
            self.vs.cancelDuplicateDetail()
            self.sd.screenShot(resultMessage="Screenshot Captured")
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time, start_time)


    @allure.testcase("close duplicate valuesetDetail")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_closeDuplicate(self):
        start_time = time.time()
        tc_desc = "Verify that user is able to close the duplicate valueset popup"
        tc_status = "FAIL"
        tc_name = "Close_Duplicate_Valueset_TC02"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            self.dsp.goToValueSet()
            self.vs.pageRefresh()
            result_1 = self.dsp.verifyValueSettext()
            assert result_1 == value_set['ExpectedValueSettext']
            result = self.vs.waitForSearchedValueSet()
            self.vs.enterValueSetName(value_set['valuesetname'])
            time.sleep(3)
            self.vs.clickSearchedFValueSet()
            result_2 = self.vs.verifyIndexText()
            assert result_2 == value_set['index_text']
            time.sleep(2)
            self.vs.clickDuplicateDetail()
            time.sleep(2)
            result_3 = self.vs.verifyDuplicateDetailButtonText()
            assert result_3 == value_set['Duplicate_Button_Text']
            self.vs.closeduplicatedetailpopup()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time, start_time)

    @allure.testcase("Set Default")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_setDefault(self):
        start_time = time.time()
        tc_desc = "Verify that user set default version of valueset"
        tc_status = "FAIL"
        tc_name = "Set_Default_Valueset_TC01"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            self.dsp.goToValueSet()
            self.vs.pageRefresh()
            result_1 = self.dsp.verifyValueSettext()
            assert result_1 == value_set['ExpectedValueSettext']
            result = self.vs.waitForSearchedValueSet()
            self.vs.enterValueSetName(value_set['valuesetname'])
            time.sleep(2)
            self.vs.clickSearchedFValueSet()
            result_2 = self.vs.verifyIndexText()
            assert result_2 == value_set['index_text']
            time.sleep(2)
            self.vs.duplicateButton()
            time.sleep(2)
            self.vs.addDuplicateButton()
            self.vs.verifyEnable()
            time.sleep(4)
            self.vs.verifyEnable()
            time.sleep(4)
            self.vs.setDefault()
            time.sleep(4)
            message_text = self.vs.verifySucessMessage()
            assert message_text == value_set['Add_message_text']
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time, start_time)

    @allure.testcase("Cancel Default")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cancelDefault(self):
        start_time = time.time()
        tc_desc = "Verify that user is able to cancel the set default popup"
        tc_status = "FAIL"
        tc_name = "Cancel_Set_Default_Valueset_TC01"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            self.dsp.goToValueSet()
            self.vs.pageRefresh()
            result_1 = self.dsp.verifyValueSettext()
            assert result_1 == value_set['ExpectedValueSettext']
            result = self.vs.waitForSearchedValueSet()
            self.vs.enterValueSetName(value_set['valuesetname'])
            time.sleep(3)
            self.vs.clickSearchedFValueSet()
            result_2 = self.vs.verifyIndexText()
            assert result_2 == value_set['index_text']
            time.sleep(2)
            self.vs.duplicateButton()
            time.sleep(2)
            self.vs.cancelDuplicateButtonPopup()
            time.sleep(4)
            self.vs.verifyEnable()
            result_3 = self.vs.verifyIndexText()
            assert result_3 == value_set['index_text']
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time, start_time)

    @allure.testcase("Close Popup")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_closePopup(self):
        start_time = time.time()
        tc_desc = "Verify that user is able to close the set default popup"
        tc_status = "FAIL"
        tc_name = "Close_Set_Default_Valueset_TC01"
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
            self.vs.clickSearchedFValueSet()
            result_2 = self.vs.verifyIndexText()
            assert result_2 == value_set['index_text']
            time.sleep(2)
            self.vs.duplicateButton()
            time.sleep(2)
            self.vs.verifyEnable()
            self.vs.closeDuplicatePopUpButton()
            time.sleep(4)
            self.vs.verifyEnable()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time, start_time)

