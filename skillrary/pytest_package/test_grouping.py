#custom markers
from pytest import mark

@mark.smoke
def test_validate_login(): #smoke
    print("executing login test")

@mark.regression
def test_shopping(): #regression
    print("executing shopping test")

@mark.regression
def test_payment(): #regression
    print("executing payment test")

@mark.smoke
def test_registration(): #smoke
    print("executing registration test")



