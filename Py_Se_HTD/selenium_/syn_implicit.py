# Implicit wait - it is applied only to find_element,find_elements
    # - u cannot give the condition,once defined will be applicable to all find_element&elements

from selenium import webdriver
import time
path = r"../drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(30)

"""
driver.get("file:///C:/Users/User/OneDrive/Desktop/selenium_/loading%20(1).html")
driver.maximize_window()

start = time.time()
driver.find_element_by_name("fname").send_keys("Suha")
end = time.time()
print(end-start)

"""
#########progress bar using implicit wait
driver.get("file:///C:/Users/User/OneDrive/Desktop/selenium_/progressbar%20(1).html")
driver.maximize_window()
driver.find_element_by_xpath("//button[text()='Click Me']").click()
driver.find_element("xpath","//div[text()='100%']")
driver.find_element_by_xpath("//button[text()='Click Me']").click()

