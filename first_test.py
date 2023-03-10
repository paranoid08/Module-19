import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc=Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self,2,2)==4

    def test_division_calculate_correctly(self):
        assert self.calc.division(self,4,2)==2

    def test_multiply_subtraction_correctly(self):
        assert self.calc.subtraction(self,3,1)==2

    def test_multiply_adding_correctly(self):
        assert self.calc.adding(self,3,2)==5

    # def test_multiply_calculate_failed(self): //негативный кейс
    #     assert self.calc.multiply(self,2,2)==5

# def multiply(x,y): // без вызова класса
#     return x*y
#
# def test_multiply_calculate_correctly():
#     assert multiply(2,2)==4