from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
path = r"C:\Users\User\PycharmProjects\pythonProject2\Py_Se_RMG\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://www.facebook.com/reg/")
driver.maximize_window()
driver.find_element("name","firstname").send_keys("Suhasini")
time.sleep(2)
driver.find_element("name","lastname").send_keys("kattimani")
time.sleep(2)
driver.find_element("name","reg_email__").send_keys("suhasini007kattimani@gmail.com")
driver.find_element("name","reg_email_confirmation__").send_keys("suhasini007kattimani@gmail.com")
time.sleep(2)
driver.find_element("name","reg_passwd__").send_keys("Suhasi@10")
time.sleep(2)
###select class

ele_day = driver.find_element("xpath","//select[@id='day']")
_day = Select(ele_day)
_day.select_by_value("10")
ele_month = driver.find_element("xpath","//select[@id='month']")
_month = Select(ele_month)
_month.select_by_visible_text("Jul")
ele_year = driver.find_element("xpath","//select[@id='year']")
_year = Select(ele_year)
_year.select_by_index(8)
driver.find_element("xpath","//label[text()='Female']/..//input[@type='radio']").click()




