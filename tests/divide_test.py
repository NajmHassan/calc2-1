"""testing division class"""
import pytest
from calc.divide import Division
def test_calculation_division():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (4.0,2.0)
    # Act
    division = Division(mynumbers)
    #Assert
    assert division.get_result() == 2.0

def test_calculation_division2():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (4,2.0) # does not matter if its a float or int, it will be converted regardless
    # Act
    division = Division(mynumbers)
    #Assert
    assert division.get_result() == 2.0
def test_calculation_division_by_zero():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (4,0) # does not matter if its a float or int, it will be converted regardless
    # Act
    division = Division(mynumbers)
    #Assert
    with pytest.raises(ZeroDivisionError):
        division.get_result()
