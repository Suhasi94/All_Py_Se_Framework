from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
path = r"../drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://www.cleartrip.com/")
driver.maximize_window()
driver.implicitly_wait(30)
time.sleep(2)

#click crossmark
driver.find_element("xpath", "//div[@class='px-1   flex flex-middle nmx-1 pb-1']").click()
time.sleep(2)

#click hotel
driver.find_element("xpath", "//a[@href='/hotels']").click()
time.sleep(2)

#search goa
driver.find_element("xpath", "//div[@class='h-13 flex-1 p-relative']").click()
goa=driver.find_element("xpath", "//li[@class='ls-reset br-4 w-100p  px-3 dropdown__item dropdown-new__item hover:"
                                 "bg-secondary-500 hover:c-white c-pointer c-neutral-900 flex flex-middle dropdown-new__item-stroke']")
ac_obj = ActionChains(driver)
ac_obj.move_to_element(goa).perform()
ac_obj.click(goa).perform()

#dates
driver.find_element("xpath", "//div[@class='c-inherit flex flex-1 flex-nowrap fs-4 fw-500']").click()
driver.find_element("xpath", "//div[text()='December 2022']/../..//div[text()='8']").click()

driver.find_element("xpath", "//div[@class='flex flex-middle divider-wrapper']").click()
driver.find_element("xpath", "//div[text()='December 2022']/../..//div[text()='10']").click()

#dropdown
driver.find_element("xpath", "//span[@class='fw-500 fs-4 ml-4']").click()
driver.find_element("xpath", "//li[@class='ls-reset br-4 w-100p  px-3 dropdown__item dropdown-new__item "
                             "hover:bg-secondary-500 hover:c-white c-pointer c-neutral-900 fs-4 lh-24 fw-500 "
                             "p-3']").click()
driver.find_element("xpath", "//div[text()='Search hotels']").click()

# #view button
# driver.find_element("xpath", "(//button[text()='View details'])[1]").click()
# time.sleep(20)
#
# #window switch
# handles = driver.window_handles
# print(handles)
# print(handles[1])
# time.sleep(10)
# driver.switch_to.window(handles[1])
#
# #select button
# driver.find_element_by_xpath("//button[text()='Select room']").click()