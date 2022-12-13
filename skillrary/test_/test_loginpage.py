from POM.login_page import LoginPage

class TestLoginPage:

    def test_login(self,_driver):
        lp = LoginPage(_driver)
        lp.enter_username()
        lp.enter_pwd()
        lp.click_login()
