"""This is the addition calculation"""
from functools import reduce
from calc.calculation import Calculation

class Division(Calculation):
    """The addition class has one method to divide two numbers"""
    def get_result(self):
        """incapsulation method"""
        return round(reduce(lambda x, y: x / y, self.values),9) #could be wrong
