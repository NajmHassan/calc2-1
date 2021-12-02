"""testing multiplication class"""

from history.calculations import Calculations
from calculator.calculator import Calculator


def test_csvreader_multiply(create_csvreader, clear_history_fixture):
    """testing with csv file"""
    # Arrange
    data_frame = create_csvreader.show_data_frame("./csv_files/multiplication_test.csv")
    for index, row in data_frame.iterrows():
        index =index+0
        # Act
        multiply = Calculator.multiply_number((row['value_1'], row['value_2']))
        # Assert
        assert multiply == row['result']
    assert Calculations.count_history() == 10
    create_csvreader.edit_data_frame("./csv_files/multiplication_test.csv", "multiplication")
    create_csvreader.move_file("multiplication_test.csv")
