import time
def test_register(init_driver):
    driver = init_driver
    driver.find_element("link text", "Register").click()
    driver.find_element("id", "gender-female").click()
    driver.find_element("name","FirstName").send_keys("Suhasi")
    time.sleep(3)



