import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=options, executable_path="/Users/it000621/PycharmProjects/MB/driver/chromedriver 2")

driver.get("http://10.52.124.26:3031")
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
#driver.find_element_by_xpath("//a[contains(text(),'Measure Builder')]").click()
driver.find_element_by_xpath("//a[contains(text(),'Value Sets')]").click()
driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys("Test")
driver.find_element_by_xpath("//tr[1]//td[1]").click()
# time.sleep(2)
# driver.find_element_by_xpath("//span[@class='button primary' and @data-test='createNewMeasure-button']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//input[@id='name']").send_keys("First_measure")
# driver.find_element_by_xpath("//input[@placeholder='Program' and @type='search']").send_keys("Custom")
# time.sleep(2)
# driver.find_element_by_xpath("//input[@placeholder='Type' and @data-test='modal__newMeasure-type']").send_keys("Custom")
# time.sleep(2)
# print(driver.title)
# driver.find_element_by_xpath("//input[@placeholder='Category' and @type='search']").send_keys("Quality")
# time.sleep(2)
# driver.find_element_by_xpath("//input[@placeholder='Product Lines' and @type='search']").send_keys("Conifer")
# time.sleep(2)
# driver.find_element_by_xpath("//button[@id='new-measure-modal-add']").click()
# time.sleep(2)
# print(driver.title)


