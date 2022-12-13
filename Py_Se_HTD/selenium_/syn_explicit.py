############ Explicit wait

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait     #EXPLICT_WAIT class - WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
path = r"../drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

### progress bar
"""
driver.get("file:///C:/Users/User/OneDrive/Desktop/selenium_/progressbar%20(1).html")
driver.maximize_window()
driver.find_element_by_xpath("//button[text()='Click Me']").click()
wait_obj = WebDriverWait(driver,30) # WebDriverWait to give explicit condition

#wait_obj.until(expected_conditions.presence_of_element_located(("xpath","//div[text()='100%']")))
#driver.find_element_by_xpath("//button[text()='Click Me']").click()

wait_obj.until(expected_conditions.visibility_of_element_located(("xpath","//div[text()='100%']")))
driver.find_element_by_xpath("//button[text()='Click Me']").click()

"""
######## create a function which should check both visibility ,enable

driver.get("file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html")
driver.maximize_window()

#ele = driver.find_element("id","first_name")
#res = ele.is_enabled()
#print(ele.is_displayed())


def is_visible_enabled(locator):
    def wrapper(driver):
        try:
            displayed = driver.find_element(*locator).is_displayed()
            enabled = driver.find_element(*locator).is_enabled()


        except:
            return False

        else:
            return displayed and enabled

    return wrapper

wait_ = WebDriverWait(driver,30)
wait_.until(is_visible_enabled(("id","first_name")))













