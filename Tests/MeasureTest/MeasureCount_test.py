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

    @allure.testcase("Click on cancel new measure modal")
    @allure.description("PTCS-T20193 (1.0)")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.skip
    def test_cancelNewMeasure(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        self.dsp.clickMBLink()
        self.mp.newMeasure()
        result_1 = self.mp.verifyAddNewMeasureText()
        assert result_1 == True
        self.mp.cancelMeasureModal()

    @allure.testcase("Validate measure count of all measures")
    @allure.description("")
    @pytest.mark.flaky(reruns=0, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_countAllMeasure(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        self.dsp.clickMBLink()
        result_2 = self.dsp.waitForMBLink()
        self.dsp.measureCount()

    @allure.testcase("Validate measure count with valid measure")
    @allure.description("")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_countValidMeasure(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        self.dsp.clickMBLink()
        result_2 = self.dsp.waitForMBLink()
        self.dsp.searchMeasure(measure_data['measurename'])
        self.dsp.measureCount()

    @allure.testcase("Validate measure count with invalid measure")
    @allure.description("")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_countNoMeasure(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        self.dsp.clickMBLink()
        result_2 = self.dsp.waitForMBLink()
        self.dsp.searchMeasure(measure_data['wrong_measure_name'])
        self.dsp.measureCount()



