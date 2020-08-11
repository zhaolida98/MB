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
        self.mp.deleteMeasureDetail()

    @allure.testcase("Cancel Delete measure detail")
    @pytest.mark.flaky(reruns=1, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cancelDelete(self):
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
        self.mp.cancelMeasureDeleteDetails()

    @allure.testcase("Close delete Measure Popup")
    @pytest.mark.flaky(reruns=1, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_closeDeletePopup(self):
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


