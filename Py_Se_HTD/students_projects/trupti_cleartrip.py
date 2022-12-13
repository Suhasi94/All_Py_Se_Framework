from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#driver= webdriver.Chrome(ChromeDriverManager().install())
path = r"../drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
import time
################################################################33
from selenium.webdriver.common.action_chains import ActionChains
###################################################
from selenium.webdriver.common.keys import Keys
################################################################
from selenium.webdriver.support.select import Select
#########################################################################
driver.get("https://www.cleartrip.com/flights")
driver.maximize_window()
driver.implicitly_wait(60)
time.sleep(2)
driver.find_element_by_xpath("//div[@class='px-1   flex flex-middle nmx-1 pb-1']").click()
time.sleep(5)
#Where From
arrival=driver.find_element_by_xpath("//input[@placeholder='Where from?']")
arrival.click()
arrival.send_keys("BLR")
time.sleep(4)
city_dept=driver.find_elements_by_xpath("//div[@class='mr-4']")
for city in city_dept:
    city.click()
    break
time.sleep(3)
#Where to
arrival=driver.find_element_by_xpath("//input[@placeholder='Where to?']")
arrival.click()
arrival.send_keys("BOM")
time.sleep(4)
city_dept=driver.find_elements_by_xpath("//li[@class='m-1']")
for city in city_dept:
    city.click()
    break
time.sleep(3)
#date
driver.find_element_by_xpath("//div[@class='fs-4 fw-500 c-inherit flex flex-nowrap ml-4']").click()
driver.find_element_by_xpath("//div[text()='December 2022']/../..//div[text()='5']").click()
time.sleep(2)
driver.find_element_by_xpath("//div[text()='Return']").click()
driver.find_element_by_xpath("//div[text()='December 2022']/../..//div[text()='8']").click()
time.sleep(2)
#Search
driver.find_element_by_xpath("//span[text()='Search flights']").click()
time.sleep(2)
#Stps
driver.find_element_by_xpath("//p[text()='1 stop']").click()
# Departure time from Source
driver.find_element_by_xpath("(//span[@class='checkbox__mark bs-border bc-neutral-500 bw-1 ba'])[4]").click()
# Departure time from Destination
#driver.find_element_by_xpath("(//span[@class='checkbox__mark bs-border bc-neutral-500 bw-1 ba'])[11]").click()
driver.find_element("xpath",'(//p[text()="Afternoon"])[2]/../../..//input').click()

#book
driver.find_element_by_xpath("//button[text()='Book']").click()
time.sleep(2)

#Window Handles
handles= driver.window_handles
print(handles)
driver.switch_to.window(handles[1])
time.sleep(2)
#Review your Itinerary

itinerary=driver.find_element_by_xpath("//li[text()='Standard airline cancellation and date change penalties apply']")
itinerary.click()
time.sleep(2)
driver.find_element_by_xpath("//button[text()='Continue']").click()
time.sleep(3)
#Add Contact Details
driver.find_element_by_xpath("//input[@placeholder='Mobile number']").send_keys(7768871872)
time.sleep(2)
driver.find_element_by_xpath("//input[@placeholder='Email address']").send_keys("giradkartrupti4@gmail.com")
time.sleep(2)
driver.find_element_by_xpath("(//button[text()='Continue'])[2]").click()
time.sleep(2)
#Add travellers Details
driver.find_element_by_xpath("//input[@placeholder='First name']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@placeholder='Last name']").click()
time.sleep(2)
driver.find_element_by_xpath("//button[text()='Continue to payment']").click()