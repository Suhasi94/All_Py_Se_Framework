import pytest

"""
@pytest.fixture() # setup module
def greet():
    print("***hi***")


def test_spam(greet):
    print("in test spam")


def test_display(greet):
    print("displaying a message")
"""
###########using fixture param autouse= True by default it will be false


"""
@pytest.fixture(autouse=True) # setup module
def greet():
    print("***hi***")


def test_spam():
    print("in test spam")


def test_display():
    print("displaying a message")
"""

"""
@pytest.fixture(autouse=True)
def greet():
    print("***hi***")   # act as setup
    yield
    print("***bye***") # act as teardown

def test_spam(greet):
    print("in test spam")


def test_display(greet):
    print("displaying a message")
"""


@pytest.fixture(scope="class")
def greet():
    print("***hi***")   # act as setup
    yield
    print("***bye***") # act as teardown


@pytest.mark.usefixtures("greet")
class TestSample:
    def test_spam(self):
        print("in test spam")

    def test_display(self):
        print("displaying a message")


