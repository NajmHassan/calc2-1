"""This is our calculation base class / Abstract Class"""

class Calculation:
    """Calculation class """
    def __init__(self,values: tuple):
        """constructor for Calculation Class"""
        self.values = Calculation.convert_floats(values)
    @classmethod
    def create(cls, values: tuple):
        """ factory method"""
        return cls(values)
    @staticmethod
    def convert_floats(values):
        """ converts input from ints to floats and puts them in a lst"""
        lst = []
        for item in values:
            lst.append(float(item))
        return lst
