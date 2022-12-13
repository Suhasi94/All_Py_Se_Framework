import pytest


@pytest.fixture(autouse="True",scope="session")
def greet():
    print("****hi****")  # set up module
    yield
    print("***bye****") #teardown module



def test_spam():
    print("in test spam")

def test_display():
    print("in display")


#### class

@pytest.fixture(autouse="True",scope="session")
def greet1():
    print("****hi****")  # set up module
    yield
    print("***bye****") #teardown module

@pytest.mark.usefixtures("greet1")
class TestDemo:
    def test_spam1(self):
        print("in test spam")

    def test_display1(self):
        print("in display")