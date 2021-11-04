"""This is our calculation base class / Abstract Class"""
class Calculation:
    """Calculation class """
    def __init__(self,value_a, value_b):
        """constructor for Calculation Class"""
        self.value_a = value_a
        self.value_b = value_b

    @classmethod
    def create(cls, value_a, value_b):
        """class factory"""
        return cls(value_a,value_b)

    def bla(self, value_a):
        """ placeholder  for now"""
        return value_a + self.value_a
