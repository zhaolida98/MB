import time

from selenium import webdriver


class A():

    def test(self):
        driver = webdriver.Chrome(executable_path="/Users/it000621/PycharmProjects/MB/driver/chromedriver 2")
        driver.maximize_window()
        driver.get("http://10.52.124.26:3031")
        driver.find_element_by_xpath(
            "//body//div[@class='login-wrapper login-wrapper-modal']//div[@class='login-wrapper " \
            "login-wrapper-modal']//div[1]//div[2]").click()
        driver.find_element_by_xpath("//form[@id='datashop-login-form']//input[@name='email']").send_keys(
            "himanshu.verma@innovaccer.com")
        driver.find_element_by_xpath("//form[@id='datashop-login-form']//input[@name='password']").send_keys(
            "Innovaccer@123")
        driver.find_element_by_xpath(
            "//form[@id='datashop-login-form']//button[contains(text(),'Sign in to continue')]").click()
        time.sleep(5)
        print("title of the page is", driver.title)


a = A()
a.test()
