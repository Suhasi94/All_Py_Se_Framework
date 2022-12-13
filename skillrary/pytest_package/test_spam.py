import pytest
#def test_function1():
#    assert "hai" == "hello"


#def test_function2():
#    assert True

class TestCalculator1:
    a = 10
    b = 5
    def test_add(self):
        assert self.a + self.b == 10,"the sum is not 10"

    @pytest.mark.skip(reason="just skin text_div")
    def test_div(self):
        assert self.a//self.b == 5,"the quotient is not 5"

    @pytest.mark.skipif(b==2,reason="denominator is zero")
    def test_div(self):
        assert self.a//self.b == 2,"the quotient is not 2"



class TestCalculator2:
    a = 10
    b = 5
    def test_add(self):
        assert self.a + self.b == 15,"the sum is not 10"

    @pytest.mark.skip(reason="just skip text_div")
    def test_div(self):
        assert self.a//self.b == 5,"the quotient is not 5"

