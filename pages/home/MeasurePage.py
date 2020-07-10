import logging
import time

import allure
from allure_commons.types import AttachmentType

import utilities.Custom_logger as cl
from base.selenium_driver import SeleniumDriver


class MeasurePage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _edit_measure_detail_xpath = "//button[@id='meta-edit']"
    _duplicate_measure_detail_xpath = "//button[@id='meta-content']"
    _duplicate_save_measure_detail_xpath = "//button[@id='measure-version=duplicate']"
    _duplicate_cancel_measure_detail_xpath = "//button[@id='measure-version-cancel']"
    _delete_measure_detail_xpath = "//button[@id='meta-duplicate']"
    _duplicate_measure_xpath = "//button[contains(text(),'Duplicate')]"
    _edit_measure_xpath = "//button[@class='button secondary no-margin ng-scope']"
    _measure_text_xpath = "//div[@class='columns large-12 section-heading']//span"
    _save_edit_measure_detail_xpath = "//button[@id='new-measure-modal-save']"
    _cancel_edit_measure_detail_xpath = "//button[@id='new-measure-modal-cancel']"
    _chk_poor_measure_xpath = "//input[@id='new-measure-modal-poor']"
    _measure_version_dropdown_xpath = "//div[@class='selectize-input']"
    _searched_measure_xpath = "//tr[1]//td[1]"

    def clickEditMeasureDetail(self):
        self.elementClick(self._edit_measure_detail_xpath, locatorType="xpath")

    def clickSearchMessage(self):
        self.elementClick(self._searched_measure_xpath, locatorType="xpath")

    def clickDuplicateMeasureDetail(self):
        self.elementClick(self._duplicate_measure_detail_xpath, locatorType='xpath')

    def clickDuplicateSaveMeausreDetail(self):
        self.elementClick(self._duplicate_save_measure_detail_xpath, locatorType="xpath")

    def clickDuplicateCancelMeausreDetail(self):
        self.elementClick(self._duplicate_cancel_measure_detail_xpath, locatorType="xpath")

    def clickDeleteMeasureDetail(self):
        self.elementClick(self._delete_measure_detail_xpath, locatorType='xpath')

    def clickEditMeasure(self):
        self.elementClick(self._edit_measure_xpath, locatorType="xpath")

    def clickDuplicateMeasure(self):
        self.elementClick(self._duplicate_measure_xpath, locatorType='xpath')

    def clickEditMeasureOverview(self):
        self.elementClick(self._edit_measure_detail_xpath, locatorType="xpath")

    def clickSaveEditMeasureOverview(self):
        self.elementClick(self._save_edit_measure_detail_xpath, locatorType="xpath")

    def clickCancelEditMeasure(self):
        self.elementClick(self._cancel_edit_measure_detail_xpath, locatorType="xapth")

    def clickCancelDuplicateMeasure(self):
        self.elementClick(self._cancel_edit_measure_detail_xpath, locatorType="xpath")

    def chkVersionDetails(self):
        select_box = self.elementClick(self._measure_version_dropdown_xpath)
        options = [x for x in select_box.find_elements_by_tag_name("span")]
        for element in options:
            return
            element.get_attribute("value")

    ### This is the functionality.

    def clicksearchMeasure(self, measurename=""):
        self.clickSearchMessage()
        allure.attach(self.driver.get_screenshot_as_png(), name="Search_Measure", attachment_type=AttachmentType.PNG)

    def editsearchMeasure(self, measurename=""):
        self.clickEditMeasureOverview()
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="Edit_measure", attachment_type=AttachmentType.PNG)
        self.clickSaveEditMeasureOverview()

    def duplicateMeasure(self, measurename=""):
        self.clickDuplicateMeasureDetail()
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="Duplicate_Measure", attachment_type=AttachmentType.PNG)
        self.clickDuplicateSaveMeausreDetail()

    def cancelEditMeasure(self):
        self.clickEditMeasureOverview()
        allure.attach(self.driver.get_screenshot_as_png(), name="Edit_measure", attachment_type=AttachmentType.PNG)
        self.clickCancelEditMeasure()

    def cancelDuplicateMeasure(self):
        self.clickDuplicateMeasureDetail()
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="Duplicate_Measure", attachment_type=AttachmentType.PNG)
        self.clickCancelDuplicateMeasure()

    def verifyMeasureText(self):
        result = self.isElementPresent(self._measure_text_xpath, locatorType="xpath")
        allure.attach(self.driver.get_screenshot_as_png(), name="MeasureScreen", attachment_type=AttachmentType.PNG)
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._failed_login, locatorType="xpath")
        return result

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()
