# Glassdoor login
# Linear code

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
path = r"../drivers/chromedriver.exe"
opt = webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")
driver=webdriver.Chrome(path,options=opt)
driver.get("https://www.glassdoor.co.in/index.htm")
driver.maximize_window()
driver.implicitly_wait(50)


# Continue with Email
#username
driver.find_element("xpath","//input[@title='Enter Email']").send_keys("kandiramya844@gmail.com")
time.sleep(1)
driver.find_element("xpath","//button[@type='submit']").click()
time.sleep(1)
#password
driver.find_element("xpath","//input[@id='inlineUserPassword']").send_keys("Ramya@123")
time.sleep(1)
#submit
driver.find_element("xpath","//button[@name='submit']").click()
time.sleep(5)
#profile
obj=driver.find_element("xpath",'(//div[@class="d-flex"])[8]')
profile=ActionChains(driver)
profile.move_to_element(obj).perform()
time.sleep(2)
#signout
driver.find_element("xpath",'(//div[@class="d-flex align-items-center py-std col header-menu-item-label"])[33]').click()


## Continue with Facebook
driver.find_element("xpath","//button[@class='facebookWhite gd-btn center ']").click()
# time.sleep(1)
# handles=driver.window_handles
# print(handles)
# driver.switch_to.window(handles[1])
#username
driver.find_element("xpath","//input[@class='inputtext _55r1 inputtext inputtext']").send_keys("ramyakandi08@gmail.com")
time.sleep(1)
#password
driver.find_element("xpath","//input[@autocomplete='current-password']").send_keys("Ramya@123")
time.sleep(1)
driver.find_element("xpath","//input[@value='Log in']").click()
time.sleep(2)