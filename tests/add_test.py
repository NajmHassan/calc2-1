"""testing Addition class"""

from calc.addition import Addition
def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (1.0,2.0)
    # Act
    addition = Addition(mynumbers)
    #Assert
    assert addition.get_result() == 3.0

def test_calculation_addition2():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (1.0,2.0,3.0)
    # Act
    addition = Addition(mynumbers)
    #Assert
    assert addition.get_result() == 6.0

def test_calculation_addition3():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (1,2.0)
    # Act
    addition = Addition(mynumbers)
    #Assert
    assert addition.get_result() == 3.0
