from selenium import webdriver
import pytest
import time
path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

"""
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()
driver.implicitly_wait(30)


@pytest.mark.parametrize("user_,pwd_",[("admin","manager"),("trainee","trainee")])
def test_login(user_,pwd_):
    driver.find_element_by_id("username").send_keys(user_)
    time.sleep(2)
    driver.find_element("name","pwd").send_keys(pwd_)
    time.sleep(2)
    driver.find_element("xpath","//div[text()='Login ']").click()
    print(driver.title)
    driver.find_element_by_link_text("Logout").click()
"""
"""
@pytest.mark.parametrize("a,b", [(2,3),(4,5),(6,7)])
def test_add(a,b):
    print(a+b)

#test_add(2,3)
#test_add(4,5)

"""

############## @pytest.mark.skip(reason=" ")


class TestCalculator:
    a = 6
    b = 2

    @pytest.mark.skip(reason="simply to check")
    def test_add(self):
        assert self.a + self.b == 8,"invalid output"

    def test_div(self):
        assert self.a/self.b == 3,"invalid divsion"

class TestCalculator1:
    a = 6
    b = 2

    @pytest.mark.skipif(b==2,reason="simply to check")
    def test_add1(self):
        assert self.a + self.b == 8,"invalid output"

    def test_div1(self):
        assert self.a/self.b == 3,"invalid divsion"
        print("condition is passed")











