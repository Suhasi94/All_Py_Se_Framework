#from selenium import webdriver
import time
#path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
#driver = webdriver.Chrome(executable_path=path)
#driver.get("https://demo.actitime.com/login.do")
#driver.maximize_window()

from Data import reading_objects
login_objects = reading_objects.read_locators()
#print(login_objects)

class Loginpage:
    def __init__(self,driver):
        self.driver = driver

    def enter_username(self):
        self.driver.find_element(*login_objects['txt_username']).send_keys("admin")

    def enter_pwd(self):
        self.driver.find_element(*login_objects['txt_password']).send_keys("manager")

    def click_login(self):
        self.driver.find_element(*login_objects['btn_login']).click()

#lp = Loginpage()
#lp.enter_username()
#lp.enter_pwd()
#lp.click_login()
