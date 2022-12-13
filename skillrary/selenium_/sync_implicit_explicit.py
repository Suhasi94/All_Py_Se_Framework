# synchronization
# 1. unconditional - time.sleep(n)
# 2. conditional 1. impicit wait 2.expicit wait

# implicit wait   - driver.implicitly_wait(n)
from selenium import webdriver
import time
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
url = "file:///C:/Users/User/OneDrive/Desktop/selenium_/loading%20(1).html"
driver.get(url)
driver.implicitly_wait(30)
start = time.time()
driver.find_element_by_name("fname").send_keys("suhasini")
end = time.time()
driver.find_element_by_name("lname").click()
print(end-start)

url1 = "file:///C:/Users/User/OneDrive/Desktop/selenium_/progressbar%20(1).html"
driver.get(url1)
driver.implicitly_wait(40)
driver.find_element_by_xpath('//button[text()="Click Me"]').click()

driver.find_element_by_xpath('//div[text()="100%"]')
driver.find_element_by_xpath('//button[text()="Click Me"]').click()












