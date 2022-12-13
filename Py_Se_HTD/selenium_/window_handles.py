
from selenium import webdriver
import time
path = r"../drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(30)
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()
driver.find_element_by_link_text("Twitter").click()
handles = driver.window_handles
print(handles)
driver.switch_to.window(handles[1])
driver.find_element("xpath","//span[text()='Follow']").click()

