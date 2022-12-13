from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement


class _visibility_of_element_located(visibility_of_element_located):
    def __init__(self,locator):
        super().__init__(locator)

    def __call__(self,driver):

        print("calling __call__")
        result = super().__call__(driver)
        if isinstance(result,WebElement):
            return result.is_enabled()
        else:
            return False

def wait(func):
    def wrapper(*args, **kwargs): #args=(self,("id","Firstname"))\,kwagrs={"value":"Suhasi"}
        instance = args[0]
        locator = args[1]
        print(f"waiting for element {locator}")
        w = WebDriverWait(instance.driver, 20)
        v = _visibility_of_element_located(locator)
        w.until(v)
        return func(*args,**kwargs)
    return wrapper

# def wait(enabled=True,max_time_out=20):
#     def _wait(func):
#         def wrapper(*args, **kwargs): #args=(self,("id","Firstname"))\,kwagrs={"value":"Suhasi"}
#             instance = args[0]
#             locator = args[1]
#             print(f"waiting for element {locator}")
#             w = WebDriverWait(instance.driver,20)
#             if enabled:
#                 v = _visibility_of_element_located(locator)
#             else:
#                 v = visibility_of_element_located(locator)
#
#             w.until(v)
#             return func(*args,**kwargs)
#         return wrapper
#     return _wait


class SeleniumWrapper:

    def __init__(self,driver):
        self.driver = driver

    @wait
    def enter_text(self,locator,*,value):
        print("calling enter text")
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)
    @wait
    def click_element(self,locator):
        print("calling click element")
        self.driver.find_element(*locator).click()
    @wait
    def select_item(self,locator,*,item):
        element = self.driver.find_element(*locator)
        s = Select(element)
        if isinstance(item,str):
            s.select_by_visible_text(item)
        else:
            s.select_by_index(item)
    @wait
    def select_items(self,locator,*,items):
        for item in items:
            self.select_item(*locator, item)