from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
path = r"C:\Users\User\PycharmProjects\pythonProject2\Py_Se_RMG\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
# driver.get("file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html")
# driver.maximize_window()
#single select listboxes
#list_box = driver.find_element("xpath","//select[@id='standard_cars']")
# sel_obj = Select(list_box)
# sel_obj.select_by_index(0)
# time.sleep(2)
# sel_obj.select_by_visible_text("Jaguar")
# time.sleep(2)
# sel_obj.select_by_value("nin")
# print(sel_obj.is_multiple) #returns none if not multiple else returns true
#
# #all the options in the listbox
# all_options = sel_obj.options #list of webelements of all the options
# for option in all_options:
#     print(option.text)

####################################################################################

# list_box = driver.find_element("xpath","//select[@id='multiple_cars']")
# sel_obj = Select(list_box)
# sel_obj.select_by_index(1)
# time.sleep(2)
# sel_obj.select_by_visible_text("Jaguar")
# time.sleep(2)
# sel_obj.select_by_value("nin")
# print(sel_obj.is_multiple)

#to deselect
# sel_obj.deselect_by_visible_text("Nissan")
# time.sleep(2)
# sel_obj.deselect_by_index(2)
# time.sleep(2)
# sel_obj.deselect_by_value("jgr")
#sel_obj.deselect_all()

# all_option = sel_obj.options
# for option in all_option:
#     print(option.text)

# sel_options = sel_obj.all_selected_options #list of only selected webele
#
# for option in sel_options:
#     print(option.text)
#
# print(sel_obj.first_selected_option.text)
# driver.close()

###auto suggestion list box - normal webelement method
#myntra - puma - list of puma products

driver.get("https://www.myntra.com/")
driver.maximize_window()
driver.find_element("xpath","//input[@class='desktop-searchBar']").send_keys("puma")
driver.implicitly_wait(10)
driver.find_element("xpath","//li[text()='Puma Sweatshirts']").click()