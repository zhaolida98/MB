import time

import random as rand
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(options=chrome_options,
                          executable_path="/Users/it000621/PycharmProjects/MB/driver/chromedriver 2")
_login_link = "//div[@id='app']//following::div[45]//*[text()='Innovaccer']"
_email_field = "//form[@id='datashop-login-form']//input[@name='email']"
_password_field = "//form[@id='datashop-login-form']//input[@name='password']"
_submit_link = "//form[@id='datashop-login-form']//button[contains(text(),'Sign in to continue')]"
_successful_login = "//div[@class='view-container']//p[@class='email']"
_failed_login = "//div[@class='login-error-alert alert callout']"
_analytics_link_xpath = "//span[contains(text(),'Analytics')]"
_measure_builder_xpath = "//a[contains(text(),'Measure Builder')]"
_value_set = "//span[contains(text(),'Value Sets')]"
_search_measure_xpath = "//input[@id='search']"
_measure_count_xpath = "//span[@class='label count ng-binding']"
_three_dots_xpath = "//tr[1]//td[7]//span[1]//i[1]"
_no_measure_text = "//h4[@class='title']"
_searched_measure_xpath = "//a[contains(text(),'Test_001')]"
_edit_measure_detail_xpath = "//button[@id='meta-edit']"
_save_edit_measure_detail_xpath = "//button[@id='new-measure-modal-save']"
_measure_count_xpath = "//span[@class='label count ng-binding']"
_search_valueset = "//input[@placeholder='Search']"
# _searched_valueset = "//td[contains(text(),'Copy of HPV Tests Value Set')]"
_searchedvalueset = "//table/tbody/tr[1]/td[1]"
_edit_valueset_detail = "//div[@class='sc-jDwBTQ jAsbbw']//button[@class='sc-ifAKCX gFckEz'][contains(text()," \
                        "'Edit')]"
_edit_value_name = "//input[@placeholder='Name']"
_save_valueset = "//div[@class='sc-caSCKo gujKlR']//button[text()='Save']"
_cancel_valueset = "//div[@class='sc-caSCKo gujKlR']//button[text()='Cancel']"
_new_valueset = "//button[contains(text(),'New Value Set')]"
_new_valueset_name = "//input[@placeholder='Name']"
_drop_down_xpath = "//div[@class='sc-jWBwVP hFBhID']//following::div[5]//*"
_drop_down_values = "//div[@class='sc-jWBwVP hFBhID']//following::div[7]//li[1]"

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sanitas-staging.innovaccer.com")
driver.find_element_by_xpath(_login_link).click()
driver.find_element_by_xpath(_email_field).send_keys("himanshu.verma@innovaccer.com")
driver.find_element_by_xpath(_password_field).send_keys("Test@1234")
driver.find_element_by_xpath(_submit_link).click()
s1 = driver.title
print(s1)
if s1 == "Sanitas-stage":
    print("Test pass")
else:
    print("Test Failed")

time.sleep(3)
driver.find_element_by_xpath(_analytics_link_xpath).click()
time.sleep(3)
driver.find_element_by_xpath(_value_set).click()
time.sleep(10)
driver.find_element_by_xpath(_new_valueset).click()
time.sleep(3)

value_set_name = str(rand.randint(100,100000))
print(value_set_name)

driver.find_element_by_xpath(_new_valueset_name).send_keys("Test_Innovaccer"+value_set_name)
time.sleep(8)
driver.find_element_by_xpath(_drop_down_xpath).click()
valueset_text = "Medication"
result_set = driver.find_element_by_xpath("//div[@class='sc-jWBwVP hFBhID']//following::div[7]/ul")
Options = result_set.find_elements_by_tag_name("li")

for option in Options:
    if option.text == valueset_text:
        option.click()
        break;
    #print(option.text)

add_button = driver.find_element_by_xpath("//div[@class='sc-caSCKo gujKlR']//button[text()='Add']")
add_button.click()

# selectname = driver.find_element_by_xpath(_drop_down_values)
# driver.execute_script("arguments[0].click();", selectname)

# driver.find_element_by_xpath(_drop_down_values).send_keys("Procedure")
# elements = driver.find_elements_by_xpath(_drop_down_values)

# for e in elements:
#     print(e.text)
# driver.find_element_by_xpath(_drop_down_xpath).send_keys("Procedure")
time.sleep(15)
# driver.find_element_by_xpath(_search_valueset).send_keys("Test")
# time.sleep(5)
# searchedname = driver.find_element_by_xpath(_searchedvalueset)
# driver.execute_script("arguments[0].click();", searchedname)
# try:
#     driver.find_element_by_xpath(_searchedvalueset).click()
# except ElementClickInterceptedException:
#     time.sleep(2)
#     driver.find_element_by_xpath(_searchedvalueset).click()

time.sleep(4)
s2 = driver.title
print(s2)


# s1 = driver.find_element_by_xpath(_measure_count_xpath).text
# print(s1)

# driver.find_element_by_xpath(_search_measure_xpath).send_keys("Test_001")
# driver.find_element_by_xpath(_searched_measure_xpath).click()
# driver.find_element_by_xpath(_edit_measure_detail_xpath).click()
# time.sleep(2)
# driver.find_element_by_xpath(_save_edit_measure_detail_xpath).click()
# measure_update_text = driver.find_element_by_xpath("//div[@class='notifications']").text
# print(measure_update_text)
#assert measure_update_text == "Measure successfully updated"
# def verifyTextContains(self, actualText, expectedText, locator, locatorType="id"):
#     """
#     Verify actual text contains expected text string
#
#     Parameters:
#         expectedList: Expected Text
#         actualList: Actual Text
#     """
#     self.log.info("Actual Text From Application Web UI --> :: " + actualText + locator + locatorType)
#     self.log.info("Expected Text From Application Web UI --> :: " + expectedText + locator + locatorType)
#     if expectedText.lower() in actualText.lower():
#         self.log.info("### VERIFICATION CONTAINS !!!")
#         return True
#     else:
#         self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
#         return False


