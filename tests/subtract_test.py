"""testing subtraction class"""

from history.calculations import Calculations
from calculator.calculator import Calculator

def test_csvreader_subtraction(create_csvreader,clear_history_fixture):
    """testing with csv file"""
    data_frame = create_csvreader.show_data_frame("./csv_files/subtraction_test.csv")
    for index, row in data_frame.iterrows():
        index = index + 0
        sub = Calculator.subtract_number((row['value_1'], row['value_2']))
        assert sub == row['result']
    assert Calculations.count_history() == 10
    create_csvreader.edit_data_frame("./csv_files/subtraction_test.csv", "subtraction")
    create_csvreader.move_file("subtraction_test.csv")
