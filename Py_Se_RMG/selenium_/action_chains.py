from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#Keys constant are there so no need to create object can directly access using classname
import time
path = r"C:\Users\User\PycharmProjects\pythonProject2\Py_Se_RMG\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
"""
driver.get("https://www.meesho.com/")
driver.maximize_window()
driver.implicitly_wait(30)
ac = ActionChains(driver)
time.sleep(2)
ele = driver.find_element("xpath","//span[text()='Women Ethnic']")
ac.move_to_element(ele).perform()
time.sleep(2)
ele1 = driver.find_element("xpath","//p[text()='Cotton Sarees']")
ac1 = ActionChains(driver)
ac1.move_to_element(ele1).perform()
ele1.click()
"""

"""
driver.get("file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html")
driver.maximize_window()

ele_dd = driver.find_element_by_id("double-click")
########### to double click
ac_obj = ActionChains(driver)
time.sleep(2)
ac_obj.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)
ac_obj.double_click(ele_dd).perform()
time.sleep(2)
ac_obj.send_keys(Keys.PAGE_UP).perform()

####### drag and drop -- url = "https://crossbrowsertesting.github.io/drag-and-drop.html"
driver.get("https://crossbrowsertesting.github.io/drag-and-drop.html")
driver.maximize_window()
time.sleep(2)
source = driver.find_element_by_id("draggable")
target = driver.find_element_by_id("droppable")
ac_obj = ActionChains(driver)
ac_obj.drag_and_drop(source,target).perform()
"""

### context_click

"""
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()
reg = driver.find_element_by_xpath("//a[text()='Register']")
ac_obj = ActionChains(driver)
time.sleep(2)

ac_obj.context_click(reg).perform()
time.sleep(2)
ac_obj.send_keys(Keys.TAB).perform()
time.sleep(2)
ac_obj.send_keys(Keys.ENTER).perform()
"""

"""
#we dont have option scrolling option in selenium 3 but in selenium 4 it is there
###simulating keys
driver.get("file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html")
driver.maximize_window()
ac_obj = ActionChains(driver)
time.sleep(2)
#ac_obj.send_keys(Keys.PAGE_DOWN).perform()
#ac_obj.send_keys(Keys.ARROW_DOWN).perform()
#ac_obj.key_down(Keys.CONTROL).perform() # key_down will press the keys
#ac_obj.send_keys("A").perform()
#ac_obj.key_up(Keys.CONTROL).perform() #key_up will release the keys
ac_obj.key_down(Keys.CONTROL).send_keys("A").key_up(Keys.CONTROL).perform()
"""