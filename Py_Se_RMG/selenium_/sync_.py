from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException

path = r"C:\Users\User\PycharmProjects\pythonProject2\Py_Se_RMG\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("file:///C:/Users/User/OneDrive/Desktop/selenium_/loading%20(1).html")
driver.maximize_window()


#unconditional synchronization - time.sleep()
#time.sleep(20)
#driver.find_element("name","fname").send_keys("Suha")
#driver.find_element("name","lname").send_keys("Katti")


# conditional synchronization - implicit wait and explicit wait
#implicit wait - internally , automatically

#driver.implicitly_wait(30)
#start = time.time()
#driver.find_element("name","fname").send_keys("Suha")
#driver.find_element("name","lname").send_keys("Katti")
#end = time.time()
#print(end-start)


#2. explicit wait(webdriverwait)
from selenium.webdriver.support.ui import WebDriverWait #class
from selenium.webdriver.support import expected_conditions as EC #module
#fluent wait
wait_ = WebDriverWait(driver,timeout=2,poll_frequency=1,ignored_exceptions=[NoSuchElementException])
#element = driver.find_element("name","fname")
# wenever the element is already present in the dom only den use visiblity_of
#wait_.until(EC.visibility_of(element))
#whenever u want to locate the ele on the dom,it raises TOE error wen not found within the time

locator = "name","fname" #it will taken as tuple
ele = wait_.until(EC.visibility_of_element_located(locator))
print(ele)
ele.send_keys("suha")










