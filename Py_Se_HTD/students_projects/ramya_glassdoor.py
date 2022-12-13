import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

#login_objects = reading_object.read_locators()
path = r"../drivers/chromedriver.exe"
opt = webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")
driver=webdriver.Chrome(path,options=opt)
driver.get("https://www.glassdoor.co.in/index.htm")
driver.maximize_window()
driver.implicitly_wait(50)

class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    def mail_username(self):
        #self.value1 = value1
        #self.driver.find_element(*login_objects['mail_username']).send_keys(self.value1)
        self.driver.find_element("xpath", "//input[@title='Enter Email']").send_keys("kandiramya844@gmail.com")

    def un_submit(self):

        #self.driver.find_element(*login_objects['un_submit']).click()
        driver.find_element("xpath", "//button[@type='submit']").click()


    def mail_pwd(self):
        #self.value2 = value2
        #self.driver.find_element(*login_objects['mail_pwd']).send_keys(self.value2)
        self.driver.find_element("xpath", "//input[@id='inlineUserPassword']").send_keys("Ramya@123")
        time.sleep(1)

    def pwd_submit(self):
        #self.driver.find_element(*login_objects['pwd_submit']).click()
        self.driver.find_element("xpath", "//button[@name='submit']").click()
        time.sleep(5)

    def profile(self):
        time.sleep(10)
        #obj=self.driver.find_element(*login_objects['profile'])
        obj = self.driver.find_element("xpath", '(//div[@class="d-flex"])[8]')
        profile = ActionChains(self.driver)
        profile.move_to_element(obj).perform()

    def signout(self):
        #self.driver.find_element(*login_objects['sign-out']).click()
        self.driver.find_element("xpath",'(//div[@class="d-flex align-items-center py-std col header-menu-item-label"])[33]').click()
        time.sleep(5)

class Facebook_login:

    def __init__(self,driver):
        self.driver = driver

    def facebook(self):
        #self.driver.find_element(*login_objects['facebook']).click()
        self.driver.find_element("xpath", "//button[@class='facebookWhite gd-btn center ']").click()
        time.sleep(5)
        # self.value3 = value3
        # handles = self.driver.window_handles
        # print(handles)
        # self.driver.switch_to.window(handles[1])

    def fb_username(self):
        self.driver.find_element("xpath","//input[@class='inputtext _55r1 inputtext inputtext']").send_keys("ramyakandi08@gmail.com")
        #self.driver.find_element(*login_objects['fb_username']).send_keys(self.value3)


    def fb_pwd(self):
        time.sleep(5)
        #self.value4 = value4
        #self.driver.find_element(*login_objects['fb_pwd']).send_keys(self.value4)
        driver.find_element("xpath", "//input[@autocomplete='current-password']").send_keys("Ramya@123")

    def fb_login(self):
        #self.driver.find_element(*login_objects['fb_login']).click()
        self.driver.find_element("xpath", "//input[@value='Log in']").click()

        time.sleep(5)


lp = LoginPage(driver)
lp.mail_username()
lp.un_submit()
lp.mail_pwd()
lp.pwd_submit()
lp.profile()
lp.signout()
lp1 = Facebook_login(driver)
lp1.facebook()
lp1.fb_username()
lp1.fb_pwd()
lp1.fb_login()
