import pytest

@pytest.fixture(params=["hello","hai"])
def greet():
    print("---hello----")
    yield
    print("---End---")


def test_spam(greet):
    print()
    print(1+2)

###########


@pytest.fixture(params=["hello", "hai"])
def greet(request):
    # print(request.param)
    print("---hello----")
    yield request.param
    print("---End---")


def test_spam(greet):
    print(greet)
    print(1 + 2)