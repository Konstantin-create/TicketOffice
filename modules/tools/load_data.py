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

    def __load_carriages(self, train_id) -> list:
        data = file_reader.read_train(train_id)

        carriages = []
        for key in data.keys():
            for i in data[key]['count_carriages']:
                for _ in range(int(i)):
                    carriages.append(
                        Carriage().get_carriage_type_by_str(key)(
                            price=data[key]['price'],
                            max_seats=data[key]['max_seats']
                        )
                    )

        print(train_id)
        print(carriages)
        print()
        return carriages

    def __load_train(self, train_id: int) -> Train:
        return Train(carriages=self.__load_carriages(train_id))

    def __load_routes(self) -> None:
        for el in self.__ini_data:
            self.__routes.append(Route(train=self.__load_train(el['train']), route=el['route'], time=el['schedule']))

    def load(self) -> list:
        self.__load_routes()
        return self.__routes
