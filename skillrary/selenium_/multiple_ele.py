from selenium import webdriver
import time
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)
url = ("https://demowebshop.tricentis.com/electronics")
url1 = r"C:\Users\User\OneDrive\Desktop\selenium_\demo (1).html"
driver.get(url1)
#cat_box = driver.find_elements_by_xpath('//div[@class="block block-category-navigation"]//a')
"""
print(cat_box)
for element in cat_box:
    print(element.text)#text of the webelement
"""
#res = driver.find_elements_by_tag_name("input")
#print(len(res))
#res1 = driver.find_elements_by_xpath("//input")
#print(len(res1))
links = driver.find_elements_by_tag_name("a")
for link in links:
    print(link.text)



