"""testing multiplication class"""

from calc.multiplication import Multiplication
def test_calculation_multiplication():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (3.0,3.0)
    # Act
    multiplication = Multiplication(mynumbers)
    #Assert
    assert multiplication.get_result() == 9.0

def test_calculation_multiplication2():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (2,3.0) # does not matter if its a float or int, it will be converted regardless
    # Act
    multiplication = Multiplication(mynumbers)
    #Assert
    assert multiplication.get_result() == 6.0

def test_calculation_multiplication3():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (2,3.0,0) # does not matter if its a float or int, it will be converted regardless
    #Act
    multiplication = Multiplication(mynumbers)
    #Assert
    assert multiplication.get_result() == 0.0
