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


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ValueSetTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def TestclassSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.mp = MeasurePage(self.driver)
        self.dsp = DataShopPage(self.driver)
        self.vs = ValuePage(self.driver)
        self.ts = TestStatus(self.driver)

    @allure.testcase("Edit Valueset with save")
    @pytest.mark.flaky(reruns=0, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
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

    @allure.testcase("Edit Valueset with cancel")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_CancelValueSet(self):
        tc_desc = "Cancel the Edit duplicate valueset with new name"
        tc_status = "FAIL"
        tc_name = "Edit_TC02"
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
            self.vs.clickEditValueSetDetail()
            time.sleep(2)
            self.vs.cancelValueSetName()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)


    @allure.testcase("Verify name in edit valueset popup")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ValidateNameValueSet(self):
        tc_desc = "Verify popup heading"
        tc_status = "FAIL"
        tc_name = "Edit_TC03"
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
            self.vs.clickEditValueSetDetail()
            time.sleep(2)
            self.vs.verifyEditPopupName()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)




    @allure.testcase("Close valueset popup with close button")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_CloseValueSet(self):
        tc_desc = "Close the Edit duplicate valueset with close button"
        tc_status = "FAIL"
        tc_name = "Edit_TC04"
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
            self.vs.clickEditValueSetDetail()
            time.sleep(2)
            self.vs.closeEditPopup()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)

    @allure.testcase("No valueset found")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_InvalidValueSet(self):
        tc_desc = "No valueset found"
        tc_status = "FAIL"
        tc_name = "Edit_TC05"
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
            self.vs.searchAndClickValueSet(value_set['invalidValueSet'])
            time.sleep(3)
            t1 = self.vs.noValueSetFound()
            assert t1 == value_set['no_value_set_text']
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)


    @allure.testcase("Count the number of valueSet")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_CountTotalValueSet(self):
        tc_desc = "Count total number of value-set"
        tc_status = "FAIL"
        tc_name = "Edit_TC06"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            self.dsp.goToValueSet()
            time.sleep(4)
            self.vs.countTotalValueSet()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)

    @allure.testcase("Count entered valueSet")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_CountTotalValueSet(self):
        tc_desc = "Count total number of entered value-set"
        tc_status = "FAIL"
        tc_name = "Edit_TC07"
        tc_priority = "Low"
        tc_time = self.sd.getTime()
        try:
            self.lp.login(user_data['username'], user_data['password'])
            result = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result, "Login was successful")
            self.dsp.goToValueSet()
            time.sleep(4)
            self.vs.enterValueSetName(value_set['valuesetname'])
            time.sleep(2)
            self.vs.countTotalValueSet()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)

    @allure.testcase("Save Changes")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_saveChanges(self):
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
            time.sleep(5)
            self.vs.verifyEnableSaveButton()
            self.vs.clickSaveButton()
            self.vs.verifyEnableSaveButton()
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)


    @allure.testcase("Cancel with save and close")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cancelWithSaveAndClose(self):
        tc_desc = "Cancel with save and close"
        tc_status = "FAIL"
        tc_name = "Edit_TC09"
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
            time.sleep(2)
            self.vs.cancelButton()
            time.sleep(4)
            self.vs.verifySaveAndCloseButton()
            self.vs.saveAndClose()
            self.vs.verifySaveAndCloseButton()
            result_3 = self.vs.verifyIndexText()
            assert result_3 == value_set['index_text']
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)

    @allure.testcase("Cancel with cancel")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cancelWithCancel(self):
        tc_desc = "Cancel with cancel"
        tc_status = "FAIL"
        tc_name = "Edit_TC10"
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
            time.sleep(2)
            self.vs.cancelButton()
            time.sleep(4)
            self.vs.verifyCancelEditButtonPopup()
            self.vs.cancelEditButtonPopup()
            self.vs.verifyCancelEditButtonPopup()
            result_3 = self.vs.verifyIndexText()
            assert result_3 == value_set['index_text']
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)

    @allure.testcase("Cancel with close without saving")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cancelWithCloseWithoutSaving(self):
        tc_desc = "Cancel with close without saving"
        tc_status = "FAIL"
        tc_name = "Edit_TC11"
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
            time.sleep(2)
            self.vs.cancelButton()
            time.sleep(4)
            self.vs.verifyCloseWithoutSavingButtonPopup()
            self.vs.closeWithoutSavingButton()
            self.vs.verifyCloseWithoutSavingButtonPopup()
            result_3 = self.vs.verifyIndexText()
            assert result_3 == value_set['index_text']
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)

    @allure.testcase("close cancel popup")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_closeCancelPopup(self):
        tc_desc = "Cancel with close icon"
        tc_status = "FAIL"
        tc_name = "Edit_TC12"
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
            time.sleep(2)
            self.vs.cancelButton()
            time.sleep(4)
            self.vs.closeEditCancelPopup()
            result_3 = self.vs.verifyIndexText()
            assert result_3 == value_set['index_text']
            tc_status = "PASS"
        except Exception as e:
            tc_status = "FAIL"
        finally:
            self.sd.insert_new_record(tc_name, tc_desc, tc_status, tc_priority, tc_time)

