import time
import pytest

pytestmark = pytest.mark.usefixtures("init_driver") #for module

def test_login(init_driver):
    driver = init_driver
    driver.find_element("link text","Log in").click()
    driver.find_element("id","Email").send_keys("suhasi7330@gmail.com")
    driver.find_element("id","Password").send_keys("12345")
    time.sleep(3)