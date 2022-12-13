import pytest
from selenium import webdriver
import time
path = r"C:\Users\User\PycharmProjects\pythonProject2\Py_Se_RMG\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://demowebshop.tricentis.com/")
path = r"C:\Users\User\PycharmProjects\pythonProject2\Py_Se_RMG\screenshots"#it will create outside
path1 = r"C:\Users\User\PycharmProjects\pythonProject2\Py_Se_RMG\screenshots\\"
#// is mandatory  to take the screenshot in perticular directory
driver.save_screenshot(path1 + "screenshot1.png")



