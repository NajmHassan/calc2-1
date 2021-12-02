"""testing division class"""
import pytest
from calculator.calculator import Calculator
from history.calculations import Calculations


def test_csvreader_divide(create_csvreader, clear_history_fixture):
    """testing with csv file"""
    for index, row in create_csvreader.show_data_frame("./csv_files/division_test.csv").iterrows():
        index =index+0
        divide = Calculator.divide_number((row['value_1'], row['value_2']))
        try:
            assert divide == row['result']
        except ZeroDivisionError:
            with pytest.raises(ZeroDivisionError):
                assert divide.get_result() is True
    assert Calculations.count_history() == 10
    create_csvreader.edit_data_frame("./csv_files/division_test.csv", 'division')
    create_csvreader.move_file("division_test.csv")
