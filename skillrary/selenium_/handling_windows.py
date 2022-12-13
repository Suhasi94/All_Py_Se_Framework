###handling multiple windows
from selenium import webdriver
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)
url = "https://demowebshop.tricentis.com/"
driver.get(url)
driver.implicitly_wait(30)
driver.find_element_by_link_text("Twitter").click()
handles = driver.window_handles
print(handles)
driver.switch_to.window(handles[1])
driver.find_element("xpath",'//span[text()="Follow"]').click()
driver.switch_to.window(handles[0])
driver.find_element_by_link_text("Log in").click()
#driver.switch_to.window(handles[1])
#driver.close()
driver.quit()

