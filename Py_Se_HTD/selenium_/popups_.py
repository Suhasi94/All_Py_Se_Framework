from selenium import webdriver
import time
path = r"../drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(30)
"""
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()
driver.find_element_by_xpath("//input[@value='Search']").click()

# Javascript popups
# switch to the alert
alert_obj = driver.switch_to.alert

# accept it or dissmiss
# alert_obj.accept() -- ok ,accept ,alert_obj.dismiss() -- cancel,dismiss
alert_obj.accept()

driver.find_element_by_link_text("Log in").click()
"""
driver.get("file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html")
driver.maximize_window()
driver.find_element_by_xpath("//button[text()='Delete']").click()
# switch to the alert
time.sleep(2)
alert_obj = driver.switch_to.alert
time.sleep(2)
alert_obj.dismiss()

### File upload popups/hidden division/model windowpop
file_path = r"C:\Users\User\Downloads\Suhasini.resume.docx"
driver.find_element_by_id("resume").send_keys(file_path)

