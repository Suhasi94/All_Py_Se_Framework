### xpath using dependent and independent element
# 1. indentify dependent and independent elements
#2. write xpath expression for independent element
#3. traverse backward till we get the common parent for both dep and independ element
#4. locating the dependent element

# /..  ----traverse 1step backward
# /../.. ---for 2 step
# / --- traverse forward


from selenium import webdriver
import time
path = r"../drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
#driver.get("file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html")
#driver.maximize_window()
#time.sleep(2)
#driver.find_element("xpath", "//td[text()='Ruby']/..//input[@name='download']").click()
#languages = ["Ruby","Java","Perl","Python","C#","JavaScript"]
"""
for language in languages[::-1]:
    xpath_value = f"//td[text()='{language}']/..//input[@name='download']"
    driver.find_element("xpath", xpath_value).click()
    time.sleep(2)
"""

driver.get("https://www.python.org/downloads/")
driver.maximize_window()
time.sleep(2)
driver.find_element("xpath", "// a[text() = 'Python 3.9.15'] /../..// a[text() = 'Release Notes']").click()