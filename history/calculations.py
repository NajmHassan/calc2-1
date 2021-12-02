"""Calculation history Class"""
#from calc.addition import Addition
from calc.divide import Division
from calc.multiplication import Multiplication
from calc.subtraction import Subtraction

class Calculations:
    """Calculation history Class"""
    history = []

    @staticmethod
    def show_history():
        """clearing history"""
        return Calculations.history

    @staticmethod
    def clear_history():
        """clearing history"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """counting history"""
        return len(Calculations.history)

    @staticmethod
    def remove_last_calculation():
        """removing last history calculation"""
        return Calculations.history.pop()

    @staticmethod
    def get_last_calculation():
        """getting last history calculation"""
        return Calculations.history[-1]

    @staticmethod
    def get_first_calculation():
        """getting first history calculation """
        return Calculations.history[0]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation.get_result())

    @staticmethod
    def add_addition_calculation(values):
        """creates addition object, adds the calculation to history using  method add_calculation"""
        Calculations.add_calculation(values)
        return Calculations.get_last_calculation()

    @staticmethod
    def add_subtraction_calculation(values):
        """creates subtract object, adds the calculation to history using  method add_calculation"""
        Calculations.add_calculation(Subtraction.create(values))
        return Calculations.get_last_calculation()

    @staticmethod
    def add_multiply_calculation(values):
        """creates multiply object, adds the calculation to history using  method add_calculation"""
        Calculations.add_calculation(Multiplication.create(values))
        return Calculations.get_last_calculation()

    @staticmethod
    def add_division_calculation(values):
        """creates division object, adds the calculation to history using  method add_calculation"""
        Calculations.add_calculation(Division.create(values))
        return Calculations.get_last_calculation()
