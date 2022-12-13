import pytest
from selenium import webdriver
#driver = webdriver.Chrome(r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe")

#@pytest.fixture()
#def fixture():
    #driver = webdriver.Chrome(r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe")
    #driver.get("https://demowebshop.tricentis.com/electronics")
    #driver.maximize_window()
    #yield driver
    #print(driver.title)
    #driver.quit()




def test_login(fixture):
    #driver.get("https://demowebshop.tricentis.com/electronics")
    fixture.find_element_by_link_text("Log in").click()

def test_register(fixture):
    #driver.get("https://demowebshop.tricentis.com/electronics")
    fixture.find_element_by_link_text("Register").click()