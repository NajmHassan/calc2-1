""" This is the increment function"""
from history.calculations import Calculations
from calc.addition import Addition

class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_number(values: tuple):
        """ adds list of numbers"""
        return Calculations.add_addition_calculation(Addition.create(values))
    @staticmethod
    def subtract_number(values: tuple):
        """ subtract a list of numbers"""
        return Calculations.add_subtraction_calculation(values)
    @staticmethod
    def multiply_number(values: tuple):
        """ mulitply a list of numbers"""
        return Calculations.add_multiply_calculation(values)
    @staticmethod
    def divide_number(values: tuple):
        """ divide list of numbers"""
        return Calculations.add_division_calculation(values)
