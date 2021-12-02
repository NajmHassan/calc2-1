"""CSV class resides here!"""
import datetime
from pathlib import Path
import pandas as pd
from history.calculations import Calculations
class Csvreader:
    """csv reader Class"""
    data_frame =0
    data = []
    @staticmethod
    def show_data_frame(pathtofile):
        """shows the csv file"""
        data_set = pd.read_csv(str(pathtofile))
        data_frame = pd.DataFrame(data_set)
        return data_frame
    @staticmethod
    def edit_data_frame(pathtofile, operation):
        """edits the csv file"""
        data_set = pd.read_csv(str(pathtofile))
        data_frame = pd.DataFrame(data_set)
        data_frame['myResult'] = Calculations.show_history()
        data_frame['time_stamp'] = datetime.datetime.now()
        data_frame['path to file'] = pathtofile
        data_frame['operation'] = operation
        data_frame.to_csv("./results/" + operation+"-log.csv", encoding='utf-8', index="," )
        print("")
        print(data_frame)
    @staticmethod
    def move_file(filename):
        """moving file to done folder"""
        Path("./csv_files/"+filename).rename("./csv_files_done/"+filename)
