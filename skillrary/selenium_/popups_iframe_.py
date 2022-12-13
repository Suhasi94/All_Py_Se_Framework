from selenium import webdriver
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)

## Javascript Popups
"""
url = "https://demowebshop.tricentis.com/"
driver.get(url)
driver.find_element_by_xpath('//input[@type="submit"]').click()
alert_obj = driver.switch_to.alert
print(alert_obj.text)
alert_obj.accept() #yes,ok
#alert_obj.dismiss() # cancel,no
driver.find_element_by_link_text("Register").click()

"""
########## file upload pop ups


"""
url = "file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html"
driver.get(url)
#f_path = "upload file path
driver.find_element_by_id("resume").send_keys(f_path)
"""
######iframe - inlineframe

driver.get("file:///C:/Users/User/OneDrive/Desktop/selenium_/iframe%20(1).html")
#to switch to multiple frame
#1.indexing
#2.id,name = value
#3. web element
driver.implicitly_wait(30)
fr = driver.find_element_by_name("frame1")
driver.switch_to.frame(fr)
driver.find_element_by_id("small-searchterms").send_keys("book")
#switching back to parent/main frame
driver.switch_to.default_content()
#only after switching to main frame you can access the webelement of u 2frame
f1 = driver.find_element_by_id("FR2")
driver.switch_to.frame(f1)

driver.find_element_by_id("search_form").click()


















