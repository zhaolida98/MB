import time
import unittest

import allure
import pytest

from pages.Datashop.DataShopPage import DataShopPage
from pages.MeasurePage.MeasurePage import MeasurePage
from pages.home.login_page import LoginPage
from utilities.configreader import measure_data, user_data


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SMTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def TestclassSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.mp = MeasurePage(self.driver)
        self.dsp = DataShopPage(self.driver)

    @allure.testcase("Click on cancel duplicate measure button as per the search criteria")
    @pytest.mark.flaky(reruns=0, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_duplicateSearchedMessage(self):
        self.lp.login(user_data['username'], user_data['password'])
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.dsp.clickLink()
        self.dsp.searchMeasure(measure_data['measurename'])
        time.sleep(2)
        self.mp.clicksearchMeasure()
        time.sleep(2)
        self.mp.clickDuplicateMeasure()
        self.mp.clickCancelDuplicateButton()
        time.sleep(3)
