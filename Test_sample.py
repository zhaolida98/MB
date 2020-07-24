import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(options=chrome_options,executable_path="/Users/it000621/PycharmProjects/MB/driver/chromedriver 2")
_login_link = "//body//div[@class='login-wrapper login-wrapper-modal']//div[@class='login-wrapper " \
                  "login-wrapper-modal']//div[1]//div[2]"
_email_field = "//form[@id='datashop-login-form']//input[@name='email']"
_password_field = "//form[@id='datashop-login-form']//input[@name='password']"
_submit_link = "//form[@id='datashop-login-form']//button[contains(text(),'Sign in to continue')]"
_successful_login = "//div[@class='view-container']//p[@class='email']"
_failed_login = "//div[@class='login-error-alert alert callout']"
_analytics_link_xpath = "//a[contains(text(),'Analytics')]"
_measure_builder_xpath = "//a[contains(text(),'Measure Builder')]"
_value_set = "//a[contains(text(),'Value Sets')]"
_search_measure_xpath = "//input[@id='search']"
_measure_count_xpath = "//span[@class='label count ng-binding']"
_three_dots_xpath = "//tr[1]//td[7]//span[1]//i[1]"
_no_measure_text = "//h4[@class='title']"
_searched_measure_xpath = "//a[contains(text(),'Test_001')]"
_edit_measure_detail_xpath = "//button[@id='meta-edit']"
_save_edit_measure_detail_xpath = "//button[@id='new-measure-modal-save']"
_measure_count_xpath = "//span[@class='label count ng-binding']"

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://10.52.124.26:3031")
driver.find_element_by_xpath(_login_link).click()
driver.find_element_by_xpath(_email_field).send_keys("himanshu.verma@innovaccer.com")
driver.find_element_by_xpath(_password_field).send_keys("Innovaccer@123")
driver.find_element_by_xpath(_submit_link).click()
s1= driver.title
print(s1)
if s1 == "Innovaccer":
    print("Test pass")
else:
    print("Test Failed")

time.sleep(3)
driver.find_element_by_xpath(_analytics_link_xpath).click()
driver.find_element_by_xpath(_measure_builder_xpath).click()
time.sleep(4)
print("test has been reached")
s1 = driver.find_element_by_xpath(_measure_count_xpath).text
print(s1)
# driver.find_element_by_xpath(_search_measure_xpath).send_keys("Test_001")
# driver.find_element_by_xpath(_searched_measure_xpath).click()
# driver.find_element_by_xpath(_edit_measure_detail_xpath).click()
# time.sleep(2)
# driver.find_element_by_xpath(_save_edit_measure_detail_xpath).click()
# measure_update_text = driver.find_element_by_xpath("//div[@class='notifications']").text
# print(measure_update_text)
#assert measure_update_text == "Measure successfully updated"



