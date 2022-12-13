#pip install pytest-html


import pytest

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