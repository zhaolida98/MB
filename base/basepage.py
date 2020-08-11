from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from Utils.util import Util

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.title
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    def verifyText(self, Expectedtext):
        """
        Verify the page Title

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualText = self.text
            return self.util.verifyTextContains(actualText, Expectedtext)
        except:
            self.log.error("Failed to get text")
            print_stack()
            return False