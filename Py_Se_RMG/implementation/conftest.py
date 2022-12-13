
# to ignore -- pytest --ignore=test_login.py --ignore test_regis.py -vs
# for failed - pytest -vs --last-failed --last-failed-no-failures none
# for reports pytest --html="path".html



import pytest
from selenium import webdriver
import time
path = r"C:\Users\User\PycharmProjects\pythonProject2\Py_Se_RMG\drivers\chromedriver.exe"

@pytest.fixture()
#@pytest.fixture(scope="module")
def init_driver():
    driver = webdriver.Chrome(executable_path=path)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.close()


