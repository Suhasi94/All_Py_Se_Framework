#8 locators
from selenium import webdriver
import time
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)
url = ("https://demowebshop.tricentis.com/electronics")
driver.get(url)
#driver.find_element_by_id("small-searchterms").send_keys("books")
time.sleep(2)
#driver.find_element_by_name("q").send_keys("books")
#driver.find_element_by_class_name("search-box-text.ui-autocomplete-input").send_keys("book")

#driver.find_element("name","q").click()
#driver.find_element("class name","search-box-text.ui-autocomplete-input").click()
#driver.find_element("id","small-searchterms").click()

#locating using link text
#res=driver.find_element_by_link_text("Register")
#time.sleep(2)
#res.click()
#time.sleep(2)
#driver.back()

# locating using partial link
#res1 = driver.find_element_by_partial_link_text("Regi")
#time.sleep(2)
#res1.click()

# css selector syntax - tagname[attributename=value]
#driver.find_element_by_css_selector('input[type=text]').click()


#xpath --- relative xpath -syntax-- //tagname[@attributename=attributevalue]

#1.absolute xpath - starts from the of the html code
# /html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li/a[1]
#2.Relative xpath - directly jumps to elements dom


#driver.find_element_by_xpath('//a[@class="ico-register"]').click()

#driver.find_element_by_xpath('//a[text()="Register"]').click()
#dependent independent xpath
#url1 = r"C:\Users\User\OneDrive\Desktop\selenium_\demo (1).html"
#driver.get(url1)

#languages = ["Ruby","Java","Perl","Python","C#","JavaScript"]
#for language in languages[::-1]:
    #driver.find_element_by_xpath(f'//td[text()="{language}"]/..//input[@name="download"]').click()

    #time.sleep(2)
url1 = "https://www.python.org/downloads/"
driver.get(url1)
res = driver.find_element_by_xpath('//a[text()="Python 3.9.15"]/../..//a[text()="Release Notes"]')
res.click()










