import pytest
from selenium import webdriver
import pytest
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from  webdriver_manager.microsoft import EdgeChromiumDriverManager


#p = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
path = r"C:\Users\User\OneDrive\Desktop\driver_file\chromedriver.exe"
path1 = r"C:\Users\User\OneDrive\Desktop\driver_file\geckodriver.exe"
path2 = r"C:\Users\User\OneDrive\Desktop\driver_file\msedgedriver.exe"


#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary





@pytest.fixture(params=["Chrome","Firefox","Edge"])
def _driver(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
        #driver = webdriver.Chrome(path)


    elif request.param == "Firefox":
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=path1, options=options)
        #driver = webdriver.Firefox(GeckoDriverManager().install())

    elif request.param == "Edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())



    driver.get("https://demo.actitime.com/login.do")
    driver.maximize_window()
    yield driver

