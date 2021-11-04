"""This is the addition calculation"""

from calc.calculation import Calculation

class Addition(Calculation):
    """The addition class has one method"""
    def get_result(self):
        """incapsulation method"""
        return self.value_a + self.value_b
