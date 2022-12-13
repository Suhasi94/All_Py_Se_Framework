class SeleniumWrapper:

    def __init__(self, driver):
        self.driver = driver

    def enter_txt(self,locator,value):
        self.driver.find_element(*locator).send_keys(value)

    def click_element(self,locator):
        self.driver.find_element(*locator).click()