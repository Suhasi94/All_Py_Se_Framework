from selenium import webdriver
from data import reading_objects
from library.selenium_wrapper import SeleniumWrapper


login_objects = reading_objects.read_locators() #dictionary

class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.sel_wrapper = SeleniumWrapper(driver)

    def enter_username(self):
        self.sel_wrapper.enter_txt(login_objects["txt_username"],"admin")

    def enter_pwd(self):
        self.sel_wrapper.enter_txt(login_objects["txt_password"],"manager")

    def click_login(self):
        self.sel_wrapper.click_element(login_objects["btn_login"])

