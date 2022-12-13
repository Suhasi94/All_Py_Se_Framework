from selenium import webdriver
import time
path = r"C:\Users\User\PycharmProjects\pythonProject2\Py_Se_RMG\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(20)
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()

###single window
"""
driver.find_element("link text","Twitter").click()
print(driver.title) #demo web shop
#returns list of all the windows opened in the sessions
handles = driver.window_handles
print(handles) #[parent_window,child_window]
#switching the driver to child window
driver.switch_to.window(handles[1])
# u will get an error as it takes time to load the ele in dom give some implicit delay
driver.find_element("xpath","//span[text()='Follow']").click()
print(driver.title)
driver.close()"""

########## multiple window

# driver.find_element("link text","Twitter").click()
# driver.find_element("link text","Facebook").click()

#list of window handles
# handles = driver.window_handles
# time.sleep(2)
# print(handles)
# time.sleep(2)
# print(driver.title)
# time.sleep(2)
# print(driver.current_window_handle)
# for handle in handles[1:]:
#     driver.switch_to.window(handle)
#     print(driver.title)
#     driver.close()
#     time.sleep(3)

#############

driver.find_element("link text","Twitter").click()
driver.find_element("link text","Facebook").click()

print(driver.title)
handles = driver.window_handles

driver.switch_to.window(handles[1])
print(driver.title)

##switching to parent window
driver.switch_to.window(handles[0])
print(driver.title)








