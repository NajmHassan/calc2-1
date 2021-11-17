"""This is the multiplication calculation"""
from functools import reduce
from calc.calculation import Calculation

class Multiplication(Calculation):
    """The multiplication class"""
    def get_result(self):
        """incapsulation method"""
        return reduce(lambda x, y: x * y, self.values)
