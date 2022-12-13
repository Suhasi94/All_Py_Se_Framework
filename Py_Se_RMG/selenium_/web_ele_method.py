from selenium import webdriver
#from selenium.webdriver.common.by import By

import time
path = r"C:\Users\User\PycharmProjects\pythonProject2\Py_Se_RMG\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()
time.sleep(2)
#driver.find_element_by_id("username")

#from selenium.webdriver.common.by import By
#driver.find_element(By.ID,"username")
driver.find_element("id","username")