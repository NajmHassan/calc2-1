"""This is the subtraction calculation"""
from functools import reduce
from calc.calculation import Calculation

class Subtraction(Calculation):
    """The subtraction class"""

    def get_result(self):
        """incapsulation method"""
        return reduce(lambda x, y: x - y, self.values)
