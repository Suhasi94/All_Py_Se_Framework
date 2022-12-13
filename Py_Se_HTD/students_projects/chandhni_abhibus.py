from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
path = r"../drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://www.abhibus.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//a[@class='nav-link bg-gray  rounded-pill px-4 py-1']").click()
driver.implicitly_wait(10)
# for source
source = driver.find_element_by_xpath('//div[@class="source"]//div[@class="label-container"]')
source.click()
from_ = driver.find_element("xpath", '//input[@placeholder="Enter from"]')
from_.send_keys("pune")
driver.find_element("xpath", '//li[@id="source-item-4"]').click()
# for destination
destn_ = driver.find_element_by_xpath('//div[@class="destination"]//div[@class="label-container"]')
destn_.click()
to_ = driver.find_element("xpath",'//input[@placeholder="Enter to"]')
to_.send_keys("bangalore")
driver.find_element("xpath", '//li[@id="destination-item-3"]').click()
######
driver.find_element("xpath","//span[text()='SEARCH']").click()
time.sleep(2)
driver.find_element_by_xpath("//i[text()='calendar_today']").click()
time.sleep(3)
driver.find_element_by_xpath('//button[@class="MuiButtonBase-root MuiIconButton-root MuiPickersCalendarHeader-iconButton"]').click()
time.sleep(2)
driver.find_element_by_xpath("//p[text()='8']").click()
time.sleep(2)
driver.find_element_by_xpath("(//span[text()='SL'])[1]").click()
time.sleep(2)
# driver.find_element_by_xpath("//input[@id='mobile-number']").send_keys('7993712206')
# time.sleep(5)
# driver.find_element_by_xpath("//span[@class='MuiButton-label']").click()
# time.sleep(30)
# driver.find_element_by_xpath("//span[@class='MuiButton-label']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//div[@class='availability']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//div[@class='book-btn p']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//input[@id='name']").sendkeys("sravanivadithya")
# time.sleep(2)
# driver.find_element_by_xpath("//span[text()='PROCEED']").click()
# time.sleep(2)
# # driver.find_element_by_xpath("(//span[text()='3A'])[1]").click()