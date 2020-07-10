import time
import unittest

import allure
import pytest

from pages.home.DataShopPage import DataShopPage
from pages.home.login_pages import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SMTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def TestclassSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.dshop = DataShopPage(self.driver)

    @allure.testcase("Validate the count of measure as per the search criteria")
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_validSearch(self):
        self.lp.login("himanshu.verma@innovaccer.com", "Innovaccer@123")
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        time.sleep(10)
        self.dshop.searchMeasure("Test")
        time.sleep(5)
