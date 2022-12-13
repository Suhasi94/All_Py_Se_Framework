from selenium import webdriver
import time
path = r"../drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

"""
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(2)
list_web_ele = driver.find_elements("xpath","//div[@class='block block-category-navigation']//a")
print(list_web_ele)
for element in list_web_ele:
    element.click()
    time.sleep(2)
    #driver.back()

"""

#driver.get("file:///C:/Users/User/OneDrive/Desktop/selenium_/demo%20(1).html")
#driver.maximize_window()
#time.sleep(2)

"""
list_webelement = driver.find_elements("xpath","//input[@type='checkbox' and  @name='download']")
for ele in list_webelement:
    ele.click()
    time.sleep(2)
"""

"""
list_webele = driver.find_elements("name","download")
for ele in  list_webele:
    ele.click()
    time.sleep(2)
"""
## in multiple_elements of demo.html

"""
textbox = driver.find_elements("name","fname")
msgs = ["Ruby","Perl","Java","Python","C#","JavaScript","CSS","HTML","PHP"]
for webele_, value in zip(textbox,msgs):
    webele_.send_keys(value)
    time.sleep(2)
"""

driver.get("https://www.python.org/")
driver.maximize_window()
time.sleep(2)
#links = driver.find_elements("tagname","a")
links = driver.find_elements("xpath","//a")
link_text = []
for link in links:
    text_=link.text
    print(link.get_attribute("href"))

    if text_:
        link_text.append(text_)

print(link_text)









