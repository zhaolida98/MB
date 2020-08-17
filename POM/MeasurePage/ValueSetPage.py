import logging
import time

import Utils.Custom_logger as cl
from Utils.configreader import VP
from base.selenium_driver import SeleniumDriver


class ValuePage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ##ValuesetPage
    _search_valueset = VP['searchvalueset']
    _searched_valueset = VP['searchedvalueset']
    ##Left hand side edit details
    _edit_valueset_detail=VP['editvaluesetdetail']
    _edit_value_name = VP['editvaluename']
    _save_valueset = VP['savevalueset']
    #####Validate the name
    _verify_edit_name = VP['verifyeditname']
    _close_edit_popup = VP['closeeditpopup']
    _no_valueset_found = VP['novaluesetfound']
    _count_total_valueSet = VP['counttotalvalueSet']
    _cancel_valueset = VP['cancelvalueset']
    _duplicate_valueset_detail = VP['duplicatevaluesetdetail']
    _duplicate_detail_popup_name = VP['duplicatedetailpopupname']
    _some_error_occurred = VP['someerroroccurred']
    _valueSetDuplicateName = VP['valueSetDuplicateName']
    _duplicate_button_valuesetdetail = VP['duplicatebuttonvaluesetdetail']
    _cancel_duplicatebutton_valuesetdetail = VP['cancelduplicatebuttonvaluesetdetail']
    _close_duplicate_popup = VP['closeduplicatepopup']
    _duplicate_popup_name = VP['duplicatepopupname']
    _delete_valueSet = VP['deletevalueSet']
    _yes_delete = VP['yesdelete']
    _cancel_delete = VP['canceldelete']
    _close_delete_popup = VP['closedeletepopup']
        ## Right top side details
    _duplicate_button = VP['duplicatebutton']
    _add_button_value = VP['addbuttonvalue']
    _set_default = VP['setdefault']
    _cancel_button_value = VP['cancelbuttonvalue']
    _edit_duplicate_button = VP['editduplicatebutton']
    _edit_valueSet_rightside = VP['editvalueSetrightside']
    _save_edit_button = VP['saveeditbutton']
    _cancel_edit_button = VP['canceleditbutton']
    _close_without_saving_popup = VP['closewithoutsavingpopup']
    _cancel_edit_button_popup = VP['canceleditbuttonpopup']
    _save_and_close_popup = VP['saveandclosepopup']
    ##Add new value-set
    _valueset_name = VP['valuesetname']
    _success_edit_valueset = VP['successeditvalueset']
    _close_duplicate_button_popup = VP['closeduplicatebuttonpopup']
    _close_edit_cancel_popup = VP['closeeditcancelpopup']
    _start_index_text_xpath = "//p[contains(text(),'Start Index')]"
    _duplicatesearchedvalueset_xpath = VP['duplicatesearchedvalueset']


    def verifyIndexText(self):
        index = self.getText(self._start_index_text_xpath,locatorType="xpath")
        return index

    def editRSide(self):
        self.elementClick(self._edit_valueSet_rightside,locatorType="xpath")

    def closeEditCancelPopup(self):
        self.elementClick(self._close_edit_cancel_popup,locatorType="xpath")

    def closeWithoutSavingButton(self):
        self.elementClick(self._close_without_saving_popup,locatorType="xpath")

    def cancelEditButtonPopup(self):
        self.elementClick(self._cancel_edit_button_popup,locatorType="xpath")

    def cancelButton(self):
        self.jsClick(self._cancel_edit_button,locatorType="xpath")

    def saveAndClose(self):
        self.elementClick(self._save_and_close_popup,locatorType="xpath")

    def saveEditButton(self):
        self.elementClick(self._save_edit_button,locatorType="xpath")

    def editButton(self):
        self.elementClick(self._edit_duplicate_button,locatorType="xpath")


    def verifySucessMessage(self):
        message_text = self.getText(self._success_edit_valueset,locatorType="xpath")
        return message_text

    def closeDuplicatePopUpButton(self):
        self.elementClick(self._close_duplicate_button_popup,locatorType="xpath")

    def setDefault(self):
        self.elementClick(self._set_default,locatorType="xpath")

    def getValueSetName(self):
        self.getText(self._valueset_name,locatorType="xpath")

    def duplicateButton(self):
        self.elementClick(self._duplicate_button,locatorType="xpath")

    def addDuplicateButton(self):
        self.elementClick(self._add_button_value,locatorType="xpath")

    def cancelDuplicateButtonPopup(self):
        self.elementClick(self._cancel_button_value,locatorType="xpath")

    def deleteValueSet(self):
        self.elementClick(self._delete_valueSet,locatorType="xpath")

    def confirmDelete(self):
        self.elementClick(self._yes_delete,locatorType="xpath")

    def cancelDelete(self):
        self.elementClick(self._cancel_delete,locatorType="xpath")

    def closeDeletePopup(self):
        self.elementClick(self._close_delete_popup,locatorType="xpath")

    def duplicatedetailpopupnameValidate(self):
        self.isElementPresent(self._duplicate_popup_name,locatorType="xpath")

    def closeduplicatedetailpopup(self):
        self.elementClick(self._close_duplicate_popup,locatorType="xpath")

    def cancelDuplicateDetail(self):
        self.elementClick(self._cancel_duplicatebutton_valuesetdetail,locatorType="xpath")

    def clickDuplicateDetail(self):
        self.elementClick(self._duplicate_valueset_detail,locatorType="xpath")

    def clickDuplicateButton(self):
        self.getElementList(self._duplicate_valueset_detail,locatorType="xpath")

    def verifyDuplicateValueSetName(self):
        name = self.getText(self._duplicate_detail_popup_name,locatorType="xpath")
        return name

    def verifyDuplicateNameChange(self):
        dname = self.isElementPresent(self._valueSetDuplicateName,locatorType="xpath")
        return dname

    def validateDuplicateName(self,actualtext="",expectedtext=""):
        dname_1 = self.verifyTextContains(actualtext,expectedtext,locatorType="xpath")
        return dname_1

    def getDuplicateValueSetText(self):
        result = self.getText(self._valueSetDuplicateName,locatorType="xpath")
        return result


    def clickDuplicateDetailButton(self):
        self.elementClick(self._duplicate_button_valuesetdetail,locatorType="xpath")

    def verifyDuplicateDetailButtonText(self):
        result = self.getText(self._duplicate_button_valuesetdetail,locatorType="xpath")
        return result

    def noValueSetFound(self):
        result_1 = self.getText(self._no_valueset_found,locatorType="xpath")
        return result_1

    def countTotalValueSet(self):
        self.getText(self._count_total_valueSet,locatorType="xpath")



    def closeEditPopup(self):
        self.elementClick(self._close_edit_popup,locatorType="xpath")

    def verifyEditPopupName(self):
        self.getText(self._verify_edit_name, locatorType='xpath')

    def enterValueSetName(self, valueset):
        self.sendKeys(valueset, self._search_valueset, locatorType="xpath")

    def clickSearchedFValueSet(self):
        self.jsClick(self._duplicatesearchedvalueset_xpath, locatorType="xpath")

    def waitForSearchedValueSet(self):
        svs = self.waitForElement(self._searched_valueset, locatorType="xpath")
        result = self.isElementPresent(element=svs)
        return result


    def clickEditValueSetDetail(self):
        self.elementClick(self._edit_valueset_detail,locatorType="xpath")

    def clearValueSetName(self):
        self.elementClear(self._edit_value_name,locatorType="xpath")


    def entereditvaluesetName(self, name):
        self.sendKeys(name,self._edit_value_name,locatorType="xpath")

    def saveValueSetName(self):
        self.elementClick(self._save_valueset,locatorType="xpath")

    def verifySaveButtonText(self):
        name = self.getText(self._save_valueset,locatorType="xpath")
        return name


    def cancelValueSetName(self):
        self.elementClick(self._cancel_valueset,locatorType="xpath")

    def clickSearchedValueSet(self):
        self.elementClick(self._searched_valueset,locatorType="xpath")



    def searchAndClickFirstValueSet(self, valueset):
        self.enterValueSetName(valueset)
        time.sleep(5)
        self.clickSearchedFValueSet()

    def searchAndClickValueSet(self, valueset):
        self.enterValueSetName(valueset)
        time.sleep(5)
        self.clickSearchedValueSet()



    def verifyEnable(self):
        self.isEnable(self._set_default,locatorType="xpath")


    def verifyEnableSaveButton(self):
        self.isEnable(self._save_edit_button,locatorType="xpath")

    def verifySaveAndCloseButton(self):
        self.isEnable(self._save_and_close_popup,locatorType="xpath")

    def verifyCancelEditButtonPopup(self):
        self.isEnable(self._cancel_edit_button_popup,locatorType="xpath")

    def verifyCloseWithoutSavingButtonPopup(self):
        self.isEnable(self._close_without_saving_popup,locatorType="xpath")

    def clickSaveButton(self):
        self.elementClick(self._save_edit_button,locatorType="xpath")













