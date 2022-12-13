
def test_register(_driver):

    _driver.find_element_by_link_text("Register").click()

def test_login(_driver):

    _driver.find_element_by_link_text("Log in").click()