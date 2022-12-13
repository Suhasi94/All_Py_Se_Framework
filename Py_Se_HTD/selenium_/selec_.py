from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
path = r"../drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
#driver.get("file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html")
#driver.maximize_window()
#time.sleep(2)

## Handling single select list box

#locating the standard list box


#ele = driver.find_element_by_id("standard_cars")

# creating an object for select class
#sel_obj = Select(ele)
"""
time.sleep(2)
#selecting the option by visible text
sel_obj.select_by_visible_text("Audi")
time.sleep(2)
# selecting the option by value
sel_obj.select_by_value("bmw")
time.sleep(2)
## selecting the option by index
sel_obj.select_by_index(4)

#getting all the options in the listbox

all_options = sel_obj.options
#print(all_options)

for option in all_options:

    sel_obj.select_by_visible_text(option.text)
    time.sleep(2)

for index in range(len(all_options)):
    sel_obj.select_by_index(index)
    time.sleep(1)

for index,value in enumerate(all_options):
    sel_obj.select_by_index(index)
    time.sleep(1)

#print(sel_obj.is_multiple)
"""

#Handling Multi select list box

"""
ele = driver.find_element("id", "multiple_cars")
obj_ms = Select(ele)
obj_ms.select_by_visible_text("Audi")
obj_ms.select_by_visible_text("Ford")
obj_ms.select_by_value("bmw")
obj_ms.select_by_index(5)
print(obj_ms.is_multiple)  # True
#print(sel_obj.is_multiple) # None


# to select all the item
option = obj_ms.options

# to get the only selected items
sel_ option = obj_ms.all_selected_options
for item in option:
    print(item.text)

# to get the first element that is selected
print(obj_ms.first_selected_option.text)

# deselect - deselect can be done same as select through visible text,index,value
#deselecting using index
obj_ms.deselect_by_index(1)
#obj_ms.deselect_by_visible_text("Mini") - even if the item is not selected & u try to deselect
                                           # it will throw the error
# deselecting all
obj_ms.deselect_all()   #u can deselect all but cannot select all at a time

"""

### facebook register page

driver.get("https://www.facebook.com/signup")
driver.maximize_window()
driver.find_element_by_name("firstname").send_keys("Suhasini")
driver.find_element_by_name("lastname").send_keys("Kattimani")
driver.find_element_by_name("reg_email__").send_keys("suhasi@gmail.com")
driver.find_element_by_id("password_step_input").send_keys("Xyz123a@13")
day_ = driver.find_element_by_id("day")
sel_obj_day = Select(day_)
sel_obj_day.select_by_visible_text("10")
month_ = driver.find_element_by_id("month")
sel_obj_month = Select(month_)
sel_obj_month.select_by_value("7")
year_ = driver.find_element_by_id("year")
sel_obj_year = Select(year_)
sel_obj_year.select_by_index(11)
driver.find_element("xpath","//label[text()='Female']/..//input[@type='radio']").click()















