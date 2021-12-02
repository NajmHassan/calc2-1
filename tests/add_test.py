"""testing Addition class"""

from calculator.calculator import Calculator
from history.calculations import Calculations


def test_csvreader_add(create_csvreader,clear_history_fixture):
    """testing with csv file"""
    for index, row in create_csvreader.show_data_frame("./csv_files/addition_test.csv").iterrows():
        index = index+0
        tuple_values = (row['value_1'], row['value_2'])
        addition = Calculator.add_number(tuple_values)
        result = addition
        assert result == row['result']
    assert Calculations.count_history() == 10
    create_csvreader.edit_data_frame("./csv_files/addition_test.csv", "addition")
    create_csvreader.move_file("addition_test.csv")
