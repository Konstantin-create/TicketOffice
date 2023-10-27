"""
File to load data from files to objects
"""

from modules.classes import *
from modules.tools import file_reader


class DataLoader:
    def __init__(self):
        self.__ini_data = file_reader.read_ini()
        self.__stations_data = file_reader.read_stations_conf()
        self.__routes = []

    def __load_routes(self) -> None:

        print(*self.__ini_data, sep='\n')
        for el in self.__ini_data:
            train = Route(train=el['train'], )

    def load(self) -> list:
        self.__load_routes()
        return self.__routes
