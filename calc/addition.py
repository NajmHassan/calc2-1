"""This is the addition calculation"""
from functools import reduce
from calc.calculation import Calculation

class Addition(Calculation):
    """The addition class has one method inherit Calculation class"""
    def get_result(self):
        """incapsulation method"""
        return reduce(lambda x, y:x + y, self.values)
