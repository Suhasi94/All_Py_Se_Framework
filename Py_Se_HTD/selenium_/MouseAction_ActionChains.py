# To do lower level operations will be using ActionChains

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys  # key operation
import time
path = r"../drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

"""
driver.get("https://www.meesho.com/")
driver.maximize_window()

women_ethnic = driver.find_element("xpath","//span[text()='Women Ethnic']")
##### to hover around
ac_obj = ActionChains(driver)
ac_obj.move_to_element(women_ethnic).perform()

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

#####simulating keys

ac_obj.key_down(Keys.CONTROL).send_keys("A").key_up(Keys.CONTROL).perform()

"""
####### drag and drop -- url = "https://crossbrowsertesting.github.io/drag-and-drop.html"
"""
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
#### monster job,jobskill,python jobs

driver.get("https://www.monsterindia.com/")
driver.maximize_window()

ac_obj = ActionChains(driver)

job_ = driver.find_element_by_id("130")
ac_obj.move_to_element(job_).perform()
time.sleep(2)

job_skill = driver.find_element("xpath","//a[text()='Jobs by Skills']")
ac_obj.move_to_element(job_skill).perform()
time.sleep(2)

python_job = driver.find_element_by_xpath("//a[@href='https://www.monsterindia.com/search/python-jobs']")
ac_obj.move_to_element(python_job).perform()
time.sleep(2)
python_job.click()



