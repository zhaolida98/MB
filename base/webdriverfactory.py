from selenium import webdriver

from Utils.configreader import url, driver_path, browser


class WebDriverFactory():

    def __init__(self, browser):

        self.browser = browser

    def getWebDriverInstance(self):

        baseurl = url['OH_url']
        if self.browser == browser['INTERNET']:
            driver = webdriver.Ie(executable_path=driver_path['ie_driver'])
        elif self.browser == browser['EDGE']:
            driver = webdriver.Edge(executable_path=driver_path['edge_driver'])
        elif self.browser == browser['SAFARI']:
            driver = webdriver.Safari(executable_path=driver_path['safari_driver'])
        elif self.browser == browser['FIREFOX']:
            driver = webdriver.Firefox(executable_path=driver_path['firefox_driver'])
        elif self.browser == browser['CHROME']:
            driver = webdriver.Chrome(executable_path=driver_path['chrome_driver'])
        else:
            driver = webdriver.Chrome(executable_path=driver_path['chrome_driver'])
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseurl)
        return driver
