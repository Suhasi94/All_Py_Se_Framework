### Explicit wait ###
# 1. i need use - WebDriverWait Class
# 2. i need use expected_conditions - module

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
"""
url = "file:///C:/Users/User/OneDrive/Desktop/selenium_/progressbar%20(1).html"

driver = webdriver.Chrome(executable_path=path)
driver.get(url)
driver.find_element_by_xpath('//button[text()="Click Me"]').click()
wait_ = WebDriverWait(driver,30)
wait_.until(EC.visibility_of_element_located(("xpath",'//div[text()="100%"]')))
driver.find_element_by_xpath('//button[text()="Click Me"]').click()
"""
#CREATE A FUNC that checks both visibility as well as enability
driver = webdriver.Chrome(executable_path=path)
url1 = "file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html"
driver.get(url1)
driver.maximize_window()

ele = driver.find_element("id","first_name")
print(ele.is_enabled())

locator = ("id","first_name")

def is_visible_enabled(locator):
    def wrapper(driver):
        try:
            displayed = driver.find_element(*locator).is_displayed()
            enabled = driver.find_element(*locator).is_enabled()
        except :
            return False
        else:
            return displayed and enabled
    return wrapper




wait_ = WebDriverWait(driver,30)
wait_.until(is_visible_enabled(("id","first_name")))









