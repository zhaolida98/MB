import time
import unittest

import allure
import pytest

from pages.home.DataShopPage import DataShopPage
from pages.home.MeasurePage import MeasurePage
from pages.home.login_pages import LoginPage
from utilities.configreader import user_data, measure_data


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SMCTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def TestclassSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.mp = MeasurePage(self.driver)
        self.dsp = DataShopPage(self.driver)

    @allure.testcase("Click on searched measure as per the search criteria")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_clickSearchedMessage(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.dsp.searchMeasure(measure_data['measurename'])
        time.sleep(2)
        self.mp.clicksearchMeasure()
        time.sleep(5)

    @allure.testcase("Click on Edit measure as per the search criteria")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_editSearchedMessage(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.dsp.searchMeasure(measure_data['measurename'])
        time.sleep(2)
        self.mp.clicksearchMeasure()
        time.sleep(5)
        self.mp.editsearchMeasure()
        time.sleep(5)

    @allure.testcase("Click on duplicate measure as per the search criteria")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_duplicateSearchedMessage(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.dsp.clickLink()
        self.dsp.searchMeasure(measure_data['measurename'])
        time.sleep(2)
        self.mp.clicksearchMeasure()
        time.sleep(3)
        self.mp.duplicateMeasure()
        time.sleep(2)
        self.cancelDuplicateMeasure()

    @allure.testcase("Click on cancel edit measure as per the search criteria")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_duplicateSearchedMessage(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.dsp.clickLink()
        self.dsp.searchMeasure(measure_data['measurename'])
        time.sleep(2)
        self.mp.clicksearchMeasure()
        time.sleep(5)
        self.mp.cancelEditMeasure()
        time.sleep(2)

    @allure.testcase("Click on cancel duplicate measure as per the search criteria")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_duplicateSearchedMessage(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.dsp.clickLink()
        self.dsp.searchMeasure(measure_data['measurename'])
        time.sleep(2)
        self.mp.clicksearchMeasure()
        time.sleep(5)
        self.mp.cancelDuplicateMeasure()
        time.sleep(5)
