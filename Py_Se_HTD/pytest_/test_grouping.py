
####  for group testing in terminal
###   pytest test_grouping.py -vs -m regression  ---- only regression test cases
#### pytest test_grouping.py -vs -m smoke  ---- only smoke test cases will run

import pytest
"""
@pytest.mark.smoke
def test_validate_login():  #smoke
    print("validing login details")

@pytest.mark.regression
def test_shopping(): #regression
    print("inside shopping cart")


@pytest.mark.regression
def test_payment(): #regression
    print("paying the bill")

@pytest.mark.smoke
def test_replacement(): #smoke
    print("did not like so replacing it")
    
"""

class TestCalculator:
    a = 9
    b = 1

    @pytest.mark.marker2
    @pytest.mark.marker1
    def test_add(self):
        assert self.a + self.b == 10,"a+b!=0"
        print("condition is passed")

    @pytest.mark.marker2
    def test_sub(self):
        assert self.a - self.b == 0,"difference is not zero"

    def test_mul(self):
        assert self.a * self.b == 100,"product is not 100"

    @pytest.mark.marker1
    def test_div(self):
        assert self.a//self.b == 5,"quotient is not 5"

