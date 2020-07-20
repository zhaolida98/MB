import logging
import time

import allure
from allure_commons.types import AttachmentType

import utilities.Custom_logger as cl
from base.selenium_driver import SeleniumDriver


class ValuePage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        ##ValuesetPage
    _search_valueset = "//input[@placeholder='Search']"
    _searched_valueset = "//tr[1]//td[1]"
        ##Left hand side edit details
    _edit_valueset_detail="//div[@class='sc-jDwBTQ jAsbbw']//button[@class='sc-ifAKCX gFckEz'][contains(text()," \
                              "'Edit')]"
    _edit_value_name = "//input[@placeholder='Name']"
    _save_valueset = "//div[@class='sc-caSCKo gujKlR']//button[text()='Save']"
    _cancel_valueset = "//div[@class='sc-caSCKo gujKlR']//button[text()='Cancel']"
    _duplicate_valueset_detail = "//div[@class='sc-jDwBTQ jAsbbw']//button[@class='sc-ifAKCX gFckEz'][contains(text(),'Duplicate')]"
    _duplicate_button_valuesetdetail = "//button[@class='sc-ifAKCX SmNIF']"
    _cancel_duplicatebutton_valuesetdetail = "//button[contains(text(),'Cancel')]"
        ## Right top side details
    _duplicate_button = "//div[@class='sc-jAaTju eHDsWC']//button[@class='sc-ifAKCX gFckEz'][contains(text(),'Duplicate')]"
    _add_button_value = "//div[@class='sc-caSCKo gujKlR']//button[contains(text(),'Add')]"
    _cancel_button_value = "//div[@class='sc-caSCKo gujKlR']//button[contains(text(),'Cancel')]"
    _edit_duplicate_button = "//div[@class='sc-jAaTju eCacIb']//div[3]"
    _save_edit_button = "//button[@class='sc-ifAKCX SmNIF']"
    _cancel_edit_button = "//button[contains(text(),'Cancel')]"
    _close_without_saving_popup = "//button[contains(text(),'Close without saving')]"
    _cancel_edit_button_popup = "//div[@class='sc-jAaTju hoRdzg']//button[@class='sc-ifAKCX gFckEz'][contains(text(),'Cancel')]"
    _save_and_close_popup = "//button[contains(text(),'Save & Close')]"
        ##Add new value-set


    def enterValueSetName(self, valueset):
        self.sendKeys(valueset,self._search_valueset,locatorType="xpath")

    def clickSearchedValueSet(self):
        self.elementClick(self._searched_valueset,locatorType="xpath")

    def clickEditValueSetDetail(self):
        self.elementClick(self._edit_valueset_detail,locatorType="xpath")

    def enterValuesetName(self, name):
        self.sendKeys(self._edit_value_name,locatorType="xpath")

    def saveValueSetName(self):
        self.elementClick(self._save_valueset,locatorType="xpath")


    def cancelValueSetName(self):
        self.elementClick(self._cancel_valueset,locatorType="xpath")


    def searchAndClickValueSet(self, valueset):
        self.enterValueSetName(valueset)
        time.sleep(5)
        self.clickSearchedValueSet()











