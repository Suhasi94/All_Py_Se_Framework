from selenium import webdriver
import time

path = r"../drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("file:///C:/Users/User/OneDrive/Desktop/selenium_/iframe%20(1).html")
driver.maximize_window()

# switch to the iframe
#switching using index
#driver.switch_to.frame(0)

#switching using  id,name attribute value
#driver.switch_to.frame("frame1")  # name value
#driver.switch_to.frame("FR1") # id value

# locate the iframe webelement

ele = driver.find_element("xpath","//iframe[@name='frame1']")

#switch to the frame using iframe webelement
driver.switch_to.frame(ele)

driver.find_element_by_name("q").send_keys("books")
### to switch to iframe2,1st switch back the control to parent frame
driver.switch_to.default_content()
# switch to iframe2 # using name attribute value
driver.switch_to.frame("frame2")
time.sleep(2)
driver.find_element_by_id("search_form").send_keys("cars")






