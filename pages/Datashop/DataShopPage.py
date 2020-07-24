import logging
import time

import utilities.Custom_logger as cl
from base.selenium_driver import SeleniumDriver


class DataShopPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _analytics_link_xpath = "//a[contains(text(),'Analytics')]"
    _measure_builder_xpath = "//a[contains(text(),'Measure Builder')]"
    _value_set = "//a[contains(text(),'Value Sets')]"
    _search_measure_xpath = "//input[@id='search']"
    _three_dots_xpath = "//tr[1]//td[7]//span[1]//i[1]"
    _no_measure_text = "//h4[@class='title']"
    _measure_count_xpath = "//div[@id='main_content']/div[2]/div/div[@class='ng-scope']/div/section[1]//span[" \
                       "@class='label count ng-binding']"

    # Actions performed on the Element.

    def getNoMeasureText(self):
        self.getText(locator=self._no_measure_text,locatorType="xpath")


    def clickAnalyticsLink(self):
        self.elementClick(self._analytics_link_xpath, locatorType="xpath")

    def clickMeasureBuilder(self):
        self.elementClick(self._measure_builder_xpath, locatorType="xpath")

    def clickSearchMeasure(self):
        self.elementClick(self._search_measure_xpath, locatorType="xpath")

    def enterSearchMeasure(self, measurename):
        self.sendKeys(measurename, self._search_measure_xpath, locatorType="xpath")

    def clickValueset(self):
        self.elementClick(self._value_set,locatorType="xpath")

    def measureCount(self):
        self.getText(self._measure_count_xpath, locatorType="xpath")


    ### This is the functionality.

    def clickMBLink(self):
        self.clickAnalyticsLink()
        time.sleep(2)
        self.clickMeasureBuilder()
        time.sleep(2)

    def searchMeasure(self, measurename=""):
        self.clickSearchMeasure()
        self.enterSearchMeasure(measurename)
        time.sleep(2)
        self.measureCount()
        time.sleep(2)

    def clickValueSetLink(self):
        self.clickAnalyticsLink()
        self.clickValueset()

