"""This is the addition calculation"""

from calc.calculation import Calculation

class Division(Calculation):
    """The addition class has one method to divide two numbers"""
    def get_result(self):
        """This is encapsulation"""
        return self.value_a / self.value_b
