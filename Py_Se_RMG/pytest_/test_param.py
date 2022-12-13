import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path = r'C:\Users\User\PycharmProjects\pythonProject2\Py_Se_RMG\drivers\chromedriver.exe'


# @pytest.mark.parametrize("a, b", [(1, 2), (3, 4)])
# def test_add(a, b):
#     assert a + b == 10


@pytest.mark.parametrize("username, pwd", [("admin", "manager"), ("user1", "pwd1"), ("trainee", "trainee")])
def test_actitime_login(username, pwd):
    driver = webdriver.Chrome(executable_path=path)

    driver.get("https://demo.actitime.com/login.do")
    driver.maximize_window()

    driver.find_element("id", "username").send_keys(username)
    driver.find_element("name", "pwd").send_keys(pwd)

    driver.find_element("xpath", "//div[text()='Login ']").click()

    wait_ = WebDriverWait(driver, 10)
    try:
        wait_.until(EC.title_is("actiTIME - Enter Time-Track"), message="Invalid credentials")

    except TimeoutException as error_msg:
        raise error_msg

    finally:
        driver.close()