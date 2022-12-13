import pytest
from selenium import webdriver
import time
path = r"../drivers/chromedriver.exe"
#driver = webdriver.Chrome(executable_path=path)
@pytest.fixture()
def _driver():
    driver = webdriver.Chrome(executable_path=path)
    driver.get("https://demowebshop.tricentis.com")
    driver.maximize_window()
    yield driver
    print(driver.title)
    driver.close()