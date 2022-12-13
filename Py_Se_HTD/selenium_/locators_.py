from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

path = r"../drivers/chromedriver.exe"

driver_obj = webdriver.Chrome(ChromeDriverManager().install())

driver_obj.get("https://demowebshop.tricentis.com/")
time.sleep(2)
driver_obj.maximize_window()
#time.sleep(2)
#driver_obj.minimize_window()
#time.sleep(2)
#driver_obj.maximize_window()
#time.sleep(2)
#driver_obj.refresh()
#print(driver_obj.title)
#print(driver_obj.current_url)
#driver_obj.close()
#driver_obj.quit()


### locating the webelement using id locator
#driver_obj.find_element_by_id("small-searchterms").send_keys("books")

### using name locator
#driver_obj.find_element_by_name("q").send_keys("books")

###using class name locator
#driver_obj.find_element_by_class_name("button-1.search-box-button").click()

###using link_text
#driver_obj.find_element("link text","Register").click()

###using partial_link_text
#driver_obj.find_element("partial link text","Reg").click()

###### using css selector
#driver_obj.find_element("css selector",'input[value="Search store"]').send_keys("books")

####using tag name
#links = driver_obj.find_elements_by_tag_name("a")
#print(links)
#for lin in links:
#   print(lin.text)

### using xpath
#driver_obj.find_element("xpath",'//a[@class="ico-register"]').click()
 ## xpath using text()

#driver_obj.find_element("xpath", "//a[text()='Log in']").click()


#  url = "https://demo.actitime.com/login.do"

#### login





