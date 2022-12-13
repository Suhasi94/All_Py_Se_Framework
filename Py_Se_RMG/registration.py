from selenium import webdriver
from selenium.webdriver.support.select import Select
from lib import SeleniumWrapper
import time
path = r"./drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

sw = SeleniumWrapper(driver)

# def enter_text(loctype,locvalue,value):
#     print("calling enter text")
#     driver.find_element(loctype,locvalue).clear()
#     driver.find_element(loctype,locvalue).send_keys(value)
#
# def click_element(loctype,locvalue):
#     print("calling click element")
#     driver.find_element(loctype,locvalue).click()
#
# def select_item(loctype,locvalue,item):
#     element = driver.find_element(loctype,locvalue)
#     s = Select(element)
#     if isinstance(item,str):
#         s.select_by_visible_text(item)
#     else:
#         s.select_by_index(item)
#
# def select_items(loctype,locvalue,items):
#     for item in items:
#         select_item(loctype,locvalue,item)

#select_items("id","multiple_cars",["Audi","Mercedes","Toyota"])

#driver.find_element("link text", "Register").click()
sw.click_element(("link text", "Register"))
#driver.find_element("id", "gender-female").click()
sw.click_element(("id", "gender-female"))
#driver.find_element("name", "FirstName").send_keys("Suhasi")
sw.enter_text(("name","FirstName"),value="Suhasi")
#driver.find_element("name","LastName").send_keys("Katti")
sw.enter_text(("name","LastName"),value="Katti")
#driver.find_element("name","Email").send_keys("suhasini007kattimani@gmail.com")
sw.enter_text(("name","Email"),value="suhasini007kattimani@gmail.com")
#driver.find_element("id","Password").send_keys("123456")
sw.enter_text(("id","Password"),value="123456")

#driver.find_element("id","ConfirmPassword").send_keys("123456")
sw.enter_text(("id","ConfirmPassword"),value="123456")
#driver.find_element("xpath","//input[@value='Register']").click()
sw.click_element(("xpath","//input[@value='Register']"))