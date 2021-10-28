"""Testing the Calculator"""
import pytest
from calc.main import Calculator


def test_calculator_result():
    """testing calc result is 0"""
    calc = Calculator()
    assert calc.result == 0


def test_calculator_add():
    """Testing the Add function of the calc"""
    #Arrange by instantiating the calc class
    calc = Calculator()
    #Act by calling the method to be tested
    calc.add_number(1,2)
    #Assert that the results are correct
    assert calc.result == 3

def test_calculator_subtract():
    """Testing the subtract method of the calc"""
    # Arrange
    calc = Calculator()
    # Act
    calc.subtract_number(2,1)
    # Assert
    assert calc.get_result() == 1

def test_calculator_multiply():
    """Testing the multiplication method of the calc"""
    # Arrange
    calc = Calculator()
    # Act
    calc.multiply_number(2,3)
    # Assert
    assert calc.get_result() == 6

def test_calculator_divide():
    """Testing the division method of the calc"""
    # Arrange
    calc = Calculator()
    # Act
    calc.divide_number(0,1)
    # Assert
    assert calc.get_result() == 0

def test_calculator_divide_by_0():
    """Testing the division method by0  of the calc"""
    # Arrange
    calc = Calculator()
    # Act & Assert
    with pytest.raises(ZeroDivisionError):
        calc.divide_number(2, 0)
