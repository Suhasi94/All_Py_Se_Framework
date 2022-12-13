import pytest

"""
# default autouse=False,scope=function
@pytest.fixture(autouse=True)
def greet():
    print("\nhello world")
    yield
    print("***end***")

def test_spam():
    print("in test spam")

def test_display():
    print("in test display")
"""
######### using class, autouse=True, scope=class

"""
@pytest.fixture(autouse=True,scope="class")
def greet():
    print("\nhello world")
    yield
    print("***end***")

class TestDemo:
    def test_spam(self):
        print("in test spam")

    def test_display(self):
        print("in test display")
"""

## without using autouse

# @pytest.fixture(scope="class")
# def greet():
#     print("\nhello world")
#     yield
#     print("***end***")
#
# @pytest.mark.userfixtures("greet") #if u more fixture u can use ("greet","xyz")
# class TestDemo:
#     def test_spam(self):
#         print("in test spam")
#
#     def test_display(self):
#         print("in test display")


#### scope = module

# @pytest.fixture(scope="module")
# def greet():
#     print("\nhello world")
#     yield
#     print("***end***")
#
# @pytest.mark.userfixtures("greet") #if u more fixture u can use ("greet","xyz")
# class TestDemo:
#     def test_spam(self):
#         print("in test spam")
#
#     def test_display(self):
#         print("in test display")
#
#
# @pytest.mark.userfixtures("greet")
# class TestDemo1:
#     def test_spam(self):
#         print("in test spam")
#
#     def test_display(self):
#         print("in test display")



####################### using pytestmark = pytest.mark.usefixtures


# @pytest.fixture(scope="module")
# def greet():
#     print("\nhello world")
#     yield
#     print("***end***")
#
# pytestmark = pytest.mark.usefixtures("greet")
#
# class TestDemo:
#     def test_spam(self):
#         print("in test spam")
#
#     def test_display(self):
#         print("in test display")
#
# class TestDemo1:
#     def test_spam(self):
#         print("in test spam")
#
#     def test_display(self):
#         print("in test display")






