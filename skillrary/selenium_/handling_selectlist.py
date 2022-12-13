from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)
url1 = r"C:\Users\User\OneDrive\Desktop\selenium_\demo (1).html"
driver.get(url1)
element = driver.find_element_by_id("standard_cars")
#creating an object for select class
s_obj=Select(element)
s_obj.select_by_visible_text("Audi")
time.sleep(2)
s_obj.select_by_visible_text("BMW")
time.sleep(2)
s_obj.select_by_value("jgr")
time.sleep(2)
s_obj.select_by_value("merc")

s_obj.select_by_index(1)


#s_obj.deselect_by_value("jgr") #multiselect cars
#s_obj.deselect_all()

all_options = s_obj.options
for element in all_options:
    print(element.text)

for option in all_options:
    s_obj.select_by_visible_text(option.text)
    time.sleep(2)















