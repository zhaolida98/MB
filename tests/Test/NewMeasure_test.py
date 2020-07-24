import time
import unittest

import allure
import pytest

from pages.Datashop.DataShopPage import DataShopPage
from pages.MeasurePage.MeasurePage import MeasurePage
from pages.home.login_page import LoginPage
from utilities.configreader import user_data, measure_data
from utilities.teststatus import TestStatus


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
    #@pytest.mark.skip
    def test_clickSearchedMessage(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        time.sleep(3)
        self.dsp.clickMBLink()
        time.sleep(3)
        self.mp.newMeasure()
        time.sleep(2)
        self.mp.cancelMeasureModal()
        time.sleep(4)

    @allure.testcase("Click on cancel new measure modal")
    @allure.description("PTCS-T20193 (1.0)")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    #@pytest.mark.skip
    def test_selectDeselectPoorMeasure(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        time.sleep(3)
        self.dsp.clickMBLink()
        time.sleep(3)
        self.dsp.searchMeasure(measure_data['wrong_measure_name'])
        time.sleep(2)
        self.mp.clicksearchMeasure()
        time.sleep(2)
        self.mp.isCheckBoxSelected()
        time.sleep(5)

    @allure.testcase("Validate measure count of all measures")
    @allure.description("")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_countAllMeasure(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        time.sleep(3)
        self.dsp.clickMBLink()
        time.sleep(3)
        self.dsp.measureCount()
        time.sleep(3)



    @allure.testcase("Validate measure count with valid measure")
    @allure.description("")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_countValidMeasure(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        time.sleep(3)
        self.dsp.clickMBLink()
        time.sleep(3)
        self.dsp.searchMeasure(measure_data['measurename'])
        time.sleep(3)
        self.dsp.measureCount()


    @allure.testcase("Validate measure count with invalid measure")
    @allure.description("")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_countNoMeasure(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        time.sleep(3)
        self.dsp.clickMBLink()
        time.sleep(3)
        self.dsp.searchMeasure(measure_data['wrong_measure_name'])
        time.sleep(3)
        self.dsp.measureCount()



