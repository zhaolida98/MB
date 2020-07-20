import time
import unittest

import allure
import pytest

from pages.Datashop.DataShopPage import DataShopPage
from pages.MeasurePage.MeasurePage import MeasurePage
from pages.home.login_page import LoginPage
from utilities.configreader import user_data


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SMCTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def TestclassSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.mp = MeasurePage(self.driver)
        self.dsp = DataShopPage(self.driver)

    @allure.testcase("Click on duplicate measure as per the search criteria")
    @pytest.mark.flaky(reruns=1, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_duplicateSearchedMessage(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.dsp.clickLink()
        self.dsp.searchMeasure("Test")
        time.sleep(2)
        self.mp.clicksearchMeasure()
        time.sleep(5)
        self.mp.cancelDuplicateMeasure()
        time.sleep(5)
