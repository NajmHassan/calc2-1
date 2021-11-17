""" This is the increment function"""
from history.calculations import Calculations

class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_number(arg):
        """ adds list of numbers"""
        return Calculations.add_addition_calculation(arg)
    @staticmethod
    def subtract_number(arg):
        """ subtract a list of numbers"""
        return Calculations.add_subtraction_calculation(arg)
    @staticmethod
    def multiply_number(arg):
        """ mulitply a list of numbers"""
        return Calculations.add_multiply_calculation(arg)
    @staticmethod
    def divide_number(arg):
        """ divide list of numbers"""
        return Calculations.add_division_calculation(arg)
