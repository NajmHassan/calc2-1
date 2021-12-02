"""Fixtures may rest here..."""
import pytest
from csvclass.csvreader import Csvreader
from history.calculations import Calculations
@pytest.fixture(name="clear_history_fixture")
def clear_history_fixture():
    """method that runs each time a test method runs, clears history"""
    Calculations.clear_history()
@pytest.fixture(name="create_csvreader")
def create_csvreader():
    """create object"""
    return Csvreader()
