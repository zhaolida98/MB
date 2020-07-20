import time

from selenium import webdriver

from utilities.configreader import driver_path

driver = webdriver.Chrome(executable_path=driver_path['chrome_driver'])
#driver.get("https://www.orange.com/en/home")

driver.get("http://10.52.124.26:3031")
driver.maximize_window()
time.sleep(10)
driver.find_element_by_xpath("//body//div[@class='login-wrapper login-wrapper-modal']//div[@class='login-wrapper " \
            "login-wrapper-modal']//div[1]//div[2]").click()
driver.find_element_by_xpath("//form[@id='datashop-login-form']//input[@name='email']").send_keys(
            "himanshu.verma@innovaccer.com")
driver.find_element_by_xpath("//form[@id='datashop-login-form']//input[@name='password']").send_keys(
            "Innovaccer@123")
driver.find_element_by_xpath(
            "//form[@id='datashop-login-form']//button[contains(text(),'Sign in to continue')]").click()
time.sleep(5)
print("title of the page is", driver.title)

driver.find_element_by_xpath("//a[contains(text(),'Analytics')]").click()
driver.find_element_by_xpath("//a[contains(text(),'Value Sets')]").click()
time.sleep(7)
print("title of the page is", driver.title)
driver.find_element_by_xpath("//input[@placeholder='Search']").clear()
driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys("Test")
time.sleep(5)
driver.find_element_by_xpath("//tr[1]//td[1]").click()
time.sleep(5)