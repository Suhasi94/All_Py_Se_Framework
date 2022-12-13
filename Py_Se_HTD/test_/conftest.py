import pytest
from selenium import  webdriver
from Library.config import Config
#path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
#path1 = r'C:\Users\User\Downloads\geckodriver-v0.32.0-win32\geckodriver.exe'
# CROSS BROWSING
@pytest.fixture(params=["Chrome","Firefox","Edge"])
def _driver(request):
    if request.param == "Chrome":
        #driver = webdriver.Chrome(executable_path=Config.Chrome_Driver_Path)
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif request.param == "Firefox":
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=Config.Gecko_Driver_Path, options=options)
        #driver = webdriver.Firefox(GeckoDriverManager().install())
    elif request.param == "Edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    driver.get(Config.URL)
    driver.maximize_window()
    yield driver
    print(driver.title)
    driver.save_screenshot("text_loginpage.png")
    driver.close()
