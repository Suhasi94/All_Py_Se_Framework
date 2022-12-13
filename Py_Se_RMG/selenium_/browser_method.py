from selenium import webdriver
import time
path = r'C:\Users\User\PycharmProjects\pythonProject2\Py_Se_RMG\drivers\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path)
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()
time.sleep(2)
#driver.minimize_window()
#time.sleep(2)
#driver.fullscreen_window()
#driver.back()
#time.sleep(2)
#driver.forward()
print(driver.get_window_size())
print(driver.get_window_position())
driver.quit()