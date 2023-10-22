import random
from config import Config
from modules.classes import *


class RandomData:
    def __init__(self):
        self.carriages_types = [SeatCarriage, EconomCarriage, CoupeCarriage, FirstClassCarriage]
        self.carriages_weights = [0.25, 0.3, 0.35, 0.1]

    def generate_routes(self) -> list:
        routes = []

        for i in range(random.randint(Config.ROUTES_MIN_QUANTITY, Config.ROUTES_MAX_QUANTITY)):
            routes.append(
                Route(
                    id=random.randint(1000, 9999),
                    train=Train(),
                    time=f'{random.randint(0, 23):02}:{random.randint(0, 59):02}'
                )
            )

            for j in range(random.randint(Config.CARRIAGE_MIN_QUANTITY, Config.CARRIAGE_MAX_QUANTITY)):
                carriage_type = random.choices(self.carriages_types, self.carriages_weights, k=1)[0]
                routes[-1].train.carriages.append(
                    carriage_type(
                        seats=None
                    )
                )
                for k in range(1, routes[-1].train.carriages[-1].max_seats_quantity + 1):
                    routes[-1].train.carriages[-1].seats.append(
                        Seat(
                            id=k,
                            is_busy=random.choices([True, False], [Config.WAGON_OCCUPANCY, 1 - Config.WAGON_OCCUPANCY])[
                                0]
                        )
                    )

        routes.sort(key=lambda x: (int(x.time.split(':')[0]), int(x.time.split(':')[1])))
        return routes
