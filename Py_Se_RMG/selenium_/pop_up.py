from selenium import webdriver
import time
path = r"C:\Users\User\PycharmProjects\pythonProject2\Py_Se_RMG\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(20)
# driver.get("https://demowebshop.tricentis.com")
# driver.maximize_window()
# # simple alert - ok,cancel
# #confirmation alert accept/ok,dismiss/cancel
# #prompt alert - sendkeys

### simple alert

# driver.find_element("css selector","input[value='Search']").click()
# alert_obj = driver.switch_to.alert  #text,send_keys(),accept(),dismiss()
# print(alert_obj.text)
# alert_obj.accept()
# driver.close()


#### confirmation alert

# driver.get("file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html")
# driver.maximize_window()
# driver.find_element_by_xpath("//button[text()='Delete']").click()
# #driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()

#authentication popup
# url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
# driver.get(url)
# driver.maximize_window()

#### file upload popup

# driver.get("https://www.monsterindia.com/")
# driver.maximize_window()
# driver.find_element("xpath","//div[contains(text(),'Upload Resume')]").click()
# path = r"C:\Users\User\Downloads\Suhasini.resume.docx"
# driver.find_element("xpath","//input[@id='file-upload']").send_keys(path)

