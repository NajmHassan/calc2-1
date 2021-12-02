"""testing calculator history"""
import pytest
from history.calculations import Calculations
from calc.addition import Addition

@pytest.fixture
def clear_history_fixture():
    """method that runs each time a test method runs, clears history"""
    Calculations.clear_history()

@pytest.fixture
def addition_calculation_fixture():
    """method that runs each time a test method runs, creates a calculation"""
    values = (5, 2)
    addition = Addition(values)
    Calculations.add_calculation(addition)

def test_check_calculator_clear_history(clear_history_fixture):
    """testing the number of calculation in history"""
    assert Calculations.count_history() == 0 #should be nothing since param is just clear history

def test_add_calculation_to_history(clear_history_fixture, addition_calculation_fixture):
    """testing the number of calculation in history"""
    assert Calculations.count_history() == 1 #should be 1 because of paramater

def test_clear_calculation_history(clear_history_fixture, addition_calculation_fixture):
    """testing clear history"""
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() is True

def test_get_calculation(clear_history_fixture, addition_calculation_fixture):

    """testing getting a specific calculation out of the history"""
    assert Calculations.get_calculation(0) == 7.0 #initial calculation
