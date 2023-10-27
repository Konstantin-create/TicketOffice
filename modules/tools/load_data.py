"""
File to load data from files to objects
"""

from modules.tools import file_reader


class DataLoader:
    def __init__(self):
        self.ini_data = file_reader.read_ini()
        self.stations_data = file_reader.read_stations_conf()

    def __load_routes(self) -> None:
        print(self.ini_data)

    def load(self) -> list:
        self.__load_routes()
        return []
