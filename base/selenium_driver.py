from datetime import date, datetime

import psycopg2
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from sqlalchemy.orm import sessionmaker
import pandas as pd

import Utils.Custom_logger as cl
import logging
import time
import os

from Utils.configreader import db


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../Report/screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()



    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False


    def verifyTextContains(self, actualText, expectedText,locator, locatorType="id"):
        """
        Verify actual text contains expected text string

        Parameters:
            expectedList: Expected Text
            actualList: Actual Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText+locator+locatorType)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText+locator+locatorType)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element



    def getElementList(self, locator, locatorType="id"):
        """
        NEW METHOD
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def elementClick(self, locator="", locatorType="id", element=None):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
                try:
                    element.click()
                    self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
                except ElementClickInterceptedException:
                    time.sleep(5)
                    element.click()
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def elementClear(self, locator="", locatorType="id", element=None):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.clear()
            self.log.info("Cleared the data with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot clear the data with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()


    def isEnable(self, locator="", locatorType="id", element=None):

        try:

            element = self.getElement(locator, locatorType)
            if element.is_enabled():
                self.log.info("Button is enabled with locator: " + locator +
                          " locatorType: " + locatorType)
            else:
                self.log.info("Button is not enabled with locator: " + locator +
                              " locatorType: " + locatorType)

        except:
            self.log.info("Button is not enabled with locator:" + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator: # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        Check if element is present -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False

    def jsClick(self,locator,locatorType,element=None):
        try:
            if locator:
                element = self.getElement(locator,locatorType)
                self.driver.execute_script("arguments[0].click();", element)
                self.log.info("Element is clickable with locator: " + locator +
                          " locatorType: " + locatorType)
                return element
        except:
            self.log.info("Element is not Clickable with locator:" + locator +
                          " locatorType: " + locatorType)
            print_stack()


    def duplicateClick(self,data):
        if data:
            data = self.driver.find_element_by_xpath("//table/tbody/tr[1]/td[1]")
            self.driver.execute_script("arguments[0].click();", data)
            self.log.info("Clicked on the first element of the list")
            return data
        else:
            self.log.info("Unable to click on the element")

    def pageRefresh(self):
        time.sleep(3)
        self.driver.refresh()





    def elementPresenceCheck(self, locator, byType):
        """
        Check if element is present
        """
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + str(byType))
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + str(byType))
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                               timeout=5, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def webScroll(self, direction="up"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")



    def isCheckBoxSelected(self,locator,locatorType='id',element = None):

        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            isChecked = self.driver.find_element(byType,locator).get_attribute("checked")
            if isChecked is not None:
                self.log.info("Element checked with locator:"+locator+"and locatorType:"+locatorType, isChecked)
            else:
                self.log.info("Element checked - false")
        except:
            self.log.info("Element not found with locator:"+locator+"and locatorType:"+locatorType)


    def createConnection(self):
        try:

            conn = psycopg2.connect(dbname=db['dbname'], host=db['host'],
                                    port=db['port'],
                                    user=db['user'],
                                    password=db['password'])
            self.log.info(conn)

            # create a Session
            Session = sessionmaker(bind=conn)
            session = Session()

            # print the connection if successful
            print("psycopg2 connection:", conn)

        except Exception as err:
            print("psycopg2 connect() ERROR:", err)


        return conn

    def close_connection(self,connection):
        if connection:
            connection.close()
            self.log.info("Postgres connection is closed")

    def insert_new_record(self,test_name,test_desc, test_status,test_priority,day_duration):
        connection = self.createConnection()
        self.cursor = connection.cursor()
        insert_command = "INSERT INTO delivery.test_api_automation_qa(tc_name,tc_desc,tc_status,tc_priority," \
                         "dduration)VALUES(" \
                         "'{}','{}','{}','{}','{}')".format(test_name,test_desc,test_status,test_priority,day_duration)
        self.log.info(insert_command)
        self.cursor.execute(insert_command)
        connection.commit()
        self.log.info("Record inserted sucessfully")
        self.close_connection(connection)

    def getTime(self):
        today = date.today()
        self.log.info(today)

    def getDateAndTime(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.log.info(dt_string)









#dbname=db['dbname'],host=db['host'],port=db['port'],user=db['user'],password=db['password']