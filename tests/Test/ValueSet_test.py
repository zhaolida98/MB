import time
import unittest

import allure
import pytest

from pages.Datashop.DataShopPage import DataShopPage
from pages.MeasurePage.MeasurePage import MeasurePage
from pages.MeasurePage.ValueSetPage import ValuePage
from pages.home.login_page import LoginPage
from utilities.configreader import user_data, value_set
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ValueSetTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def TestclassSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.mp = MeasurePage(self.driver)
        self.dsp = DataShopPage(self.driver)
        self.vs = ValuePage(self.driver)
        self.ts = TestStatus(self.driver)

    @allure.testcase("Click on searched measure detail as per the search criteria")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_clickSearchedValueSet(self):
        self.lp.login(user_data['username'], user_data['password'])
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verified")
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")
        self.dsp.clickValueSetLink()
        time.sleep(5)
        self.vs.searchAndClickValueSet(value_set['valuesetname'])
        time.sleep(5)
