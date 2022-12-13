import pytest
from selenium import webdriver
import time
path = r"/drivers/chromedriver.exe"


@pytest.fixture()
def init_driver():
    driver = webdriver.Chrome(executable_path=path)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.close()


def test_login(init_driver):
    driver = init_driver
    driver.find_element("link text","Log in").click()
    driver.find_element("id","Email").send_keys("suhasi7330@gmail.com")
    driver.find_element("id","Password").send_keys("12345")
    time.sleep(3)

def test_register(init_driver):
    driver = init_driver
    driver.find_element("link text", "Register").click()
    driver.find_element("id", "gender-female").click()
    driver.find_element("name","FirstName").send_keys("Suhasi")