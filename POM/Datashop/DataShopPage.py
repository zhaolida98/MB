import logging
import time

import Utils.Custom_logger as cl
from Utils.configreader import DSP, value_set
from base.basepage import BasePage


class DataShopPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _analytics_link_xpath = DSP['analytics_link_xpath']
    _measure_builder_xpath = DSP['measure_builder_xpath']
    _value_set = DSP['value_set']
    _search_measure_xpath = DSP['search_measure_xpath']
    _three_dots_xpath = DSP['three_dots_xpath']
    _no_measure_text = DSP['no_measure_text']
    _measure_count_xpath = DSP['measure_count_xpath']
    _measure_text_xpath = "//h4[@class='title inline']"
    _valueset_text_path = "//div[@class='sc-kjoXOD ffVqqg']"

    # Actions performed on the Element.

    def clearSearch(self):
        time.sleep(4)
        self.elementClear(self._search_measure_xpath, locatorType="xpath")

    def verifyValueSettext(self):
        result = self.getText(self._valueset_text_path, locatorType="xpath")
        return result

    def verifyVText(self):
        return self.verifyText(value_set['ExpectedValueSettext'])



    def verifyMeasureText(self):
        result = self.isElementPresent(self._measure_text_xpath,locatorType="xpath")
        return result

    def waitForMBLink(self):
        mb = self.waitForElement(self._measure_builder_xpath,locatorType="xpath")
        result = self.isElementPresent(element=mb)
        return result

    def waitForValueSetLink(self):
        vs = self.waitForElement(self._value_set,locatorType="xpath")
        result = self.isElementPresent(element=vs)
        return result

    def getMeasureText(self):
        self.getText(self._measure_text_xpath,locatorType="xpath")

    def getNoMeasureText(self):
        self.getText(locator=self._no_measure_text,locatorType="xpath")

    def verifyMeasureText(self):
        result = self.isElementPresent(self._no_measure_text,locatorType="xpath")
        return result


    def clickAnalyticsLink(self):
        self.elementClick(self._analytics_link_xpath, locatorType="xpath")

    def clickMeasureBuilder(self):
        self.elementClick(self._measure_builder_xpath, locatorType="xpath")

    def clickSearchMeasure(self):
        self.elementClick(self._search_measure_xpath, locatorType="xpath")

    def enterSearchMeasure(self, measurename):
        self.sendKeys(measurename, self._search_measure_xpath, locatorType="xpath")

    def clickValueSetLink(self):
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

    def goToValueSet(self):
        self.clickAnalyticsLink()
        time.sleep(5)
        self.clickValueSetLink()
        time.sleep(1)




