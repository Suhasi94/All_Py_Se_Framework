# 1. conftest is a special file used to share fixture among testcases
        # no matter how many files u have

# 2. if ur trying to execute any module in pytest it will frst execute the
       #  conftest file


import pytest
from selenium import webdriver
@pytest.fixture()
def fixture():
    driver = webdriver.Chrome(r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe")
    driver.get("https://demowebshop.tricentis.com/electronics")
    driver.maximize_window()
    yield driver
    print(driver.title)
    driver.save_screenshot("test_fixture_ex.png")
    driver.quit()
