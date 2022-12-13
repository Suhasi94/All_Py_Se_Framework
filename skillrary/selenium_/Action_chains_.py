from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)
### hovering around the webelement
"""
url = "https://www.meesho.com/"
driver.get(url)
ac_obj  = ActionChains(driver)
ele = driver.find_element_by_xpath('//span[text()="Women Ethnic"]')
ac_obj.move_to_element(ele).perform()
"""

#### double-clicking

url = "file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html"
driver.get(url)
driver.maximize_window()
ac_obj = ActionChains(driver)
button = driver.find_element_by_id("double-click")
time.sleep(2)
ac_obj.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)

ac_obj.double_click(button).perform()
ac_obj.send_keys(Keys.PAGE_UP).perform()

### drag and drop
