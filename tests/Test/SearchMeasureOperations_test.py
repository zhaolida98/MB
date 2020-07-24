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
class SMCTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def TestclassSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.mp = MeasurePage(self.driver)
        self.dsp = DataShopPage(self.driver)
        self.ts = TestStatus(self.driver)

    @allure.testcase("Click on searched measure detail as per the search criteria")
    @allure.description("PTCS-T20011 (1.0)")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_clickSearchedMessage(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        self.dsp.clickMBLink()
        self.dsp.searchMeasure(measure_data['measurename'])
        time.sleep(2)
        self.mp.clicksearchMeasure()
        time.sleep(2)

    @allure.testcase("Search non existed measure")
    @allure.description("PTCS-T20202 (1.0)")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_noMeasureMessage(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        self.dsp.clickMBLink()
        time.sleep(2)
        self.dsp.searchMeasure(measure_data['wrong_measure_name'])
        time.sleep(2)
        self.mp.clicksearchMeasure()
        self.dsp.getNoMeasureText()
        time.sleep(3)

    @allure.testcase("Click on Edit measure detail as per the search criteria")
    @allure.description("PTCS-T20018 (1.0)")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_editSearchedMessage(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        self.dsp.clickMBLink()
        self.dsp.searchMeasure(measure_data['measurename'])
        time.sleep(2)
        self.mp.clicksearchMeasure()
        time.sleep(2)
        self.mp.clickEditMeasureOverview()
        time.sleep(2)
        self.mp.MeasureClearFields()
        time.sleep(2)
        self.mp.enterName(measure_data['editMeasureName'])
        time.sleep(2)
        self.mp.enterType(measure_data['editMeasureType'])
        self.mp.clickSaveEditMeasureOverview()

    @allure.testcase("Click on Edit measure detail as per the search criteria")
    @allure.description("PTCS-T20194 (1.0)")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_editSearchedMessage(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        self.dsp.clickMBLink()
        self.dsp.searchMeasure(measure_data['measurename'])
        time.sleep(2)
        self.mp.clicksearchMeasure()
        time.sleep(2)
        self.mp.clickEditMeasureOverview()
        time.sleep(2)
        self.mp.verifyEditMeasureText()
        time.sleep(4)

    @allure.testcase("Click on duplicate measure detail as per the search criteria")
    @allure.description("PTCS-T20013 (1.0)")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_duplicateSearchedMessage(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        self.dsp.clickMBLink()
        self.dsp.searchMeasure(measure_data['measurename'])
        time.sleep(2)
        self.mp.clicksearchMeasure()
        time.sleep(3)
        self.mp.duplicateMeasure()
        time.sleep(2)
        self.mp.cancelDuplicateMeasure()

    @allure.testcase("Click on cancel edit measure detail as per the search criteria")
    @allure.description("PTCS-T20199 (1.0)")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cancelEditMeasureDetail(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        self.dsp.clickMBLink()
        self.dsp.searchMeasure(measure_data['measurename'])
        time.sleep(2)
        self.mp.clicksearchMeasure()
        time.sleep(2)
        self.mp.cancelEditMeasure()
        time.sleep(2)

    @allure.testcase("Click on cancel duplicate measure detail as per the search criteria")
    @allure.description("")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cancelDuplicateMeasureDetail(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        self.dsp.clickMBLink()
        self.dsp.searchMeasure(measure_data['measurename'])
        time.sleep(2)
        self.mp.clicksearchMeasure()
        time.sleep(2)
        self.mp.cancelDuplicateMeasure()
        time.sleep(2)

    @allure.testcase("Click on duplicate measure button as per the search criteria")
    @allure.description("")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_duplicateMeasureButton(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        self.dsp.clickMBLink()
        self.dsp.searchMeasure(measure_data['measurename'])
        time.sleep(2)
        self.mp.clicksearchMeasure()
        time.sleep(2)
        self.mp.clickDuplicateMeasure()
        self.mp.clickDuplicateButton()
        time.sleep(3)


    @allure.testcase("Click on cancel duplicate measure button as per the search criteria")
    @allure.description("")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cancelDuplicateMeasureButton(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        self.dsp.clickMBLink()
        self.dsp.searchMeasure(measure_data['measurename'])
        time.sleep(2)
        self.mp.clicksearchMeasure()
        time.sleep(2)
        self.mp.clickDuplicateMeasure()
        self.mp.clickCancelDuplicateButton()
        time.sleep(3)
