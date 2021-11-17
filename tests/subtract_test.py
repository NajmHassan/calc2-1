"""testing subtraction class"""
from calc.subtraction import Subtraction

def test_calculation_subtraction():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (2.0,1.0)
    # Act
    subtraction = Subtraction(mynumbers)
    #Assert
    assert subtraction.get_result() == 1.0

def test_calculation_subtraction2():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (2,2.0) # does not matter if its a float or int, it will be converted regardless
    # Act
    subtraction = Subtraction(mynumbers)
    #Assert
    assert subtraction.get_result() == 0.0
