import logging
import time

import Utils.Custom_logger as cl
from Utils.configreader import MP
from base.selenium_driver import SeleniumDriver


class MeasurePage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _edit_measure_detail_xpath = MP['edit_measure_detail']
    _duplicate_measure_detail_xpath = MP['duplicate_measure_detail']
    _duplicate_save_measure_detail_xpath = MP['duplicate_save_measure_detail']
    _duplicate_cancel_measure_detail_xpath = MP['duplicate_cancel_measure_detail']
    _duplicate_measure_xpath = MP['duplicate_measure']
    _cancel_duplicate_button = MP['cancel_duplicate_button']
    _duplicate_button = MP['duplicate_button']
    _edit_measure_xpath = MP['edit_measure']
    _measure_text_xpath = MP['measure_text']
    _save_edit_measure_detail_xpath = MP['save_edit_measure_detail']
    _cancel_edit_measure_detail_xpath = MP['cancel_edit_measure_detail']
    _chk_poor_measure_xpath = MP['chk_poor_measure']
    _measure_version_dropdown_xpath = MP['measure_version_dropdown']
    _measure_category_xpath = MP['measure_category']
    #########SEARCH MEASURE########################
    _searchMeasureName = MP['searchMeasureName']
    _searched_measure_xpath = MP['searched_measure']
    #########################
    _edit_measure_name=MP['edit_measure_name']
    _edit_measure_type = MP['edit_measure_type']
    ########################
    _delete_measure_detail_xpath = MP['delete_measure_detail']
    _delete_measure_xpath = MP['delete_measure']
    _delete_yes = MP['delete_yes']
    _delete_cancel = MP['delete_cancel']
    _delete_popup_text_xpath = MP['delete_popup_text']
    _delete_button_presence = "//div[@class='row wrapper']//following::div[18]/button[3]/*[text()='delete']"
    ########################
    _new_measure_button = MP['new_measure_button']
    _add_measure_button = MP['add_measure_button']
    _cancel_measure_button = MP['cancel_measure_button']
    _add_new_measure_text = MP['_add_new_measure_text']
    #######################
    _edit_measure_name_1= MP['edit_measure_name_1']
    _edit_measure_program = MP['edit_measure_program']
    _edit_product_line = MP['edit_product_line']
    _edit_poor_measure_textbox = MP['edit_poor_measure_textbox']
    _edit_measure_text_xpath = MP['_edit_measure_text']
    _duplicate_text_xpath = MP['_duplicate_text']
    #########Right Hand Side##################
    _duplicate_measure_button_xpath = MP['duplicate_measure_button']
    _continue_duplicate_button_xpath = MP['continue_duplicate_button']
    _cancel_duplicate_button_xpath = MP['cancel_duplicate_button']
    _close_duplicate_popup_xpath = MP['close_duplicate_popup']

    def deleteButtonEnable(self):
        self.isEnable(self._delete_button_presence, locatorType="xpath")

    def deleteMeasure(self):
        self.elementClick(self._delete_measure_xpath, locatorType="xpath")

    def clickRDuplicateButton(self):
        self.waitForElement(self._duplicate_measure_button_xpath, locatorType="xpath")
        self.elementClick(self._duplicate_measure_button_xpath, locatorType="xpath")

    def clickRContinueDuplicateM(self):
        self.waitForElement(self._continue_duplicate_button_xpath, locatorType="xpath")
        self.elementClick(self._continue_duplicate_button_xpath, locatorType="xpath")

    def cancelRDuplicateM(self):
        self.waitForElement(self._cancel_duplicate_button_xpath, locatorType="xpath")
        self.elementClick(self._cancel_duplicate_button_xpath, locatorType="xpath")

    def closeRDuplicateMPopup(self):
        self.waitForElement(self._close_duplicate_popup_xpath, locatorType="xpath")
        self.elementClick(self._close_duplicate_popup_xpath, locatorType="xpath")





    def verifyMeasureCategory(self):
        result = self.isElementPresent(self._measure_category_xpath,locatorType="xpath")
        return result

    def enterMeasureName(self,mname):
        self.waitForElement(self._searchMeasureName,locatorType="xpath")
        self.sendKeys(mname,self._searchMeasureName,locatorType="xpath")


    def selectDeselectChkbox(self):
        self.isCheckBoxSelected(self._edit_poor_measure_textbox,locatorType="xpath")

    def verifyAddNewMeasureText(self):
        result = self.isElementPresent(self._add_new_measure_text,locatorType="xpath")
        return result

    def newMeasure(self):
        self.elementClick(self._new_measure_button,locatorType="xpath")

    def getmNameText(self):
        self.getText(self._edit_measure_name,locatorType="xpath")

    def verifymName(self):
        result = self.isElementPresent(self._edit_measure_name,locatorType="xpath")
        return result

    def getmProgramText(self):
        self.getText(self._edit_measure_program,locatorType="xpath")

    def verifymProgram(self):
        result = self.isElementPresent(self._edit_measure_program,locatorType="xpath")
        return result

    def getmproductLineText(self):
        self.getText(self._edit_product_line,locatorType="xpath")

    def verifymProductLine(self):
        result = self.isElementPresent(self._edit_product_line,locatorType="xpath")
        return result

    def getmPoorMeasureText(self):
        self.getText(self._edit_poor_measure_textbox,locatorType="xpath")

    def verifyPoorMeasureText(self):
        result = self.isElementPresent(self._edit_poor_measure_textbox,locatorType="xpath")
        return result

    def verifyEditMeasureText(self):
        self.getmNameText()
        self.getmProgramText()
        self.getmproductLineText()
        self.getmPoorMeasureText()



    def cancelMeasureModal(self):
        self.elementClick(self._cancel_measure_button,locatorType="xpath")

    def deleteMeasureDetail(self):
        self.elementClick(self._delete_measure_detail_xpath,locatorType="xpath")

    def confirmDeleteMeasure(self):
        self.elementClick(self._delete_yes,locatorType="xpath")

    def cancelDeleteMeasure(self):
        self.elementClick(self._delete_cancel,locatorType="xpath")


    def verifyDeleteMText(self):
        result = self.isElementPresent(self._delete_popup_text_xpath,locatorType="xpath")
        return result

    def getDeleteMText(self):
        self.getText(self._delete_popup_text_xpath,locatorType="xpath")

    def enterName(self, measurename):
        self.sendKeys(measurename,self._edit_measure_name,locatorType="xpath")

    def enterType(self, measureType):
        self.sendKeys(measureType,self._edit_measure_type,locatorType="xpath")

    def clickEditMeasureDetail(self):
        self.elementClick(self._edit_measure_detail_xpath, locatorType="xpath")

    def clickSearchMeasure(self):
        self.elementClick(self._searched_measure_xpath, locatorType="xpath")

    def waitForDeleteButton(self):
        elem1 = self.waitForElement(self._delete_measure_detail_xpath,locatorType="xpath")
        result = self.elementClick(element=elem1)
        return result

    def clickDuplicateMeasureDetail(self):
        self.elementClick(self._duplicate_measure_detail_xpath, locatorType='xpath')

    def clickDuplicateSaveMeausreDetail(self):
        self.elementClick(self._duplicate_save_measure_detail_xpath, locatorType="xpath")

    def clickDuplicateCancelMeausreDetail(self):
        self.elementClick(self._duplicate_cancel_measure_detail_xpath, locatorType="xpath")

    def clickDeleteMeasureDetail(self):
        self.waitForElement(self._delete_measure_detail_xpath, locatorType='xpath')
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


    def clickDuplicateButton(self):
        self.elementClick(self._duplicate_button,locatorType="xpath")

    def clickCancelDuplicateButton(self):
        self.elementClick(self._cancel_duplicate_button,locatorType="xpath")

    def chkVersionDetails(self):
        select_box = self.elementClick(self._measure_version_dropdown_xpath,locatorType="xpath")
        options = [x for x in select_box.find_elements_by_tag_name("span")]
        for element in options:
            return
            element.get_attribute("value")

    def clicksearchMeasure(self):
        self.clickSearchMessage()

    def measureNameClearFields(self):
        self.elementClear(self._edit_measure_name,locatorType="xpath")

    def measureTypeClearFields(self):
        self.elementClear(self._edit_measure_type,locatorType="xpath")


    def MeasureClearFields(self,measurename,measuretype):
        MeasureName = self.getElement(locator=self._edit_measure_name)
        MeasureName.click()
        MeasureName.clear()
        self.enterName(measurename)
        MeasureType = self.getElement(locator=self._edit_measure_type)
        MeasureType.click()
        MeasureType.clear()
        self.enterType(measuretype)

    def deleteMeasureDetail(self):
        self.confirmDeleteMeasure()


    def cancelMeasureDeleteDetails(self):
        self.cancelDeleteMeasure()



    def duplicateMeasure(self, measurename=""):
        self.clickDuplicateMeasureDetail()
        time.sleep(3)
        self.clickDuplicateSaveMeausreDetail()

    def cancelEditMeasure(self):
        self.clickEditMeasureOverview()
        self.clickCancelEditMeasure()

    def cancelDuplicateMeasure(self):
        self.clickDuplicateMeasureDetail()
        time.sleep(3)
        self.clickCancelDuplicateMeasure()

    def verifyMeasureText(self):
        result = self.isElementPresent(self._measure_text_xpath, locatorType="xpath")
        return result

    def verifyEditMeasureText(self):
        result = self.isElementPresent(self._edit_measure_text_xpath,locatorType="xpath")
        return result

    def verifyDuplicateText(self):
        result = self.isElementPresent(self._duplicate_text_xpath,locatorType="xpath")
        return result


